# -*- coding: utf-8 -*-
"""Modbus TCP client for Remeha GTW-08 gateway."""

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException

from .registers import (
    ALL_REGISTERS,
    APPLIANCE_REGISTERS,
    DEVICE_INFO_REGISTERS,
    INVALID_VALUES,
    MAIN_CONTROLLER_REGISTERS,
    MAINTENANCE_REGISTERS,
    SYSTEM_DISCOVERY_REGISTERS,
    AccessMode,
    DataType,
    RegisterDefinition,
    get_board_registers,
    get_zone_registers,
)

DEFAULT_PORT = 502
DEFAULT_DEVICE_ID = 100  # GTW-08 default rotary switch position


class _NotSupported:
    """Sentinel indicating a register is not supported by the device."""
    def __repr__(self):
        return "NOT_SUPPORTED"


NOT_SUPPORTED = _NotSupported()


class RemehaModbusClient:
    """Client to communicate with a Remeha heating system via Modbus TCP (GTW-08)."""

    def __init__(self, host: str, port: int = DEFAULT_PORT, slave_id: int = DEFAULT_DEVICE_ID):
        """Initialize the client.

        Args:
            host: IP address or hostname of the GTW-08 gateway.
            port: Modbus TCP port (default 502).
            slave_id: Modbus device address (set via GTW-08 rotary switch).
        """
        self.host = host
        self.port = port
        self.device_id = slave_id
        self._client = AsyncModbusTcpClient(host=host, port=port)

    async def connect(self) -> bool:
        """Connect to the GTW-08 gateway."""
        return await self._client.connect()

    async def disconnect(self) -> None:
        """Disconnect from the GTW-08 gateway."""
        self._client.close()

    @property
    def connected(self) -> bool:
        """Return True if connected."""
        return self._client.connected

    async def read_register(self, register: RegisterDefinition) -> int | float | str | None:
        """Read a single register definition and return the decoded value.

        Returns None if the value is the 'invalid' sentinel for its data type.
        """
        try:
            result = await self._client.read_holding_registers(
                address=register.address,
                count=register.register_count,
                device_id=self.device_id,
            )
        except ModbusException as e:
            raise ConnectionError(f"Modbus read failed at address {register.address}: {e}") from e

        if result.isError():
            raise ConnectionError(f"Modbus error response for address {register.address}: {result}")

        raw_value = self._decode_registers(result.registers, register)

        # Check for invalid sentinel value
        invalid = INVALID_VALUES.get(register.data_type)
        if invalid is not None and raw_value == invalid:
            return None

        # Apply gain/scaling
        if register.gain != 1.0 and isinstance(raw_value, (int, float)):
            return round(raw_value * register.gain, 4)

        # Resolve enum
        if register.data_type == DataType.ENUM8 and register.enum_values:
            return register.enum_values.get(raw_value, f"unknown({raw_value})")

        return raw_value

    async def write_register(self, register: RegisterDefinition, value: int | float) -> None:
        """Write a value to a register.

        The value should be in real units (gain is applied in reverse).
        """
        if register.access != AccessMode.READ_WRITE:
            raise ValueError(f"Register {register.name} is read-only")

        # Reverse gain to get raw value
        if register.gain != 1.0:
            raw_value = int(round(value / register.gain))
        else:
            raw_value = int(value)

        try:
            if register.register_count == 1:
                result = await self._client.write_register(
                    address=register.address,
                    value=raw_value,
                    device_id=self.device_id,
                )
            else:
                # Split into multiple 16-bit registers (big-endian)
                registers = self._encode_value(raw_value, register.register_count)
                result = await self._client.write_registers(
                    address=register.address,
                    values=registers,
                    device_id=self.device_id,
                )
        except ModbusException as e:
            raise ConnectionError(f"Modbus write failed at address {register.address}: {e}") from e

        if result.isError():
            raise ConnectionError(f"Modbus write error for address {register.address}: {result}")

    async def read_all_sensors(self) -> dict[str, int | float | str | None]:
        """Read all standard sensor registers and return as a dict."""
        data = {}
        for register in ALL_REGISTERS:
            try:
                value = await self.read_register(register)
                data[register.name] = value
            except ConnectionError:
                data[register.name] = None
        return data

    async def read_appliance(self) -> dict[str, int | float | str | None]:
        """Read appliance (Gerät) registers."""
        return await self._read_register_group(APPLIANCE_REGISTERS)

    async def read_device_info(self) -> dict[str, int | float | str | None]:
        """Read GTW-08 device info and board details."""
        data = await self._read_register_group(DEVICE_INFO_REGISTERS)
        # Read board info for each detected board
        num_devices = data.get("number_of_devices_from_discovery")
        # Read board 1 always, then up to number_of_devices
        discovery = await self._read_register_group(SYSTEM_DISCOVERY_REGISTERS)
        num_boards = discovery.get("number_of_devices") or 1
        for i in range(1, min(int(num_boards), 10) + 1):
            board_regs = get_board_registers(i)
            board_data = await self._read_register_group(board_regs)
            data[f"board_{i}"] = board_data
        return data

    async def read_main_controller(self) -> dict[str, int | float | str | None]:
        """Read main controller monitoring registers."""
        return await self._read_register_group(MAIN_CONTROLLER_REGISTERS)

    async def read_maintenance(self) -> dict[str, int | float | str | None]:
        """Read maintenance registers."""
        return await self._read_register_group(MAINTENANCE_REGISTERS)

    async def read_system_discovery(self) -> dict[str, int | float | str | None]:
        """Read system discovery registers."""
        return await self._read_register_group(SYSTEM_DISCOVERY_REGISTERS)

    async def read_zone(self, zone_number: int) -> dict[str, int | float | str | None]:
        """Read all registers for a specific zone (1-12)."""
        zone_regs = get_zone_registers(zone_number)
        return await self._read_register_group(zone_regs)

    async def _read_register_group(self, registers: list[RegisterDefinition]) -> dict:
        """Read a group of registers.

        Returns a dict with:
        - decoded value for successful reads
        - None for invalid/not-available sentinel values
        - NOT_SUPPORTED for registers the device doesn't support
        """
        data = {}
        for register in registers:
            try:
                value = await self.read_register(register)
                data[register.name] = value
            except ConnectionError:
                data[register.name] = NOT_SUPPORTED
        return data

    def _decode_registers(self, registers: list[int], definition: RegisterDefinition) -> int | str:
        """Decode raw 16-bit register values to a single value based on data type."""
        # VISIBLE_STRING: decode as ASCII from register bytes
        if definition.data_type == DataType.VISIBLE_STRING:
            raw_bytes = b""
            for reg in registers:
                raw_bytes += reg.to_bytes(2, byteorder="big")
            return raw_bytes.decode("ascii", errors="replace").rstrip("\x00 ")

        if definition.register_count == 1:
            raw = registers[0]
        elif definition.register_count == 2:
            # 32-bit: first register is high word, second is low word
            raw = (registers[0] << 16) | registers[1]
        else:
            # Multi-register large value
            raw = 0
            for reg in registers:
                raw = (raw << 16) | reg
            return raw

        # Handle signed types
        if definition.data_type in (DataType.INT16, DataType.INT8):
            if raw >= 0x8000:
                raw -= 0x10000
        elif definition.data_type == DataType.INT32:
            if raw >= 0x80000000:
                raw -= 0x100000000

        # For UINT8/ENUM8/BOOL8, value is in LSB of the register
        if definition.data_type in (DataType.UINT8, DataType.ENUM8, DataType.BOOL8):
            raw = raw & 0xFF

        return raw

    @staticmethod
    def _encode_value(value: int, register_count: int) -> list[int]:
        """Encode a value into a list of 16-bit register values (big-endian)."""
        registers = []
        for i in range(register_count - 1, -1, -1):
            registers.insert(0, (value >> (i * 16)) & 0xFFFF)
        return registers
