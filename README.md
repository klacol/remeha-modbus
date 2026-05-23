# remeha_modbus

[![PyPI version](https://img.shields.io/pypi/v/remeha-modbus)](https://pypi.org/project/remeha-modbus/)
[![Python](https://img.shields.io/pypi/pyversions/remeha-modbus)](https://pypi.org/project/remeha-modbus/)
[![License: MIT](https://img.shields.io/pypi/l/remeha-modbus)](https://pypi.org/project/remeha-modbus/)

Python library for accessing Remeha heating systems via Modbus TCP (GTW-08 gateway).

Designed to be used standalone or as the backend for a Home Assistant custom integration.

## Features

- Async Modbus TCP client based on `pymodbus`
- Full register definitions from the [GTW-08 parameter list](docs/Modbus%20GTW-08%20-%20Liste%20der%20Parameter%207740782-01%2026072019.pdf)
- Automatic value scaling (gain) and signed integer handling
- Invalid value detection (returns `None` for disconnected sensors)
- Support for all 12 heating zones
- Read/Write access for configurable parameters

## Supported Registers

| Chapter | Description | Addresses |
|---------|-------------|-----------|
| System Discovery | Device info, zone count | 128 - 200 |
| Main Controller | Setpoints, temperatures, status | 256 - 352 |
| Appliance | Temperatures, pressures, counters | 384 - 503 |
| Maintenance | Service info, error codes | 512 - 551 |
| Zones (1-12) | Per-zone temps, setpoints, programs | 640 - 6783 |

## Installation

```bash
pip install remeha-modbus
```

Or for development:

```bash
git clone https://github.com/klacol/remeha-modbus.git
cd remeha-modbus
pip install -e ".[dev]"
```

## Usage

```python
import asyncio
from remeha_modbus import RemehaModbusClient

async def main():
    client = RemehaModbusClient(host="192.168.1.100", port=502, slave_id=1)
    await client.connect()

    # Read all appliance sensors
    data = await client.read_appliance()
    print(f"Vorlauftemperatur: {data['flow_temperature']} °C")
    print(f"Wasserdruck: {data['water_pressure']} bar")

    # Read a specific zone
    zone1 = await client.read_zone(1)
    print(f"Zone 1 Modus: {zone1['zone1_zone_mode']}")

    await client.disconnect()

asyncio.run(main())
```

## Testing

```bash
pytest tests/ -v
```

Tests use mocked Modbus responses so no hardware is needed.

## Hardware Setup

Requires a **Remeha GTW-08** Modbus gateway connected to the heating system's L-Bus.
The gateway provides Modbus TCP access over Ethernet.

- Set the Modbus address via the GTW-08 rotary switch
- Default port: 502
- Supported baud rates: 9600, 19200, 38400, 57600

## Reference

- [Modbus Parameter Documentation (Markdown)](docs/Modbus%20GTW-08%20-%20Liste%20der%20Parameter%207740782-01%2026072019.md)
- [Original PDF](docs/Modbus%20GTW-08%20-%20Liste%20der%20Parameter%207740782-01%2026072019.pdf)
- [GTW-08 Installation Guide (Home Assistant Community)](https://community.home-assistant.io/t/configuring-modbus-integration-for-remeha-qinta-ace-gas-heating-device/336268)

