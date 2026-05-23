# Bitfeld-Unterstützung in der remeha_modbus Library

## Problem

Einige Modbus-Register sind Bitfelder (z.B. `producer_request`, `appliance_status_1`, `appliance_status_2`). Die Library liefert für diese Register nur den rohen Integer-Wert (z.B. `66`), was für Endnutzer unverständlich ist.

Die Bit-Definitionen stecken aktuell nur im `description`-String der `RegisterDefinition`, sind aber nicht maschinenlesbar:

```python
# Aktuell:
RegisterDefinition(
    name="producer_request",
    data_type=DataType.UINT8,
    description="Erzeuger-Anforderung (Bit0=Frostschutz, Bit1=Frostschutz nur Pumpe, ...)"
)
```

## Betroffene Register

| Register | DataType | Bit-Definitionen |
|----------|----------|-----------------|
| `producer_request` | UINT8 | Bit0=Frostschutz, Bit1=Frostschutz nur Pumpe, Bit2=Schornsteinfeger, Bit3=Wartungsanforderung |
| `appliance_status_1` | UINT16 | Bit0=Flamme, Bit1=Wärmepumpe, Bit2=Elektr. Zusatzerzeuger, Bit3=Elektr. Zusatzerzeuger 2, Bit4=TWW Elektr. Zusatzerzeuger, Bit5=Wartung erforderlich, Bit6=Reset erforderlich, Bit7=Wasserdruck gering |
| `appliance_status_2` | UINT16 | Bit0=Pumpe, Bit1=3-Wege-Ventil offen, Bit2=3-Wege-Ventil, Bit3=3-Wege-Ventil geschlossen, Bit4=TWW aktiv, Bit5=Heizung aktiv, Bit6=Kühlung aktiv |

## Gewünschte Lösung

### 1. `bit_definitions` Feld in `RegisterDefinition` hinzufügen

```python
@dataclass
class RegisterDefinition:
    name: str
    address: int
    data_type: DataType
    # ... bestehende Felder ...
    enum_values: dict[int, str] | None = None
    bit_definitions: dict[int, str] | None = None  # NEU
```

### 2. Register mit Bit-Definitionen versehen

```python
RegisterDefinition(
    name="producer_request",
    data_type=DataType.UINT8,
    description="Erzeuger-Anforderung",
    bit_definitions={
        0: "Frostschutz",
        1: "Frostschutz nur Pumpe",
        2: "Schornsteinfeger",
        3: "Wartungsanforderung",
    },
)

RegisterDefinition(
    name="appliance_status_1",
    data_type=DataType.UINT16,
    description="Gerätestatus 1",
    bit_definitions={
        0: "Flamme",
        1: "Wärmepumpe",
        2: "Elektr. Zusatzerzeuger",
        3: "Elektr. Zusatzerzeuger 2",
        4: "TWW Elektr. Zusatzerzeuger",
        5: "Wartung erforderlich",
        6: "Reset erforderlich",
        7: "Wasserdruck gering",
    },
)

RegisterDefinition(
    name="appliance_status_2",
    data_type=DataType.UINT16,
    description="Gerätestatus 2",
    bit_definitions={
        0: "Pumpe",
        1: "3-Wege-Ventil offen",
        2: "3-Wege-Ventil",
        3: "3-Wege-Ventil geschlossen",
        4: "TWW aktiv",
        5: "Heizung aktiv",
        6: "Kühlung aktiv",
    },
)
```

### 3. Optional: Hilfsfunktion zum Dekodieren

```python
def decode_bitfield(register: RegisterDefinition, value: int) -> str:
    """Decode a bitfield value to a comma-separated string of active flag labels."""
    if register.bit_definitions is None:
        return ""
    active = []
    for bit in range(16):
        if value & (1 << bit):
            label = register.bit_definitions.get(bit, f"Bit{bit}")
            active.append(label)
    return ", ".join(active)
```

## Nutzung in der HA-Integration

Nach der Library-Änderung kann die Integration so darauf zugreifen:

```python
from remeha_modbus.registers import decode_bitfield

# Sensor-Wert als Klartext:
# "Frostschutz nur Pumpe" statt "2"
display_value = decode_bitfield(register, raw_value)
# Ergebnis z.B.: "Flamme, Heizung aktiv"
```

## Vorteile

- Semantik liegt in der Library, wo sie hingehört
- Alle Nutzer der Library profitieren (nicht nur die HA-Integration)
- Maschinenlesbar für beliebige Frontends
- Konsistent mit dem bestehenden `enum_values`-Pattern
