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

from remeha_modbus.client import RemehaModbusClient

# Waveshare RS232/485 ETH Modbus Gateway
GATEWAY_HOST = "192.168.1.224"
GATEWAY_PORT = 502
SLAVE_ID = 1


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


async def test_modbus(host: str, port: int, slave_id: int) -> bool:
    """Stage 3: Modbus register read test."""
    print(f"[3/3] Modbus-Verbindung (Slave {slave_id}) ...")

    client = RemehaModbusClient(host=host, port=port, slave_id=slave_id)

    try:
        connected = await client.connect()
        if not connected:
            print("      FEHLER - Modbus-Verbindung fehlgeschlagen")
            return False

        print("      OK - Verbunden\n")

        # System Discovery lesen
        print("=== System Discovery ===")
        try:
            discovery = await client.read_system_discovery()
            for name, value in discovery.items():
                print(f"  {name}: {value}")
        except Exception as e:
            print(f"  Fehler: {e}")

        print()

        # Hauptregler-Daten lesen
        print("=== Hauptregler (Main Controller) ===")
        try:
            main_ctrl = await client.read_main_controller()
            for name, value in main_ctrl.items():
                if value is not None:
                    print(f"  {name}: {value}")
        except Exception as e:
            print(f"  Fehler: {e}")

        print()

        # Gerätedaten lesen
        print("=== Gerät (Appliance) ===")
        try:
            appliance = await client.read_appliance()
            for name, value in appliance.items():
                if value is not None:
                    print(f"  {name}: {value}")
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
    success = await test_modbus(GATEWAY_HOST, GATEWAY_PORT, SLAVE_ID)

    print()
    print("=" * 60)
    if success:
        print("ERGEBNIS: Alle Tests erfolgreich!")
    else:
        print("ERGEBNIS: Modbus-Kommunikation fehlgeschlagen.")
        sys.exit(3)


if __name__ == "__main__":
    asyncio.run(main())
