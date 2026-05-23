# -*- coding: utf-8 -*-
"""Device identification mapping for Remeha boilers connected via GTW-08.

The GTW-08 Modbus interface does not expose a human-readable device name.
This mapping table allows identification of the boiler model based on the
article numbers and device types read from the Modbus registers.

Community contributions welcome! If you have a Remeha boiler with a GTW-08,
please submit a PR or issue with:
  - Your boiler model name (from the type plate)
  - The output of: scripts/test_connection.py (Device Info section)
"""

from dataclasses import dataclass


@dataclass
class DeviceIdentification:
    """Known device identification entry."""
    model: str
    article_numbers: list[int]
    device_type: int | None = None
    notes: str = ""


# =============================================================================
# Known device mappings
#
# To add your device:
# 1. Run scripts/test_connection.py and note the Device Info output
# 2. Add an entry below with:
#    - model: The commercial name from your boiler's type plate
#    - article_numbers: The article_number values from board info
#    - device_type: The device_type_gtw08 value (optional)
#    - notes: Any additional info (power rating, variant, etc.)
# 3. Submit a PR to https://github.com/klacol/remeha-modbus
# =============================================================================

KNOWN_DEVICES: list[DeviceIdentification] = [
    DeviceIdentification(
        model="Remeha Quinta Ace 160",
        article_numbers=[7724481, 7651932],
        device_type=7688,
        notes="160 kW, board3=7724481, board4=7651932",
    ),
]


def identify_device(
    article_numbers: list[int],
    device_type: int | None = None,
) -> str | None:
    """Try to identify the boiler model from article numbers and device type.

    Returns the model name if a match is found, None otherwise.
    """
    for device in KNOWN_DEVICES:
        # Match if any known article number is present
        if any(an in article_numbers for an in device.article_numbers):
            return device.model
        # Fallback: match on device_type alone if specified
        if device_type and device.device_type == device_type:
            return device.model
    return None
