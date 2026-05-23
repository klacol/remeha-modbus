#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick connection test for the Remeha Modbus gateway via Waveshare ETH adapter.

Tests in 3 stages:
1. Ping (ICMP reachability)
2. TCP port check (port 502 open?)
3. Modbus register read
"""

import asyncio
import socket
import subprocess
import sys

sys.path.insert(0, ".")

from remeha_modbus.client import NOT_SUPPORTED, RemehaModbusClient
from remeha_modbus.device_map import identify_device
from remeha_modbus.registers import (
    APPLIANCE_REGISTERS,
    MAIN_CONTROLLER_REGISTERS,
    SYSTEM_DISCOVERY_REGISTERS,
    RegisterDefinition,
)

# Build lookup: register name -> RegisterDefinition
_REG_LOOKUP: dict[str, RegisterDefinition] = {}
for _reg in SYSTEM_DISCOVERY_REGISTERS + MAIN_CONTROLLER_REGISTERS + APPLIANCE_REGISTERS:
    _REG_LOOKUP[_reg.name] = _reg


def _format_value(name: str, value) -> str:
    """Format a register value with unit and gain info for display."""
    if value is NOT_SUPPORTED:
        return f"  {name}: [read error]"
    if value is None:
        return f"  {name}: [not supported]"
    reg = _REG_LOOKUP.get(name)
    if reg is None:
        return f"  {name}: {value}"
    unit = f" {reg.unit}" if reg.unit else ""
    gain_info = f"  (gain={reg.gain})" if reg.gain != 1.0 else ""
    return f"  {name}: {value}{unit}{gain_info}"


_legend_printed = False


def _print_legend():
    global _legend_printed
    if not _legend_printed:
        print()
        print("  Legend: [not supported] = device returned 0xFF/0xFFFF (feature not available)")
        print("          [read error]    = device returned Modbus error (register unknown)")
        _legend_printed = True

# Waveshare RS232/485 ETH Modbus Gateway
GATEWAY_HOST = "192.168.1.224"
GATEWAY_PORT = 502
DEVICE_ID = 100  # GTW-08 Modbus-Adresse lt. Kodierrad-Einstellung


def test_ping(host: str, count: int = 3, timeout: int = 5, label: str = "") -> bool:
    """Stage 1: ICMP ping test."""
    if label:
        print(f"{label} Ping {host} ...")
    else:
        print(f"    Ping {host} ...")
    result = subprocess.run(
        ["ping", "-c", str(count), "-W", str(timeout), host],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        # Extract round-trip time from last line
        for line in result.stdout.splitlines():
            if "rtt" in line or "round-trip" in line:
                print(f"      OK - {line.strip()}")
                break
        else:
            print("      OK - Host erreichbar")
        return True
    else:
        print(f"      FEHLER - Host nicht erreichbar")
        print(f"      {result.stderr.strip() or result.stdout.strip()}")
        return False


def test_port(host: str, port: int, timeout: int = 5) -> bool:
    """Stage 2: TCP port connectivity test."""
    print(f"[2/3] TCP-Verbindung zu {host}:{port} ...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        print(f"      OK - Port {port} ist offen")
        return True
    except socket.timeout:
        print(f"      FEHLER - Timeout (Port {port} antwortet nicht)")
        return False
    except ConnectionRefusedError:
        print(f"      FEHLER - Verbindung abgelehnt (Port {port} geschlossen)")
        return False
    except OSError as e:
        print(f"      FEHLER - {e}")
        return False
    finally:
        sock.close()


async def test_modbus(host: str, port: int, device_id: int) -> bool:
    """Stage 3: Modbus register read test."""
    print(f"[3/3] Modbus-Verbindung (Device {device_id}) ...")

    client = RemehaModbusClient(host=host, port=port, slave_id=device_id)

    try:
        connected = await client.connect()
        if not connected:
            print("      FEHLER - Modbus-Verbindung fehlgeschlagen")
            return False

        print("      OK - Verbunden\n")

        # Geräteinformation (Stammdaten)
        print("=== Geräteinformation (Device Info) ===")
        try:
            device_info = await client.read_device_info()
            # Collect article numbers for device identification
            article_numbers = []
            for name, value in device_info.items():
                if isinstance(value, dict):
                    # Board sub-dict: strip boardN_ prefix from keys
                    prefix = name.replace("_", "") + "_"  # "board_1" -> "board1_"
                    board_values = []
                    for k, v in value.items():
                        if v is None or v is NOT_SUPPORTED:
                            continue
                        short_key = k.replace(prefix, "", 1)
                        board_values.append(f"{short_key}={v}")
                        if short_key == "article_number":
                            article_numbers.append(int(v))
                    if board_values:
                        print(f"  {name}: {', '.join(board_values)}")
                else:
                    print(_format_value(name, value))
            # Try to identify the boiler model
            device_type = device_info.get("device_type_gtw08")
            model = identify_device(article_numbers, device_type)
            if model:
                print(f"\n  >>> Gerät erkannt: {model}")
            else:
                print(f"\n  >>> Gerät unbekannt. Bitte melden unter:")
                print(f"      https://github.com/klacol/remeha-modbus/issues")
                print(f"      (Modellname vom Typenschild + obige Werte angeben)")
        except Exception as e:
            print(f"  Fehler: {e}")

        print()

        # System Discovery lesen
        print("=== System Discovery ===")
        try:
            discovery = await client.read_system_discovery()
            for name, value in discovery.items():
                print(_format_value(name, value))
        except Exception as e:
            print(f"  Fehler: {e}")
        _print_legend()

        print()

        # Hauptregler-Daten lesen
        print("=== Hauptregler (Main Controller) ===")
        try:
            main_ctrl = await client.read_main_controller()
            for name, value in main_ctrl.items():
                print(_format_value(name, value))
        except Exception as e:
            print(f"  Fehler: {e}")

        print()

        # Gerätedaten lesen
        print("=== Gerät (Appliance) ===")
        try:
            appliance = await client.read_appliance()
            for name, value in appliance.items():
                print(_format_value(name, value))
        except Exception as e:
            print(f"  Fehler: {e}")

        return True

    except ConnectionError as e:
        print(f"      Verbindungsfehler: {e}")
        return False
    except Exception as e:
        print(f"      Unerwarteter Fehler: {e}")
        return False
    finally:
        await client.disconnect()


ROUTER_HOST = "192.168.1.1"


async def main():
    print(f"Remeha Modbus Gateway Test: {GATEWAY_HOST}:{GATEWAY_PORT}")
    print("=" * 60)
    print()

    # Stage 0: VPN check (ping router)
    print(f"[0/3] VPN-Prüfung (Ping {ROUTER_HOST}) ...")
    if not test_ping(ROUTER_HOST):
        print("\n>>> Abbruch: Router nicht erreichbar. Ist das VPN aktiv?")
        sys.exit(1)

    print()

    # Stage 1: Ping Gateway
    print(f"[1/3] Ping Gateway ({GATEWAY_HOST}) ...")
    if not test_ping(GATEWAY_HOST):
        print("\n>>> Abbruch: Gateway nicht erreichbar. Ist das Gerät eingeschaltet?")
        sys.exit(1)

    print()

    # Stage 2: Port check
    if not test_port(GATEWAY_HOST, GATEWAY_PORT):
        print("\n>>> Abbruch: Port nicht erreichbar. Ist das Gateway eingeschaltet?")
        sys.exit(2)

    print()

    # Stage 3: Modbus
    success = await test_modbus(GATEWAY_HOST, GATEWAY_PORT, DEVICE_ID)

    print()
    print("=" * 60)
    if success:
        print("ERGEBNIS: Alle Tests erfolgreich!")
    else:
        print("ERGEBNIS: Modbus-Kommunikation fehlgeschlagen.")
        sys.exit(3)


if __name__ == "__main__":
    asyncio.run(main())
