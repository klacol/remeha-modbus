# -*- coding: utf-8 -*-
"""Modbus register definitions for Remeha GTW-08.

Based on: Modbus GTW-08 - Liste der Parameter 7740782-01 26072019.pdf

Register addressing:
- Modbus function codes: 03 (Read Holding), 04 (Read Input), 06 (Write Single), 16 (Write Multiple)
- Max 40 registers per read/write operation
"""

from dataclasses import dataclass
from enum import Enum, IntEnum


class DataType(Enum):
    """Supported data types on the Remeha L-Bus."""
    UINT8 = "uint8"
    UINT16 = "uint16"
    UINT32 = "uint32"
    INT8 = "int8"
    INT16 = "int16"
    INT32 = "int32"
    ENUM8 = "enum8"
    BOOL8 = "b8"
    VISIBLE_STRING = "visible_string"
    OCTET_STRING = "octet_string"


class AccessMode(Enum):
    """Register access mode."""
    READ = "read"
    READ_WRITE = "read_write"


@dataclass
class RegisterDefinition:
    """Definition of a single Modbus register or register group."""
    address: int
    name: str
    description: str
    data_type: DataType
    access: AccessMode
    gain: float = 1.0        # Multiplier to convert raw value to real value
    unit: str = ""
    register_count: int = 1  # Number of 16-bit registers this value spans
    enum_values: dict | None = None  # For ENUM8 types


# =============================================================================
# Chapter 6: Überwachung der Hauptsteuerung (Main Controller Monitoring)
# Addresses 256 - 352
# =============================================================================

MAIN_CONTROLLER_REGISTERS = [
    RegisterDefinition(
        address=256, name="power_setpoint",
        description="Leistungssollwert für Heizanforderung",
        data_type=DataType.UINT8, access=AccessMode.READ_WRITE,
        gain=1.0, unit="%",
    ),
    RegisterDefinition(
        address=257, name="temperature_setpoint",
        description="Temperatursollwert für Heizanforderung",
        data_type=DataType.INT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=258, name="algorithm_type",
        description="Art der Regelung",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "beide", 1: "Leistung", 2: "Temperatur", 3: "keine"},
    ),
    RegisterDefinition(
        address=259, name="heat_demand_type",
        description="Art der Heizanforderung",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "keine", 7: "Heizung", 8: "Kühlung"},
    ),
    RegisterDefinition(
        address=272, name="power_actual",
        description="Ist-Leistung (Zusammenfassung aller Kessel)",
        data_type=DataType.UINT8, access=AccessMode.READ,
        gain=1.0, unit="%",
    ),
    RegisterDefinition(
        address=273, name="flow_temperature",
        description="Vorlauftemperatur des Geräts",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=274, name="return_temperature",
        description="Rücklauftemperatur des Geräts",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=275, name="producer_status",
        description="Erzeuger-Statusbitfeld",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=277, name="appliance_error",
        description="Aktueller Fehler Gerät (0xFFFF = kein Fehler)",
        data_type=DataType.UINT16, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=278, name="appliance_error_priority",
        description="Priorität Gerätefehler",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Verriegelung", 3: "Sperrung", 6: "Warnung", 255: "Kein Fehler"},
    ),
    RegisterDefinition(
        address=288, name="burner_starts",
        description="Zähler Brennerstarts",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2,
    ),
    RegisterDefinition(
        address=290, name="burner_hours",
        description="Zähler Brennerstunden",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2, unit="h",
    ),
    RegisterDefinition(
        address=292, name="service_burning_hours",
        description="Brennstunden seit letzter Wartung",
        data_type=DataType.UINT16, access=AccessMode.READ,
        unit="h",
    ),
]


# =============================================================================
# Chapter 7: Gerät (Appliance)
# Addresses 384 - 503
# =============================================================================

