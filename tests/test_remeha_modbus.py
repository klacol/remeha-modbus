# -*- coding: utf-8 -*-
"""Tests for remeha_modbus using mocked Modbus responses."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from remeha_modbus.client import RemehaModbusClient
from remeha_modbus.registers import (
    ALL_REGISTERS,
    APPLIANCE_REGISTERS,
    MAIN_CONTROLLER_REGISTERS,
    MAINTENANCE_REGISTERS,
    SYSTEM_DISCOVERY_REGISTERS,
    DataType,
    RegisterDefinition,
    AccessMode,
    INVALID_VALUES,
    get_zone_registers,
)


@pytest.fixture
def client():
    """Create a RemehaModbusClient with mocked transport."""
    with patch("remeha_modbus.client.AsyncModbusTcpClient") as mock_cls:
        mock_instance = MagicMock()
        mock_instance.connected = True
        mock_instance.connect = AsyncMock(return_value=True)
        mock_instance.close = MagicMock()
        mock_cls.return_value = mock_instance
        c = RemehaModbusClient(host="192.168.1.100", port=502, slave_id=1)
        c._client = mock_instance
        yield c


class TestRegisterDefinitions:
    """Test register definition structure."""

    def test_all_registers_have_valid_data_type(self):
        all_regs = (
            SYSTEM_DISCOVERY_REGISTERS
            + MAIN_CONTROLLER_REGISTERS
            + APPLIANCE_REGISTERS
            + MAINTENANCE_REGISTERS
        )
        for reg in all_regs:
            assert isinstance(reg.data_type, DataType)
            assert isinstance(reg.access, AccessMode)

    def test_zone_registers_calculation(self):
        zone1 = get_zone_registers(1)
        zone2 = get_zone_registers(2)

        # Zone 1 starts at 640, zone 2 at 1152
        assert zone1[0].address == 640
        assert zone2[0].address == 1152

        # Names should include zone number
        assert "zone1_" in zone1[0].name
        assert "zone2_" in zone2[0].name

    def test_zone_number_validation(self):
        with pytest.raises(ValueError):
            get_zone_registers(0)
        with pytest.raises(ValueError):
            get_zone_registers(13)

    def test_invalid_values_defined(self):
        assert INVALID_VALUES[DataType.UINT16] == 0xFFFF
        assert INVALID_VALUES[DataType.INT16] == -32768

    def test_register_names_are_unique_across_all_registers(self):
        names = [reg.name for reg in ALL_REGISTERS]
        duplicates = sorted({name for name in names if names.count(name) > 1})
        assert duplicates == [], f"Duplicate register names found: {duplicates}"


class TestClientDecoding:
    """Test register value decoding."""

    def test_decode_uint16(self, client):
        reg = RegisterDefinition(
            address=410, name="flow_rate", description="Durchfluss",
            data_type=DataType.UINT16, access=AccessMode.READ,
            gain=0.01, unit="l/min",
        )
        # Raw value 350 => 3.50 l/min
        result = client._decode_registers([350], reg)
        assert result == 350

    def test_decode_int16_positive(self, client):
        reg = RegisterDefinition(
            address=400, name="flow_temp", description="Vorlauftemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        # Raw 4500 => 45.00 °C
        result = client._decode_registers([4500], reg)
        assert result == 4500

    def test_decode_int16_negative(self, client):
        reg = RegisterDefinition(
            address=384, name="outside_temp", description="Außentemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        # Raw 0xFFF6 = 65526 => should be -10
        result = client._decode_registers([0xFFF6], reg)
        assert result == -10

    def test_decode_uint32(self, client):
        reg = RegisterDefinition(
            address=288, name="burner_starts", description="Brennerstarts",
            data_type=DataType.UINT32, access=AccessMode.READ,
            register_count=2,
        )
        # High word: 0x0001, Low word: 0x86A0 => 100000
        result = client._decode_registers([0x0001, 0x86A0], reg)
        assert result == 100000

    def test_decode_uint8_from_register(self, client):
        reg = RegisterDefinition(
            address=272, name="power_actual", description="Ist-Leistung",
            data_type=DataType.UINT8, access=AccessMode.READ,
            gain=1.0, unit="%",
        )
        # Register value 0x0048 => UINT8 from LSB = 72
        result = client._decode_registers([0x0048], reg)
        assert result == 72

    def test_decode_enum8(self, client):
        reg = RegisterDefinition(
            address=385, name="season_mode", description="Jahresmodus",
            data_type=DataType.ENUM8, access=AccessMode.READ,
            enum_values={0: "Winter", 1: "Winter Frostschutz", 2: "Sommer Neutralbereich", 3: "Sommer"},
        )
        result = client._decode_registers([0x0003], reg)
        assert result == 3  # decode returns raw, enum resolution happens in read_register


class TestClientReadRegister:
    """Test full read_register flow with mocked Modbus responses."""

    @pytest.mark.asyncio
    async def test_read_temperature(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [4500]  # 45.00 °C
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=400, name="flow_temperature", description="Vorlauftemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        result = await client.read_register(reg)
        assert result == 45.0

    @pytest.mark.asyncio
    async def test_read_negative_temperature(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [0xFF9C]  # -100 raw => -1.00 °C
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=384, name="outside_temperature", description="Außentemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        result = await client.read_register(reg)
        assert result == -1.0

    @pytest.mark.asyncio
    async def test_read_invalid_value_returns_none(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [0x8000]  # INT16 invalid sentinel
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=384, name="outside_temperature", description="Außentemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        result = await client.read_register(reg)
        assert result is None

    @pytest.mark.asyncio
    async def test_read_enum_value(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [0x0001]  # "Ja"
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=512, name="service_required", description="Wartung erforderlich",
            data_type=DataType.ENUM8, access=AccessMode.READ,
            enum_values={0: "Nein", 1: "Ja"},
        )
        result = await client.read_register(reg)
        assert result == "Ja"

    @pytest.mark.asyncio
    async def test_read_uint32_counter(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [0x0000, 0x2710]  # 10000
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=288, name="burner_starts", description="Brennerstarts",
            data_type=DataType.UINT32, access=AccessMode.READ,
            register_count=2,
        )
        result = await client.read_register(reg)
        assert result == 10000

    @pytest.mark.asyncio
    async def test_read_water_pressure(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        mock_response.registers = [0x0012]  # 18 raw => 1.8 bar
        client._client.read_holding_registers = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=409, name="water_pressure", description="Wasserdruck",
            data_type=DataType.UINT8, access=AccessMode.READ,
            gain=0.1, unit="bar",
        )
        result = await client.read_register(reg)
        assert result == 1.8


class TestClientWriteRegister:
    """Test write operations."""

    @pytest.mark.asyncio
    async def test_write_temperature_setpoint(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        client._client.write_register = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=257, name="temperature_setpoint", description="Temperatursollwert",
            data_type=DataType.INT16, access=AccessMode.READ_WRITE,
            gain=0.01, unit="°C",
        )
        # Write 55.0 °C => raw value 5500
        await client.write_register(reg, 55.0)

        client._client.write_register.assert_called_once_with(
            address=257, value=5500, device_id=1,
        )

    @pytest.mark.asyncio
    async def test_write_read_only_raises(self, client):
        reg = RegisterDefinition(
            address=400, name="flow_temperature", description="Vorlauftemperatur",
            data_type=DataType.INT16, access=AccessMode.READ,
            gain=0.01, unit="°C",
        )
        with pytest.raises(ValueError, match="read-only"):
            await client.write_register(reg, 50.0)

    @pytest.mark.asyncio
    async def test_write_enum_value(self, client):
        mock_response = MagicMock()
        mock_response.isError.return_value = False
        client._client.write_register = AsyncMock(return_value=mock_response)

        reg = RegisterDefinition(
            address=500, name="ch_enabled", description="Heizung erlaubt",
            data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
            enum_values={0: "Off", 1: "On"},
        )
        await client.write_register(reg, 1)

        client._client.write_register.assert_called_once_with(
            address=500, value=1, device_id=1,
        )


class TestDecodeBitfield:
    """Test bitfield decoding."""

    def test_single_bit_set(self):
        from remeha_modbus.registers import decode_bitfield
        reg = RegisterDefinition(
            address=279, name="appliance_status_1", description="Gerätestatus 1",
            data_type=DataType.UINT16, access=AccessMode.READ,
            bit_definitions={0: "flame", 1: "heat_pump", 5: "maintenance_required"},
        )
        assert decode_bitfield(reg, 1) == "flame"

    def test_multiple_bits_set(self):
        from remeha_modbus.registers import decode_bitfield
        reg = RegisterDefinition(
            address=279, name="appliance_status_1", description="Gerätestatus 1",
            data_type=DataType.UINT16, access=AccessMode.READ,
            bit_definitions={0: "flame", 5: "maintenance_required"},
        )
        # 33 = 0b00100001 => Bit0 + Bit5
        assert decode_bitfield(reg, 33) == "flame, maintenance_required"

    def test_no_bits_set(self):
        from remeha_modbus.registers import decode_bitfield
        reg = RegisterDefinition(
            address=276, name="producer_request", description="Erzeuger-Anforderung",
            data_type=DataType.UINT8, access=AccessMode.READ,
            bit_definitions={0: "frost_protection", 1: "frost_protection_pump_only"},
        )
        assert decode_bitfield(reg, 0) == ""

    def test_undefined_bit_shows_bit_number(self):
        from remeha_modbus.registers import decode_bitfield
        reg = RegisterDefinition(
            address=279, name="appliance_status_1", description="Gerätestatus 1",
            data_type=DataType.UINT16, access=AccessMode.READ,
            bit_definitions={0: "flame"},
        )
        # 3 = 0b11 => Bit0 defined, Bit1 undefined
        assert decode_bitfield(reg, 3) == "flame, Bit1"

    def test_no_bit_definitions_returns_empty(self):
        from remeha_modbus.registers import decode_bitfield
        reg = RegisterDefinition(
            address=272, name="power_actual", description="Ist-Leistung",
            data_type=DataType.UINT8, access=AccessMode.READ,
        )
        assert decode_bitfield(reg, 42) == ""