APPLIANCE_REGISTERS = [
    RegisterDefinition(
        address=384, name="outside_temperature",
        description="Außentemperaturmessung",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=385, name="season_mode",
        description="Jahreszeitbedingter Modus",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Winter", 1: "Winter Frostschutz", 2: "Sommer Neutralbereich", 3: "Sommer"},
    ),
    RegisterDefinition(
        address=386, name="summer_winter_threshold",
        description="Außentemperatur: Obergrenze für Heizung (30.5 = deaktiviert)",
        data_type=DataType.UINT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=388, name="frost_min_outside_temp",
        description="Außentemperatur für Frostschutzaktivierung",
        data_type=DataType.INT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=389, name="force_summer_mode",
        description="Sommermodus erzwingen",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "Off", 1: "On"},
    ),
    RegisterDefinition(
        address=400, name="flow_temperature",
        description="Vorlauftemperatur",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=401, name="return_temperature",
        description="Rücklauftemperatur",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=402, name="flue_gas_temperature",
        description="Abgastemperatur",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=403, name="heat_pump_flow_temperature",
        description="Vorlauftemperatur Wärmepumpe",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=404, name="heat_pump_return_temperature",
        description="Rücklauftemperatur Wärmepumpe",
        data_type=DataType.INT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=405, name="internal_setpoint",
        description="Interner Sollwert für Trinkwarmwasserbereitung",
        data_type=DataType.UINT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=406, name="ch_setpoint",
        description="Heizungssollwert der Anlage",
        data_type=DataType.UINT16, access=AccessMode.READ,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=409, name="water_pressure",
        description="Aktueller Wasserdruck",
        data_type=DataType.UINT8, access=AccessMode.READ,
        gain=0.1, unit="bar",
    ),
    RegisterDefinition(
        address=410, name="flow_rate",
        description="Durchfluss",
        data_type=DataType.UINT16, access=AccessMode.READ,
        gain=0.01, unit="l/min",
    ),
    RegisterDefinition(
        address=411, name="appliance_status",
        description="Gerätestatus",
        data_type=DataType.ENUM8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=412, name="appliance_sub_status",
        description="Geräte-Substatus",
        data_type=DataType.ENUM8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=413, name="power_actual",
        description="Tatsächlich erzeugte relative Leistung",
        data_type=DataType.UINT16, access=AccessMode.READ,
        gain=0.1, unit="%",
    ),
    RegisterDefinition(
        address=415, name="ionisation_current",
        description="Flammenstrom",
        data_type=DataType.UINT8, access=AccessMode.READ,
        unit="µA",
    ),
    RegisterDefinition(
        address=419, name="burner_starts",
        description="Zähler Brennerstarts",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2,
    ),
    RegisterDefinition(
        address=421, name="burner_hours",
        description="Zähler Brennerstunden",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2, unit="h",
    ),
    RegisterDefinition(
        address=433, name="ch_energy_consumption",
        description="Gesamtenergieverbrauch für Heizung",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2, unit="kWh",
    ),
    RegisterDefinition(
        address=435, name="dhw_energy_consumption",
        description="Gesamtenergieverbrauch für Trinkwasserbereitung",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2, unit="kWh",
    ),
    RegisterDefinition(
        address=437, name="cooling_energy_consumption",
        description="Gesamtenergieverbrauch für Kühlung",
        data_type=DataType.UINT32, access=AccessMode.READ,
        register_count=2, unit="kWh",
    ),
    RegisterDefinition(
        address=500, name="ch_enabled",
        description="Heizung erlaubt",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "Off", 1: "On"},
    ),
    RegisterDefinition(
        address=501, name="dhw_enabled",
        description="Warmwasserbereitung erlaubt",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "Off", 1: "On"},
    ),
    RegisterDefinition(
        address=502, name="cooling_enabled",
        description="Kühlung",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "Off", 1: "Active cooling on", 2: "Free cooling on"},
    ),
]


# =============================================================================
# Chapter 8: Wartung (Maintenance)
# Addresses 512 - 551
# =============================================================================

MAINTENANCE_REGISTERS = [
    RegisterDefinition(
        address=512, name="service_required",
        description="Wartung erforderlich",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Nein", 1: "Ja"},
    ),
    RegisterDefinition(
        address=513, name="service_notification",
        description="Aktuelle oder bevorstehende Wartungsmeldung",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={1: "A", 2: "B", 3: "C", 4: "Benutzerdefiniert"},
    ),
    RegisterDefinition(
        address=514, name="service_burning_hours",
        description="Brennstunden seit Wartung",
        data_type=DataType.UINT16, access=AccessMode.READ,
        unit="h",
    ),
    RegisterDefinition(
        address=515, name="service_operating_hours",
        description="Betriebsstunden seit letzter Wartung",
        data_type=DataType.UINT16, access=AccessMode.READ,
        unit="h",
    ),
    RegisterDefinition(
        address=531, name="appliance_on_error",
        description="Fehler am Gerät vorhanden",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Nein", 1: "Ja"},
    ),
    RegisterDefinition(
        address=532, name="current_error_1",
        description="Fehlercode Instanz 1",
        data_type=DataType.UINT16, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=533, name="error_priority_1",
        description="Fehlerstufe Instanz 1",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Verriegelung", 3: "Sperrung", 6: "Warnung"},
    ),
]


# =============================================================================
# Chapter 5: Systemermittlung (System Discovery)
# Addresses 128 - 200
# =============================================================================

SYSTEM_DISCOVERY_REGISTERS = [
    RegisterDefinition(
        address=128, name="number_of_devices",
        description="Anzahl der elektronischen Platinen",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=189, name="number_of_zones",
        description="Anzahl der vorhandenen Kreise",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=191, name="number_of_zones_ch",
        description="Anzahl der Heizkreise",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=193, name="number_of_zones_dhw",
        description="Anzahl der TWW-Kreise",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=197, name="buffer_tank_active",
        description="Puffertank ist aktiv",
        data_type=DataType.UINT8, access=AccessMode.READ,
    ),
    RegisterDefinition(
        address=198, name="cascade_active",
        description="Gerät ist Teil einer Kaskade",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={0: "Nein", 1: "Kaskadenmaster", 2: "Kaskadenslave"},
    ),
]


# =============================================================================
# Chapter 9: Kreise (Zones) - Template for Zone 1 (base address 640)
# Each zone occupies 512 registers. Zone N starts at 640 + (N-1) * 512
# =============================================================================

ZONE_BASE_ADDRESS = 640
ZONE_REGISTER_SPAN = 512

ZONE_REGISTERS_TEMPLATE = [
    RegisterDefinition(
        address=0, name="zone_type",
        description="Art des Kreises",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={
            0: "nicht vorhanden", 1: "nur HZG", 2: "HZG + Kühlung",
            3: "TWW", 4: "Prozesswärme", 5: "Schwimmbad", 254: "Sonstige",
        },
    ),
    RegisterDefinition(
        address=1, name="zone_function",
        description="Funktion des Kreises",
        data_type=DataType.ENUM8, access=AccessMode.READ,
        enum_values={
            0: "deaktiviert", 1: "ungemischt", 2: "Mischerkreis",
            3: "Schwimmbad", 4: "Hochtemperatur", 5: "Gebläsekonvektor",
            6: "TWW-Speicher", 7: "Elektr. TWW-Speicher", 8: "Zeitprogramm",
            9: "Prozesswärme", 10: "TWW Schichten", 11: "TWW BIC",
            12: "Gewerbl. WW-Speicher", 254: "TWW primär",
        },
    ),
    RegisterDefinition(
        address=8, name="zone_flow_setpoint",
        description="Temperatursollwert für Kreis",
        data_type=DataType.UINT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=9, name="zone_mode",
        description="Modus des Kreises",
        data_type=DataType.ENUM8, access=AccessMode.READ_WRITE,
        enum_values={0: "Zeitprogramm", 1: "Manuell", 2: "Frostschutz"},
    ),
    RegisterDefinition(
        address=10, name="zone_room_setpoint_1",
        description="Raumtemperatursollwert Benutzeraktivität 1",
        data_type=DataType.UINT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=25, name="zone_dhw_comfort_setpoint",
        description="Komfort-Warmwassertemperatur",
        data_type=DataType.UINT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
    RegisterDefinition(
        address=26, name="zone_dhw_reduced_setpoint",
        description="Reduzierte Warmwassertemperatur",
        data_type=DataType.UINT16, access=AccessMode.READ_WRITE,
        gain=0.01, unit="°C",
    ),
]


# =============================================================================
# Invalid values per data type (Section 3.3)
# =============================================================================

INVALID_VALUES = {
    DataType.UINT8: 0xFF,
    DataType.UINT16: 0xFFFF,
    DataType.UINT32: 0xFFFFFFFF,
    DataType.INT8: -128,
    DataType.INT16: -32768,
    DataType.INT32: -2147483648,
}


def get_zone_registers(zone_number: int) -> list[RegisterDefinition]:
    """Get register definitions for a specific zone (1-12).

    Each zone has the same register layout, offset by ZONE_REGISTER_SPAN.
    """
    if not 1 <= zone_number <= 12:
        raise ValueError(f"Zone number must be 1-12, got {zone_number}")

    base = ZONE_BASE_ADDRESS + (zone_number - 1) * ZONE_REGISTER_SPAN
    zone_regs = []
    for template in ZONE_REGISTERS_TEMPLATE:
        reg = RegisterDefinition(
            address=base + template.address,
            name=f"zone{zone_number}_{template.name}",
            description=f"Zone {zone_number}: {template.description}",
            data_type=template.data_type,
            access=template.access,
            gain=template.gain,
            unit=template.unit,
            register_count=template.register_count,
            enum_values=template.enum_values,
        )
        zone_regs.append(reg)
    return zone_regs


# All non-zone registers combined for easy iteration
ALL_REGISTERS = (
    SYSTEM_DISCOVERY_REGISTERS
    + MAIN_CONTROLLER_REGISTERS
    + APPLIANCE_REGISTERS
    + MAINTENANCE_REGISTERS
)
