# Remeha GTW-08 Modbus Parameter

> **Note:** This document is a Markdown conversion of the original PDF
> *"Modbus GTW-08 – Liste der Parameter 7740782-01 26072019"*.
> Only the German version of the PDF is available.
> In case of discrepancies between this file and the PDF, the PDF takes precedence.

## Sehr geehrter Kunde, 

Vielen Dank für den Kauf dieses Gerätes. 

Bitte lesen Sie dieses Handbuch vor der Verwendung des Produkts sorgfältig durch und heben Sie es zum späteren Nachlesen an einem sicheren Ort auf. Um langfristig einen sicheren und effizienten Betrieb sicherzustellen, empfehlen wir die regelmäßige Wartung des Produktes. Unsere Service- und Kundendienst-Organisation kann Ihnen dabei behilflich sein. 

Wir hoffen, dass Sie viele Jahre Freude an dem Produkt haben. 

## Inhalt

1. [Vorwort](#1-vorwort)
2. [Modbus-Protokoll](#2-modbus-protokoll)
   - 2.1 Einstellungen GTW-08 Modbus-Adresse
   - 2.2 Einstellungen GTW-08 Baudrate und Parität
   - 2.3 Unterstützte Funktionscodes
   - 2.4 Modbus-Ausnahmecodes
3. [Datenmodell](#3-datenmodell)
   - 3.1 Unterstützte Datentypen (Octet String, UTF-8, B8, Int8, Int16, Int32, Uint8, Uint16, Uint32, Real32, Datum/Uhrzeit)
   - 3.2 Richtlinien für die Zuordnung von Datenobjekten und Einschränkungen
   - 3.3 Ungültige Werte
4. [Geräteinformation GTW-08](#4-geräteinformation-gtw-08)
5. [Systemermittlung](#5-systemermittlung)
6. [Überwachung der Hauptsteuerung](#6-überwachung-der-hauptsteuerung)
7. [Gerät](#7-gerät)
8. [Wartung](#8-wartung)
9. [Kreise (bis zu 12 Kreise)](#9-kreise-bis-zu-12-kreise)
10. [Kaskade](#10-kaskade)
11. [Pufferspeicher](#11-pufferspeicher)


## **1 Vorwort** 

Dieses Dokument listet die verschiedenen von GTW-08 für mit Lbus verbundenen BDR-Anwendungen unterstützten Modbus-Adressen auf. 

Der Datentyp Parameter kann „lesen und schreiben“ sein. 

Der Datentyp Maßnahmen kann nur „lesen“ sein. 

Referenzdokumente: 

## **2 Modbus-Protokoll** 

## _**2.1   Einstellungen GTW-08 Modbus-Adresse**_ 

Das Codierrad des GTW-08 wird zum Festlegen der GTW08 ModBus-Adresse verwendet. 

## _**2.2   Einstellungen GTW-08 Baudrate und Parität**_ 

Der DIP-Schalter – Wer wird zum Einrichten von Baudrate und Parität des GTW-08 Modbus verwendet 

Zur Einstellung der Baudrate werden nur die Positionen 1 und 2 verwendet 

|**SCHALTER**<br>**12**|**Modbus Baudrate**|
|---|---|
|OFF-OFF|9600 bds|
|ON-OFF|19200 bds|
|OFF-ON|38400 bds|
|ON-ON|57600 bds|


Die Positionen 3 und 4 werden zur Einstellung der Parität verwendet. 

|**SCHALTER**<br>**34**|**Modbus Parität**|
|---|---|
|OFF-OFF|Parität Keine|
|ON-OFF|Parität Ungerade|
|OFF-ON|Parität Gerade|
|ON-ON|Parität Keine|


## _**2.3   Unterstützte Funktionscodes**_ 

Es werden folgende Modbus-Funktionscodes unterstützt: 

- (03d) Read Holding Register 

- (04d) Read Input Register 

- (06d) Write Single Register 

## - (16d) Write Multiple Register 

Für read multiple (04d) und (16d) write multiple unterstützt das GTW08 das Lesen/Schreiben von 40 Registern in RAW 

## _**2.4   Modbus-Ausnahmecodes**_ 

|**Ausnahmecode**|**Name**|**Bedeutung**|
|---|---|---|
|01<br>(`01`hex)|Unzulässige Funktion|BMS fordert einen nicht unterstützten Funktionscode an.|
|02<br>(`02`hex)|Unzulässige Datenadresse|BMS fordert Wortadresse außerhalb des Bereichs des BDR-Geräts an|
|03<br>(`03`hex)|Unzulässiger Datenwert|BMS-Sollwert bei Wortadresse außerhalb des Bereichs eines BDR-Gerätes|
|04<br>(`04`hex)|Ausfall Slave-Gerät|Eine Wortadresse wird geschrieben. Dieser Vorgang ist beieinem BDR-Gerät noch nicht<br>beendet|
|10<br>(`0A`hex)|Gateway-Pfad nicht verfügbar|BDR-Gerät wurde von dem GTW-08 noch nicht oder nicht mehr erkannt|
|11<br>(`0B`hex)|Keine Antwort von Gateway-<br>Zielgerät|Die angeforderte Wortadresse wurde von dem GTW-08 noch nicht aus dem BDR-Gerät<br>gelesen|


## **3 Datenmodell** 

Alle Datenobjekte werden nach CiA301-Standard gespeichert und übertragen.  Die folgenden Datentypen werden auf dem BDR-Bus unterstützt. 

## _**3.1 Unterstützte Datentypen**_ 

## **3.1.1 Octet String** 

Binäre Zeichenkette für längere Datentypen. 

## **3.1.2 UTF-8 in Octetstring** 

Lesbarer Text für Identifikationszwecke. Aufgrund der variablen Zeichenlänge erfolgt die Längendefinition von UTF-8 Zeichenketten in Bytes. Die Länge einer Zeichenkette aus Benutzersicht kann je nach Zeichensatz variieren. 

## **3.1.3 B8** 

Boolesches Array für eine Sammlung von Flags (definiert als uint8 im Stapel) 

## **3.1.4 Int8** 

Signale mit niedriger Auflösung, Parameter, die etwas erfordern 

## **3.1.5 Int16** 

Fühlerwert normale Genauigkeit und Zähler. 

## **3.1.6 Int32** 

Hochpräzise Fühlerwerte, Parameter und Zähler. 

## **3.1.7 Uint8** 

Enumeratoren, vorzeichenlose Werte mit niedriger Genauigkeit. 

## **3.1.8 Uint16** 

Normale Genauigkeit vorzeichenlose Werte. 

## **3.1.9 Uint32** 

Hohe Genauigkeit vorzeichenlose Werte. 

## **3.1.10 Real32** 

Gleitkommazahlen, nicht bevorzugter Datentyp für den L-Bus, aber für externe Geräte unterstützt. 

## **3.1.11 Datum/Uhrzeit** 

Definition gemäß CiA301-Standard: 

_Der Datentyp TIME_OF_DAY repräsentiert die absolute Zeit. Aus der Definition und den Kodierungsregeln ergibt sich, dass TIME_OF_DAY als Bitfolge der Länge 48 dargestellt wird._ 

_Die Komponente ms ist die Zeit in Millisekunden nach Mitternacht. Die Komponente days ist die Anzahl der Tage seit dem 1. Januar 1984._ 

_STRUCT OF_ 

_UNSIGNED28 ms,_ 

_VOID4 reserved,_ 

_UNSIGNED16 days_ 

_TIME_OF_DAY_ 

## _**3.2 Richtlinien für die Zuordnung von Datenobjekten und Einschränkungen**_ 

## **3.2.1 Lufttemperaturen** 

Alle Raum- und Lufttemperaturen, **mit Ausnahme der Außentemperaturen,** müssen eine Verstärkung von 0,1 und eine Auflösung von 16 Bit aufweisen. 

## **3.2.2 Außentemperaturen** 

Alle Außentemperaturmessungen und zugehörigen Parameter müssen eine Verstärkung von 0,01 und eine Auflösung von 16 Bit aufweisen. 

## **3.2.1 Wassertemperaturen** 

Alle Wassertemperaturen müssen eine Verstärkung von 0,01 und eine Auflösung von 16 Bit aufweisen. 

## **3.2.2 Enumeratoren** 

Enumeratoren müssen in jedem Fall 8-Bit-Werte sein 

## **3.2.3 Wasserdruck** 

Wasserdruck immer eine Verstärkung von 0,1 bar 

## **3.2.4 Wasserflussmessungen** 

Alle Durchflussgeschwindigkeiten in Liter/Minute. Verstärkung 0,01 

## **3.2.5 Absolute Leistung** 

Alle Datenobjekte der absoluten Leistung sind in kW mit einer Auflösung von 0,1 zu definieren und müssen vom Typ unsigned integer 16 bit sein. 

## **3.2.6 Relative Leistung** 

Alle Datenobjekte, die sich auf die relative Leistung beziehen, sind mit einer Auflösung von 0,1% zu messen. 

## _**3.3 Ungültige Werte**_ 

Bei jeder Initialisierung der Fühlermessung wird ein ungültiger Wert hinzugefügt. 

Wenn ein Signal außerhalb der Grenzen liegt, wird dieser Wert für die Messung zurückgegeben. 

Wenn der physikalische Fühler mit mehreren Signalen verbunden ist, geben die nicht verbundenen Signale einen ungültigen Wert zurück. 

Für die folgenden Typen wird der Wert für ungültig verwendet: 

| Datentyp | Ungültiger Wert | Hex |
|---|---|---|
| Unsigned Integer8 | 255 | 0xFF |
| Unsigned Integer16 | 65535 | 0xFFFF |
| Unsigned Integer32 | 4294967295 | 0xFFFFFFFF |
| Signed Integer8 | -128 | 0x80 |
| Signed Integer16 | -32768 | 0x8000 |
| Signed Integer32 | -2147483648 | 0x80000000 |

## **4 Geräteinformation GTW-08** 

|**Modbus**|**Daten**|**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**1**|parApDeviceInfoManufacturerCode Byte 0|parApDeviceInfoManufacturerCode Byte 1|Herstellercode (= USt-Code) des Gerätes|Read|VISIBLE_STRING|2001.1|
|**2**|parApDeviceInfoManufacturerCode Byte 2|parApDeviceInfoManufacturerCode Byte 3||Read|||
|**3**|parApDeviceInfoManufacturerCode Byte 4|parApDeviceInfoManufacturerCode Byte 5||Read|||
|**4**|parApDeviceInfoManufacturerCode Byte 6|parApDeviceInfoManufacturerCode Byte 7||Read|||
|**5**|parApDeviceInfoManufacturerCode Byte 8|parApDeviceInfoManufacturerCode Byte 9||Read|||
|**6**|parApDeviceInfoManufacturerCode Byte 10|parApDeviceInfoManufacturerCode Byte 11||Read|||
|**7**|parApDeviceInfoManufacturerCode Byte 12|parApDeviceInfoManufacturerCode Byte 13||Read|||
|**8**|parApDeviceInfoManufacturerCode Byte 14|parApDeviceInfoManufacturerCode Byte 15||Read|||
|**9**|parApDeviceInfoManufacturerCode Byte 16|parApDeviceInfoManufacturerCode Byte 17||Read|||
|**10**|parApDeviceInfoManufacturerCode Byte 18|parApDeviceInfoManufacturerCode Byte 19||Read|||
|**11**|DeviceType 16-9|DeviceType 8-1|Gerätetyp GTW-08|Read|UNSIGNED16|2001.2|


## **5 Systemermittlung** 

|**Modbus**|**Daten**|**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**128**|-|numberOfDevices|Anzahl der auf dem Gerät vorhandenen elektronischen Platinen|Read|UNSIGNED8|Internal<br>Variables|
|**129**|DeviceTypeBoard1 16-9|DeviceTypeBoard1 8-1|Gerätetyp an Instanz 1(CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**130**|SoftwareVersion1 16-9|SoftwareVersion1 8-1|Softwareversion des Geräts an Instanz 1(CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**131**|DeviceConfigurationTabl<br>eVersion1 16-9|DeviceConfigurationTableV<br>ersion1 8-1|Konfigurationstabelle der Version des Geräts an Instanz 1(CU-EHC, EEC, SCB,<br>...)|Read|UNSIGNED16|2001.13|
|**132**|HardwareVersion1 16-9|HardwareVersion1 8-1|Hardwareversion des Geräts an Instanz 1(CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**133**|ArticleNumber1 32-25|ArticleNumber1 24-17|Artikelnummer des Geräts an Instanz 1(CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**134**|ArticleNumber1 16-9|ArticleNumber1 8-1|||||
|**135**|DeviceTypeBoard2 16-9|DeviceTypeBoard2 8-1|Gerätetyp an Instanz 2 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**136**|SoftwareVersion2 16-9|SoftwareVersion2 8-1|Softwareversion des Geräts an Instanz 2 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**137**|DeviceConfigurationTabl<br>eVersion2 16-9|DeviceConfigurationTableV<br>ersion2 8-1|Konfigurationstabelle der Version des Geräts an Instanz 2 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**138**|HardwareVersion2 16-9|HardwareVersion2 8-1|Hardwareversion des Geräts an Instanz 2 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**139**|ArticleNumber2 32-25|ArticleNumber2 24-17|Artikelnummer des Geräts an Instanz 2 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**140**|ArticleNumber2 16-9|ArticleNumber2 8-1|||||
|**141**|DeviceTypeBoard3 16-9|DeviceTypeBoard3 8-1|Gerätetyp an Instanz 3 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**142**|SoftwareVersion3 16-9|SoftwareVersion3 8-1|Softwareversion des Geräts an Instanz 3 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**143**|DeviceConfigurationTabl<br>eVersion3 16-9|DeviceConfigurationTableV<br>ersion3 8-1|Konfigurationstabelle der Version des Geräts an Instanz 3 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**144**|HardwareVersion3 16-9|HardwareVersion3 8-1|Hardwareversion des Geräts an Instanz 3 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**145**|ArticleNumber3 32-25|ArticleNumber3 24-17|Artikelnummer des Geräts an Instanz 3 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**146**|ArticleNumber3 16-9|ArticleNumber3 8-1|||||
|**147**|DeviceTypeBoard4 16-9|DeviceTypeBoard4 8-1|Gerätetyp an Instanz 4 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**148**|SoftwareVersion4 16-9|SoftwareVersion4 8-1|Softwareversion des Geräts an Instanz 4 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**149**|DeviceConfigurationTabl<br>eVersion4 16-9|DeviceConfigurationTableV<br>ersion4 8-1|Konfigurationstabelle der Version des Geräts an Instanz 4 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**150**|HardwareVersion4 16-9|HardwareVersion4 8-1|Hardwareversion des Geräts an Instanz 4 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**151**|ArticleNumber4 32-25|ArticleNumber4 24-17|Artikelnummer des Geräts an Instanz 4 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**152**|ArticleNumber4 16-9|ArticleNumber4 8-1|||||
|**153**|DeviceTypeBoard5 16-9|DeviceTypeBoard5 8-1|Gerätetyp an Instanz 5 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**154**|SoftwareVersion5 16-9|SoftwareVersion5 8-1|Softwareversion des Geräts an Instanz 5 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**155**|DeviceConfigurationTabl<br>eVersion5 16-9|DeviceConfigurationTableV<br>ersion5 8-1|Konfigurationstabelle der Version des Geräts an Instanz 5 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**156**|HardwareVersion5 16-9|HardwareVersion5 8-1|Hardwareversion des Geräts an Instanz 5 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**157**|ArticleNumber5 32-25|ArticleNumber5 24-17|Artikelnummer des Geräts an Instanz 5 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**158**|ArticleNumber5 16-9|ArticleNumber5 8-1|||||
|**159**|DeviceTypeBoard6 16-9|DeviceTypeBoard6 8-1|Gerätetyp an Instanz 6 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**160**|SoftwareVersion6 16-9|SoftwareVersion6 8-1|Softwareversion des Geräts an Instanz 6 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**161**|DeviceConfigurationTabl<br>eVersion6 16-9|DeviceConfigurationTableV<br>ersion6 8-1|Konfigurationstabelle der Version des Geräts an Instanz 6 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**162**|HardwareVersion6 16-9|HardwareVersion6 8-1|Hardwareversion des Geräts an Instanz 6 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**163**|ArticleNumber6 32-25|ArticleNumber6 24-17|Artikelnummer des Geräts an Instanz 6 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**164**|ArticleNumber6 16-9|ArticleNumber6 8-1|||||
|**165**|DeviceTypeBoard7 16-9|DeviceTypeBoard7 8-1|Gerätetyp an Instanz 7 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**166**|SoftwareVersion7 16-9|SoftwareVersion7 8-1|Softwareversion des Geräts an Instanz 7 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**167**|DeviceConfigurationTabl<br>eVersion7 16-9|DeviceConfigurationTableV<br>ersion7 8-1|Konfigurationstabelle der Version des Geräts an Instanz 7 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**168**|HardwareVersion7 16-9|HardwareVersion7 8-1|Hardwareversion des Geräts an Instanz 7 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**169**|ArticleNumber7 32-25|ArticleNumber7 24-17|Artikelnummer des Geräts an Instanz 7 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**170**|ArticleNumber7 16-9|ArticleNumber7 8-1|||||
|**171**|DeviceTypeBoard8 16-9|DeviceTypeBoard8 8-1|Gerätetyp an Instanz 8 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**172**|SoftwareVersion8 16-9|SoftwareVersion8 8-1|Softwareversion des Geräts an Instanz 8 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**173**|DeviceConfigurationTabl<br>eVersion8 16-9|DeviceConfigurationTableV<br>ersion8 8-1|Konfigurationstabelle der Version des Geräts an Instanz 8 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**174**|HardwareVersion8 16-9|HardwareVersion8 8-1|Hardwareversion des Geräts an Instanz 8 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**175**|ArticleNumber8 32-25|ArticleNumber8 24-17|Artikelnummer des Geräts an Instanz 8 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**176**|ArticleNumber8 16-9|ArticleNumber8 8-1|||||
|**177**|DeviceTypeBoard9 16-9|DeviceTypeBoard9 8-1|Gerätetyp an Instanz 9 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**178**|SoftwareVersion9 16-9|SoftwareVersion9 8-1|Softwareversion des Geräts an Instanz 9 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**179**|DeviceConfigurationTabl<br>eVersion9 16-9|DeviceConfigurationTableV<br>ersion9 8-1|Konfigurationstabelle der Version des Geräts an Instanz 9 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**180**|HardwareVersion9 16-9|HardwareVersion9 8-1|Hardwareversion des Geräts an Instanz 9 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**181**|ArticleNumber9 32-25|ArticleNumber9 24-17|Artikelnummer des Geräts an Instanz 9 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**182**|ArticleNumber9 16-9|ArticleNumber9 8-1|||||
|---|---|---|---|---|---|---|
|**183**|DeviceTypeBoard10 16-9|DeviceTypeBoard10 8-1|Gerätetyp an Instanz 10 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**184**|SoftwareVersion10 16-9|SoftwareVersion10 8-1|Softwareversion des Geräts an Instanz 10 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**185**|DeviceConfigurationTabl<br>eVersion10 16-9|DeviceConfigurationTableV<br>ersion10 8-1|Konfigurationstabelle der Version des Geräts an Instanz 10 (CU-EHC, EEC,<br>SCB,...)|Read|UNSIGNED16|2001.13|
|**186**|HardwareVersion10 16-9|HardwareVersion10 8-1|Hardwareversion des Geräts an Instanz 10 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|Internal<br>Variables|
|**187**|ArticleNumber10 32-25|ArticleNumber10 24-17|Artikelnummer des Geräts an Instanz 10 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED32|2001.12|
|**188**|ArticleNumber10 16-9|ArticleNumber10 8-1|||||
|**189**||NumberOfZones|Anzahl der auf dem Gerät vorhandenen Kreise|Read|UNSIGNED8|Internal<br>Variables|
|**190**||NumberOfZonesDisabled|Anzahl der auf dem Gerät deaktivierten Kreise|Read|UNSIGNED8||
|**191**||NumberOfZonesCH|Anzahl der auf dem Gerät vorhandenen Heizkreise|Read|UNSIGNED8||
|**192**||NumberOfZonesCHCooling|Anzahl der auf dem Gerät vorhandenen Heiz-/Kühlkreise|Read|UNSIGNED8||
|**193**||NumberOfZonesDHW|Anzahl der auf dem Gerät vorhandenen TWW-Kreise|Read|UNSIGNED8||
|**194**||NumberOfZonesProcessHe<br>at|Anzahl der auf dem Gerät vorhandenen Prozesswärme-Kreise|Read|UNSIGNED8||
|**195**||NumberOfZonesSwimming<br>Pool|Anzahl der auf dem Gerät vorhandenen Schwimmbad-Kreise|Read|UNSIGNED8||
|**196**||NumberOfZonesOthers|Anzahl der auf dem Gerät vorhandenen sonstigen Kreise (Zeitprogramm)|Read|UNSIGNED8||
|**197**||BufferTankActive|Puffertank ist am Gerät aktiv|Read|UNSIGNED8||
|**198**||CascadeActive|das Gerät ist Teil einer Kaskade<br>0: nein<br>1: Kaskadenmaster<br>2: Kaskadenslave|Read|ENUM8||
|**199**|||Für zukünftige Verwendung reserviert||||
|**200**||Reset discovery table|Ermittlungstabelle zurücksetzen. Auf 0x5A einstellen, um den Befehl<br>auszuführen. Zurücksetzen auf 0 durch das GTW-08|Read/<br>Write|UNSIGNED8|Internal<br>Variables|


## **6 Überwachung der Hauptsteuerung** 

|**Modbus**||**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.**<br>**SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**256**|-|PowerSetpoint|An das CU-Gerät zu sendender Leistungssollwert für<br>Heizanforderung|Read/<br>Write|UNSIGNED8|PDO mapping|
|**257**|TemperatureSetpoint 16-9|TemperatureSetpoint 8-1|An das CU-Gerät zu sendender Temperatursollwert für<br>Heizanforderung|Read/<br>Write|INTEGER16|PDO mapping|
|**258**|-|AlgoritthmType|Art der Regelung (0: beide; 1: Leistung; 2: Temperatur, 3: keine)|Read/<br>Write|ENUM8|PDO mapping|
|**259**|-|HeatDemandtype|Art der Heizanforderung (0: keine; 7: Heizung; 8: Kühlung)|Read/<br>Write|ENUM8|PDO mapping|
|**260-271**|-|-|Für zukünftige Verwendung reserviert|Read|-||
|**272**||PowerActualReceivedsss|Ist-Leistung (Zusammenfassung sämtlicher Ist-Leistung, die von<br>den verbundenen Kesseln empfangen wird)|Read|UNSIGNED8|PDO mapping|
|**273**|FlowTemperatureReceived<br>16-9|FlowTemperatureReceived 8-1|Vorlauftemperatur des Geräts|Read|INTEGER16|PDO mapping|
|**274**|ReturnTemperatureReceiv<br>ed 16-9|ReturnTemperatureReceived 8-1|Rücklauftemperatur des Geräts|Read|INTEGER16|PDO mapping|
|**275**|-|ProducerManagerStatusBitfieldRecei<br>ved|0 Pumpe aktiv|Read|UNSIGNED8|PDO mapping|
||||1 Leistungsmotor aktiv (Brenner, Verdichter oder<br>Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung vorhanden||||
|**276**|-|ProducerManagerRequestReceived|0 Frostschutz|Read|UNSIGNED8|PDO mapping|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**277**|Appliance Error 16-9|Appliance Error 8-1|Aktueller Fehler Gerät (0xFFFFFF bedeutet kein Fehler)|Read|UNSIGNED16|PDO mapping|
|**278**|||Priorität Gerätefehler|Read|ENUM8|PDO mapping|
||||0: Verriegelung||||
||-|Appliance Error Priority|3: Sperrung||||
||||6: Warnung||||
||||255: Kein Fehler||||
|**279**|-|Appliance status 1|b0: varFlammeEin|Read|UNSIGNED16|PDO mapping|
||||b1: varWärmepumpeEin||||
||||b2: varElektrZusatzerzEin||||
||||b3: varElektrZusatzerz2Ein||||
||||b4: varTWWElektrZusatzerzEin||||
||||b5: varWartungGerätErforderlich||||
||||b6: varLeistungGerätNiedrigResetErforderlich||||
||||b7: varWasserdruckGerätGering||||
|**280**|||b0: varPumpeGerät|Read|UNSIGNED16|PDO mapping|
||||b1: var3WegeVentilOffen||||
||||b2: var3WegeVentil||||
||-|Appliance status 2|b3: var3WegeVentilGeschlossen||||
||||b4: VarGerätTWWAktiv||||
||||b5: VarGerätHzgAktiv||||
||||b6: varGerätKühlenAktiv||||
|**281-287**|-|-|Für zukünftige Verwendung reserviert|Read|-|-|
|**288**|varChCtrBurnerStarts 32-<br>25|varChCtrBurnerStarts 24-17|Zähler Brennerstarts|Read|UNSIGNED32|530B.0|
|**289**|varChCtrBurnerStarts 16-9|varChCtrBurnerStarts 8-1|Zähler Brennerstarts|Read|UNSIGNED32||
|**290**|varChCtrBurnHours 32-25|varChCtrBurnHours 24-17|Zähler Brennerstunden|Read|UNSIGNED32|530C.0|
|**291**|varChCtrBurnHours 16-9|varChCtrBurnHours  8-1|Zähler Brennerstunden|Read|UNSIGNED32||
|**292**|varApCtrServiceBurningHo<br>urs 16-9|varApCtrServiceBurningHours 8-1|Anzahl der Stunden, in denen das Gerät nach der Wartung in<br>Betrieb war|Read|UNSIGNED16|5040.0|
|**293**|varApCtrServiceBurnerStar<br>ts 32-25|varApCtrServiceBurnerStarts 24-17|Anzahl erfolgreicher Verdichterstarts nach der Wartung|Read|UNSIGNED32|5042.0|
|**294**|varApCtrServiceBurnerStar<br>ts 16-9|varApCtrServiceBurnerStarts 8-1|Anzahl erfolgreicher Verdichterstarts nach der Wartung|Read|UNSIGNED32||
|**295**|varApCtrBackup1Starts 32-<br>25|varApCtrBackup1Starts 24-17|Zähler Starts Zusatzerzeuger 1|Read|UNSIGNED32|50B1.0|
|**296**|varApCtrBackup1Starts 16-<br>9|varApCtrBackup1Starts 8-1|Zähler Starts Zusatzerzeuger 1|Read|UNSIGNED32||
|**297**|varApCtrBackup1Hours 32-<br>25|varApCtrBackup1Hours 24-17|Zähler Stunden Zusatzerzeuger 1|Read|UNSIGNED32|50AF.0|
|**298**|varApCtrBackup1Hours 16-<br>9|varApCtrBackup1Hours 8-1|Zähler Stunden Zusatzerzeuger 1|Read|UNSIGNED32||
|**299**|varApCtrBackup2Starts 32-<br>25|varApCtrBackup2Starts 24-17|Zähler Starts Zusatzerzeuger 2|Read|UNSIGNED32|50B2.0|
|**300**|varApCtrBackup2Starts 16-<br>9|varApCtrBackup2Starts 8-1|Zähler Starts Zusatzerzeuger 2|Read|UNSIGNED32||
|**301**|varApCtrBackup2Hours 32-<br>25|varApCtrBackup2Hours 24-17|Zähler Stunden Zusatzerzeuger 2|Read|UNSIGNED32|50B0.0|
|**302**|varApCtrBackup2Hours 16-<br>9|varApCtrBackup2Hours 8-1|Zähler Stunden Zusatzerzeuger 2|Read|UNSIGNED32||
|**303**|varApCtrHoursTotal16-9|varApCtrHoursTotal 8-1|Betriebsstundenzahl|Read|UNSIGNED32|5000.0|
|**304**|varApCtrHoursTotal16-9|varApCtrHoursTotal 8-1|Betriebsstundenzahl|Read|UNSIGNED32||
|**305-349**|-|-|Für zukünftige Verwendung reserviert|Read|-|-|
|**350**|parApTimeOfDay Byte 0|parApTimeOfDay Byte 1|Uhrzeit Ende Modusänderung ZeitStempel CIA|Read/<br>Write|OCTET_STRING|3023.0|
|**351**|parApTimeOfDay Byte 2|parApTimeOfDay Byte 3|||||
|**352**|parApTimeOfDay Byte 4|parApTimeOfDay Byte 5|||||


## **7 Gerät** 

|**Modbu**<br>**s**|**Daten**|**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**384**|varApTOutside 16-9|varApTOutside 8-1|Außentemperaturmessung|Read|INTEGER16|501E.0|
|**385**||varApSeasonMode|Jahreszeitbedingter Modus aktiv<br>0: Winter<br>1: Winter Frostschutz<br>2: Sommer Neutralbereich<br>3: Sommer|Read|ENUM8|50A7.0|
|**386**|parApSummerWinter 16 -9|parApSummerWinter 8 -1|Außentemperatur: Obergrenze für Heizung (30,5<br>bedeutet deaktiviert)|Read/<br>Write|UNSIGNED16|303A.0|
|**387**|parApNeutralBandSummerWinter<br>16 -9|parApNeutralBandSummerWinter 8 -1|Nur verwendet, wenn der Generator die Kühlung<br>verwenden konnte. Neutralbereich, in dem die HP<br>deaktiviert ist|Read/<br>Write|UNSIGNED16|303C.0|
|**388**|parApFrostMinToutside 16 -9|parApFrostMinToutside 8 -1|Außentemperatur unter der die Frostschutzfunktion<br>aktiviert wird|Read/<br>Write|INTEGER16|3041.0|
|**389**||parApForceSummerMode|Die Heizung wird gestoppt. Warmwasser wird<br>aufrechterhalten. Sommermodus erzwingen<br>0: Off<br>1: On|Read/Writ<br>e|ENUM8|303B.0|
|**390-399**|||Für Zukunft reserviert||||
|**400**|varApTflow 16 -9|varApTflow 8 -1|Vorlauftemperatur|Read|INTEGER16|5013.0|
|**401**|varApTreturn 16 -9|varApTreturn 8 -1|Rücklauftemperatur|Read|INTEGER16|5015.0|
|**402**|varApFlueGasTemperature 16 -9|varApFlueGasTemperature 8 -1|Abgastemperatur|Read|INTEGER16|5027.0|
|**403**|varHpHeatPumpTF 16 -9|varHpHeatPumpTF 8 -1|Vorlauftemperatur Wärmepumpe|Read|INTEGER16|4301.0|
|**404**|varHpHeatPumpTR 16 -9|varHpHeatPumpTR 8 -1|Rücklauftemperatur Wärmepumpe|Read|INTEGER16|4302.0|
|**405**|varApInternalSetpoint 16 -9|varApInternalSetpoint 8 -1|Interner Sollwert für die Trinkwarmwasserbereitung|Read|UNSIGNED16|50A9.0|
|**406**|varChSetpoint 16 -9|varChSetpoint 8 -1|Heizungssollwert der Anlage|Read|UNSIGNED16|5302.0|
|**407**|varHpCoolingSetpoint 16 -9|varHpCoolingSetpoint 8 -1|Vorlauftemperatur-Sollwert im Kühlmodus|Read|UNSIGNED16|4321.0|
|**408**|varDhwFlowTempSetpoint 16 -9|varDhwFlowTempSetpoint 8 -1|Vorlauftemperatur-Sollwert<br>Trinkwarmwasserbereitung|Read|UNSIGNED16|5604.0|
|**409**||varApWaterPressure|Aktueller Wasserdruck|Read|UNSIGNED8|5016.0|
|**410**|varApFlowmeter 16 -9|varApFlowmeter 8 -1|Durchfluss|Read|UNSIGNED16|5083.0|
|**411**||varApStatus|Gerätestatus|Read|ENUM8|500F.0|
|**412**||varApSubStatus|Geräte-Substatus|Read|ENUM8|5011.0|
|**413**|varApPowerActual 16 -9|varApPowerActual 8 -1|Tatsächlich erzeugte relative Leistung|Read|UNSIGNED16|501B.0|
|**414**|varHePowerSetpoint 16 -9|varHePowerSetpoint 8 -1|Leistungssollwert in % von Max.|Read|UNSIGNED16|4215.0|
|**415**||varHeIonisationCurrent|Tatsächlich gemessener Flammenstrom|Read|UNSIGNED8|4212.0|
|**416**||varProducerInternalHeatDemand Byte<br>1|Interne Heizanforderung - Leistung|Read|UNSIGNED8|5711.1|
|**417**|varProducerInternalHeatDemand<br>Byte 3|varProducerInternalHeatDemand Byte<br>2|Interner Heizanforderung - Temperatursollwert|Read|INTEGER16||
|**418**||varProducerInternalHeatDemand Byte<br>4|Interne Heizanforderung - HeizanforderungArt|Read|UNSIGNED8||
|**419**|varChCtrBurnerStarts 32-25|varChCtrBurnerStarts 24-17|Zähler Brennerstarts|Read|UNSIGNED32|530B.0|
|**420**|varChCtrBurnerStarts 16-9|varChCtrBurnerStarts 8-1|Zähler Brennerstarts|Read|UNSIGNED32||
|**421**|varChCtrBurnHours 32-25|varChCtrBurnHours 24-17|Zähler Brennerstunden|Read|UNSIGNED32|530C.0|
|**422**|varChCtrBurnHours 16-9|varChCtrBurnHours  8-1|Zähler Brennerstunden|Read|UNSIGNED32||
|**423**|varApCtrBackup1Starts 32-25|varApCtrBackup1Starts 24-17|Zähler Starts Zusatzerzeuger 1|Read|UNSIGNED32|50B1.0|
|**424**|varApCtrBackup1Starts 16-9|varApCtrBackup1Starts 8-1|Zähler Starts Zusatzerzeuger 1|Read|UNSIGNED32||
|**425**|varApCtrBackup1Hours 32-25|varApCtrBackup1Hours 24-17|Zähler Stunden Zusatzerzeuger 1|Read|UNSIGNED32|50AF.0|
|**426**|varApCtrBackup1Hours 16-9|varApCtrBackup1Hours 8-1|Zähler Stunden Zusatzerzeuger 1|Read|UNSIGNED32||
|**427**|varApCtrBackup2Starts 32-25|varApCtrBackup2Starts 24-17|Zähler Starts Zusatzerzeuger 2|Read|UNSIGNED32|50B2.0|
|**428**|varApCtrBackup2Starts 16-9|varApCtrBackup2Starts 8-1|Zähler Starts Zusatzerzeuger 2|Read|UNSIGNED32||
|**429**|varApCtrBackup2Hours 32-25|varApCtrBackup2Hours 24-17|Zähler Stunden Zusatzerzeuger 2|Read|UNSIGNED32|50B0.0|
|**430**|varApCtrBackup2Hours 16-9|varApCtrBackup2Hours 8-1|Zähler Stunden Zusatzerzeuger 2|Read|UNSIGNED32||
|**431**|varApCtrHoursTotal16-9|varApCtrHoursTotal 8-1|Betriebsstundenzahl|Read|UNSIGNED32|5000.0|
|**432**|varApCtrHoursTotal16-9|varApCtrHoursTotal 8-1|Betriebsstundenzahl|Read|UNSIGNED32||
|**433**|varApChEnergyConsumption 32-25|varApChEnergyConsumption 24-17|NGesamtenergieverbrauch für Heizung|Read|UNSIGNED32|5044.0|
|**434**|varApChEnergyConsumption 16-9|varApChEnergyConsumption 8-1|Gesamtenergieverbrauch für Heizung|Read|UNSIGNED32||
|**435**|varApDhwEnergyConsumption 32-<br>25|varApDhwEnergyConsumption 24-17|Gesamtenergieverbrauch für die<br>Trinkwasserbereitung.|Read|UNSIGNED32|5045.0|
|**436**|varApDhwEnergyConsumption 16-<br>9|varApDhwEnergyConsumption 8-1|Gesamtenergieverbrauch für die<br>Trinkwasserbereitung.|Read|UNSIGNED32||
|**437**|varApCoolingEnergyConsumption<br>32-25|varApCoolingEnergyConsumption 24-17|Gesamtenergieverbrauch für die Kühlung|Read|UNSIGNED32|5046.0|
|**438**|varApCoolingEnergyConsumption<br>16-9|varApCoolingEnergyConsumption 8-1|Gesamtenergieverbrauch für die Kühlung|Read|UNSIGNED32||
|**439-499**|reserviert für die Zukunft||||||
|**500**||parApChEnabled|Erlaubt die Heizung<br>0: Off<br>1: On|Read/Writ<br>e|ENUM8|3012.0|
|**501**||parApDhwEnabled|Erlaubt die Warmwasserbereitung<br>0: Off<br>1: On|Read/Writ<br>e|ENUM8|3013.0|
|**502**||parApCoolingEnabled|Legt die Art der Kühlung fest, die entweder für die<br>aktive oder die freie Kühlung verwendet wird:<br>0 :  OFF<br>1: Active cooling on<br>2: Free coolingon|Read/Writ<br>e|ENUM8|301E.0|
|**503**||parApCoolingForced|Schaltet manuell die Wärmepumpe in den<br>Kühlmodus<br>0: No<br>1: Yes|Read/Writ<br>e|ENUM8|3011.0|


## **8 Wartung** 

|**Modbus**||**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**512**||varApServiceRequired|Wartung erforderlich<br>0: NEIN<br>1: JA|Read|ENUM8|500E.0|
|**513**||varApCurrentOrUpcomingServiceNotifi<br>cation|Aktuelle oder bevorstehende Wartungsmeldung 1=A, 2=B,<br>3=C, 4=benutzerdefiniert.|Read|ENUM8|5048.0|
|**514**|varApCtrServiceBurningHours<br>16-9|varApCtrServiceBurningHours 8-1|Anzahl der Stunden, in denen das Gerät nach der Wartung<br>in Betrieb war|Read|UNSIGNED16|5040.0|
|**515**|varApCtrServiceOperatingHou<br>rs 16-9|varApCtrServiceOperatingHours 8-1|Anzahl der Stunden seit der letzten Wartung des Gerätes|Read|UNSIGNED16|5041.0|
|**516**|varApCtrServiceBurnerStarts<br>32-25|varApCtrServiceBurnerStarts 24-17|Anzahl erfolgreicher Verdichterstarts nach der Wartung|Read|UNSIGNED32|5042.0|
|**517**|varApCtrServiceBurnerStarts<br>16-9|varApCtrServiceBurnerStarts 8-1|Anzahl erfolgreicher Verdichterstarts nach der Wartung|Read|UNSIGNED32||
|**518-530**|||reserved for futur||||
|**531**||varApplianceOnError|Fehler am Gerät vorhanden|Read|ENUM8|Internal<br>Variable|
|**532**|varACurrentError1 16-9|varACurrentError1 8-1|Code Fehler des Geräts an Instanz 1(CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**533**||ErroPriority1|Fehlerstufe des Fehlers am Gerät an Instanz 1<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**534**|varACurrentError3 16-9|varACurrentError2 8-1|Code Fehler des Geräts an Instanz 2 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**535**||ErroPriority2|Fehlerstufe des Fehlers am Gerät an Instanz 2<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**536**|varACurrentError3 16-9|varACurrentError3 8-1|Code Fehler des Geräts an Instanz 3 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**537**||ErroPriority3|Fehlerstufe des Fehlers am Gerät an Instanz 3<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**538**|varACurrentError4 16-9|varACurrentError4 8-1|Code Fehler des Geräts an Instanz 4 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**539**||ErroPriority4|Fehlerstufe des Fehlers am Gerät an Instanz 4<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**540**|varACurrentError5 16-9|varACurrentError5 8-1|Code Fehler des Geräts an Instanz 5 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**541**||ErroPriority5|Fehlerstufe des Fehlers am Gerät an Instanz 5<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**542**|varACurrentError6 16-9|varACurrentError6 8-1|Code Fehler des Geräts an Instanz 6 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**543**||ErroPriority6|Fehlerstufe des Fehlers am Gerät an Instanz 6<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**544**|varACurrentError7 16-9|varACurrentError7 8-1|Code Fehler des Geräts an Instanz 7 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**545**||ErroPriority7|Fehlerstufe des Fehlers am Gerät an Instanz 7<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**546**|varACurrentError8 16-9|varACurrentError8 8-1|Code Fehler des Geräts an Instanz 8 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**547**||ErroPriority8|Fehlerstufe des Fehlers am Gerät an Instanz 8<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**548**|varACurrentError9 16-9|varACurrentError9 8-1|Code Fehler des Geräts an Instanz 9 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**549**||ErroPriority9|Fehlerstufe des Fehlers am Gerät an Instanz 9<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|
|**550**|varACurrentError10 16-9|varACurrentError10 8-1|Code Fehler des Geräts an Instanz 10 (CU-EHC, EEC, SCB, ...)|Read|UNSIGNED16|1003.1|
|**551**||ErroPriority10|Fehlerstufe des Fehlers am Gerät an Instanz 10<br>0: Verriegelung<br>3: Sperrung<br>6: Warnung|Read|ENUM8|2004.1|


## **9 Kreise (bis zu 12 Kreise)** 

Das GTW-08 unterstützt 12 Kreise, alle Kreise haben die gleiche Zuordnung. Für jeden Kreis sind 512 modbus register reserviert. 

|Zone|Modbus Adress|
|---|---|
|Zone 1|640 -> 1151|
|Zone 2|1152 -> 1663|
|Zone 3|1664 -> 2175|
|Zone 4|2176 -> 2687|
|Zone 5|2688 -> 3199|
|Zone 6|3200 -> 3711|
|Zone 7|3712 -> 4223|
|Zone 8|4224 -> 4735|
|Zone 9|4736 -> 5247|
|Zone 10|5248 -> 5759|
|Zone 11|5760 -> 6271|
|Zone 12|6272 -> 6783|
|**Modbus**|**Daten**||**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.**<br>**SubIndex**<br>**HZG/TWW**<br>**Sekundärkreise**|**Datenpunkte**<br>**index.**<br>**SubIndex**<br>**TWW Primär**|
|**Adresse**|MSB|LSB||||||
|**640**||varZoneTypesss|Art des angeforderten<br>Kreises<br>0: nicht vorhanden<br>1: nur HZG<br>2: HZG + KÜHLUNG<br>3: TWW<br>4: Prozesswärme<br>5: Schwimmbad<br>254: Sonstige (z.B.<br>Zeitprogramm)|Read|ENUM8|InternalVariable|InternalVariable|
|**641**||parZoneFunction|Funktion des Kreises<br>0: deaktiviert<br>1: ungemischt<br>2: Mischerkreis<br>3: Schwimmbad<br>4: Hochtemperatur<br>5: Gebläsekonvektor<br>6: TWW-Speicher<br>7: Elektr. TWW-Speicher<br>8: Zeitprogramm<br>9: Prozesswärme<br>10: TWW Schichten<br>11: TWW BIC<br>12: Gewerbl. WW-<br>Speicher<br>254: TWW primär|Read|ENUM8|InternalVariable|InternalVariable|
|**642**|parZoneFriendlyNameShort Byte 0|parZoneFriendlyNameShort Byte 1|Kreisbezeichnung kurz|Read|VISIBLE_STRING|InternalVariable|"DHW"|
|**643**|parZoneFriendlyNameShort Byte 2|parZoneFriendlyNameShort Byte 3||||||
|**644**|parZoneFriendlyNameShort Byte 4|Rotary Switch||||||
|**645**|DeviceType 16-9|DeviceType 8-1|Gerätetyp der Platine, auf<br>der sich der Kreis<br>befindet|Read|UNSIGNED16|InternalVariable|InternalVariable|
|**646**||instance|Geräteinstanz, zu der der<br>Kreisgehört|Read|UNSIGNED8|InternalVariable|InternalVariable|
|**647**||||||||
|**648**|parZoneTFlowSetpoint 16-9|parZoneTFlowSetpoint 8-1|Temperatursollwert für<br>Kreis, wenn Außenfühler<br>fehlt|Read/Write|UNSIGNED16|3402.n|Not Available|
|**649**||parZoneMode|Modus arbeitende Zone<br>0: Zeitprogramm 1:<br>Manuell 2: Frostschutz|Read/Write|ENUM8|341F.n|3661.n|
|**650**|parZoneRoomUserActivitySetpoint1 16-9|parZoneRoomUserActivitySetpoint1 8-1|Temperatursollwert der<br>Benutzeraktivitätje Kreis|Read/Write|UNSIGNED16|340C.n|Not Available|
|**651**|parZoneRoomUserActivitySetpoint2 16-9|parZoneRoomUserActivitySetpoint2 8-1|Temperatursollwert der<br>Benutzeraktivitätje Kreis|Read/Write|UNSIGNED16|340C.n|Not Available|
|**652**|parZoneRoomUserActivitySetpoint3 16-9|parZoneRoomUserActivitySetpoint3 8-1|Temperatursollwert der<br>Benutzeraktivitätje Kreis|Read/Write|UNSIGNED16|340C.n|Not Available|
|**653**|parZoneRoomUserActivitySetpoint4 16-9|parZoneRoomUserActivitySetpoint4 8-1|Temperatursollwert der<br>Benutzeraktivitätje Kreis|Read/Write|UNSIGNED16|340C.n|Not Available|
|**654**|parZoneRoomUserActivitySetpoint5 16-9|parZoneRoomUserActivitySetpoint5 8-1|Temperatursollwert der<br>Benutzeraktivitätje Kreis|Read/Write|UNSIGNED16|340C.n|Not Available|
|**655**|parZoneAmbiantNightSetpoint 16-9|parZoneAmbiantNightSetpoint 8-1|Raumsollwert zur<br>Umschaltung von<br>Komfort auf Reduziert im<br>Heizbetrieb|Read/Write|UNSIGNED16|340B.n|Not Available|
|**656**|parZoneRoomCoolingSetpoint1 16-9|parZoneRoomCoolingSetpoint1 8-1|Raumtemperatursollwert<br>der Benutzeraktivität je<br>Kreis im Kühlbetrieb|Read/Write|UNSIGNED16|3412.n|Not Available|
|**657**|parZoneRoomCoolingSetpoint2 16-9|parZoneRoomCoolingSetpoint2 8-1|Raumtemperatursollwert<br>der Benutzeraktivität je<br>Kreis im Kühlbetrieb|Read/Write|UNSIGNED16|3412.n|Not Available|
|**658**|parZoneRoomCoolingSetpoint3 16-9|parZoneRoomCoolingSetpoint3 8-1|Raumtemperatursollwert<br>der Benutzeraktivität je<br>Kreis im Kühlbetrieb|Read/Write|UNSIGNED16|3412.n|Not Available|
|**659**|parZoneRoomCoolingSetpoint4 16-9|parZoneRoomCoolingSetpoint4 8-1|Raumtemperatursollwert<br>der Benutzeraktivität je<br>Kreis im Kühlbetrieb|Read/Write|UNSIGNED16|3412.n|Not Available|
|**660**|parZoneRoomCoolingSetpoint5 16-9|parZoneRoomCoolingSetpoint5 8-1|Raumtemperatursollwert<br>der Benutzeraktivität je<br>Kreis im Kühlbetrieb|Read/Write|UNSIGNED16|3412.n|Not Available|
|**661**|parZoneAmbiantCoolingNightSetpoint 16-9|parZoneAmbiantCoolingNightSetpoint 8-1|Raumsollwert zur<br>Umschaltung von<br>Komfort auf Reduziert im<br>Heizbetrieb|Read/Write|UNSIGNED16|3460.n|Not Available|
|**662**|parZoneAmbiantHolidaySetpoint 16-9|parZoneAmbiantHolidaySetpoint 8-1|Gewünschter<br>Raumtemperatur des<br>Kreises in der Ferienzeit|Read/Write|UNSIGNED16|340A.n|Not Available|
|**663**|parZoneTemporaryRoomSetpoint 16-9|parZoneTemporaryRoomSetpoint 8-1|Vorrübergehender<br>Raumsollwertje Kreis|Read/Write|UNSIGNED16|3451.n|Not Available|
|**664**|parZoneRoomManualSetpoint 16-9|parZoneRoomManualSetpoint 8-1|Manuell eingestellter<br>gewünschter<br>Raumtemperatur-<br>Sollwert des Kreises|Read/Write|UNSIGNED16|3413.n|Not Available|
|**665**|parZoneDhwComfortSetpoint 16-9|parZoneDhwComfortSetpoint  8-1|Gewünschte Komfort-<br>Warmwassertemperatur|Read/Write|UNSIGNED16|3425.n|3654.n|
|**666**|parZoneDhwReducedSetpoint 16-9|parZoneDhwReducedSetpoint  8-1|Gewünschte reduzierte<br>Warmwassertemperatur|Read/Write|UNSIGNED16|3426.n|3655.n|
|**667**|parZoneDhwHolidaySetpoint 16-9|parZoneDhwHolidaySetpoint  8-1|Gewünschte Ferien-<br>Warmwassertemperatur|Read/Write|UNSIGNED16|3427.n|3675.n|
|**668**|parZoneDhwAntilegionelSetpoint 16-9|parZoneDhwAntilegionelSetpoint  8-1|Antilegionellen-Sollwert<br>für Kreis Speicher|Read/Write|UNSIGNED16|3428.n|365D.n|
|**669**|parZoneSwimmingPoolSetpoint 16 -9|parZoneSwimmingPoolSetpoint 8 -1|Erforderlicher<br>Schwimmbad-<br>Temperatursollwert|Read/Write|UNSIGNED16|3454.n|Not Available|
|**670**|parZoneProcessHeatSetpoint 16 -9|parZoneProcessHeatSetpoint 8 -1|Sollwert während<br>"Prozesswärme"-<br>Heizanforderung|Read/Write|UNSIGNED16|345B.n|3654.n|
|**671**||parZoneHeatingControlStrategy|Verwenden Sie die<br>Raumregelung und/oder<br>witterungsgeführte<br>Regelstrategien zur<br>Berechnung des<br>Vorlaufsollwerts<br>0: AUTO<br>1: Raum<br>2: Außen<br>3: Außen + Raum|Read/Write|ENUM8|3471.n|Not Available|
|**672**|parZoneTFlowSetpointMax 16-9|parZoneTFlowSetpointMax 8-1|Max. Vorlauftemperatur-<br>Sollwert des Kreises|Read/Write|UNSIGNED16|3401.n|362F.0|
||||ARR|||||
|**673**|parZoneTFlowCoolingMixingSetpoint 16-9|parZoneTFlowCoolingMixingSetpoint  8-1|Erforderlicher<br>Vorlauftemperatur-<br>Sollwert beim Kühlen|Read/Write|UNSIGNED16|341A.n|Not Available|
|**674**||parZoneSlope|Steigung der<br>Heizkennlinie des Kreises|Read/Write|UNSIGNED8|3416.n|Not Available|
|**675**|parZoneHCZPD 16-9|parZoneHCZPD 8-1|Grundtemperatur der<br>Heizkennlinie im<br>Komfortbetrieb|Read/Write|UNSIGNED16|3414.n|Not Available|
|**676**|parZoneHCZPN 16-9|parZoneHCZPN 8-1|Grundtemperatur der<br>Heizkennlinie im<br>reduzierten Betrieb|Read/Write|UNSIGNED16|3415.n|Not Available|
|**677**|parZoneMaxPreHeatTime 16-9|parZoneMaxPreHeatTime  8-1|Max. Vorheizzeit|Read/Write|UNSIGNED16|346C.n|Not Available|
|**678**|parZoneMixingValveShift 16-9|parZoneMixingValveShift 8-1|Umschaltung zwischen<br>berechnetem Sollwert<br>und Sollwert, der an den<br>Verbrauchermanager für<br>den Mischerkreis<br>gesendet wird|Read/Write|UNSIGNED16|3409.n|Not Available|
|**679**|parZoneMixingValveBandwith 16-9|parZoneMixingValveBandwith  8-1|Bandbreite des<br>Mischventils des Kreises,<br>in dem die Modulation<br>stattfindet: Wenn der<br>Kreis kein Mischventil<br>hat, wird der Parameter<br>für diesen Kreis ignoriert.|Read/Write|UNSIGNED16|3405.n|Not Available|
|**680**|parZoneDhwHysterisis 16-9|parZoneDhwHysterisis 8-1|Hysterese TWW<br>Speicherladung|Read/Write|UNSIGNED16|342C.n|3606.0|
|**681**|parZoneDhwCalorifierOffset 16-9|parZoneDhwCalorifierOffset 8-1|Verschiebung TWW-<br>Bereiter|Read/Write|UNSIGNED16|3467.n|3622.0|
|**682**|parZoneDhwCalorifierSetpointRaise 16-9|parZoneDhwCalorifierSetpointRaise 8-1|Vorlauftemperatur-<br>Sollwert über die<br>erforderliche<br>Speichertemperatur Delta<br>T erhöhen, um den<br>Speicher zu erwärmen|Read/Write|UNSIGNED16|3468.n|3605.0|
|**683**|parZoneProcessHeatHysterisis 16-9|parZoneProcessHeatHysterisis 8-1|Hysterese für<br>Prozesswärme pro Kreis<br>eingeschaltet|Read/Write|UNSIGNED16|345C.n|Not Available|
|**684**|parZoneProcessHeatOffset 16-9|parZoneProcessHeatOffset 8-1|Hysterese für<br>Prozesswärme pro Kreis<br>ausgeschaltet|Read/Write|UNSIGNED16|345D.n|Not Available|
|**685**|parZoneProcessHeatCalorifierSetpointRaise<br>16-9|parZoneProcessHeatCalorifierSetpointRaise<br>8-1|Vorlauftemperatur-<br>Sollwert über die<br>erforderliche<br>Speichertemperatur Delta<br>T erhöhen, um den<br>Speicher zu erwärmen|Read/Write|UNSIGNED16|3469.n|Not Available|
|**686**|parZoneDhwCalorifierHysterisis 16-9|parZoneDhwCalorifierHysterisis 8-1|Hysterese zum Starten<br>der<br>Warmwasserbereitung|Read/Write|UNSIGNED16|342C.n|3659.n|
|**687**||parZonePumpPostRun|Verzögerung für Nachlauf<br>der Pumpe des Kreises|Read/Write|UNSIGNED8|3408.n|3614.0|
|**688**||parZoneTimeProgramSelected|Vom Benutzer gewähltes<br>Zeitprogramm<br>0: Zeitprogramm 1<br>1: Zeitprogramm 2<br>2: Zeitprogramm 3|Read/Write|ENUM8|3458.n|3653.n|
|**689**|parZoneTimeProgramMonday1 Byte 0|parZoneTimeProgramMonday1 Byte 1|Zeitprogramm 1|Read/Write|OCTET_STRING|3431.n|363E.n|
|**690**|parZoneTimeProgramMonday1 Byte 2|parZoneTimeProgramMonday1 Byte 3||||||
|**691**|parZoneTimeProgramMonday1 Byte 4|parZoneTimeProgramMonday1 Byte 5||||||
|**692**|parZoneTimeProgramMonday1 Byte 6|parZoneTimeProgramMonday1 Byte 7||||||
|**693**|parZoneTimeProgramMonday1 Byte 8|parZoneTimeProgramMonday1 Byte 9||||||
|**694**|parZoneTimeProgramMonday1 Byte 10|parZoneTimeProgramMonday1 Byte 11||||||
|**695**|parZoneTimeProgramMonday1 Byte 12|parZoneTimeProgramMonday1 Byte 13||||||
|**696**|parZoneTimeProgramMonday1 Byte 14|parZoneTimeProgramMonday1 Byte 15||||||
|**697**|parZoneTimeProgramMonday1 Byte 16|parZoneTimeProgramMonday1 Byte 17||||||
|**698**|parZoneTimeProgramMonday1 Byte 18|||||||
|**699**|parZoneTimeProgramTuesday1 Byte 0|parZoneTimeProgramTuesday1 Byte 1||Read/Write|OCTET_STRING|3432.n|363F.n|
|**700**|parZoneTimeProgramTuesday1 Byte 2|parZoneTimeProgramTuesday1 Byte 3||||||
|**701**|parZoneTimeProgramTuesday1 Byte 4|parZoneTimeProgramTuesday1 Byte 5||||||
|**702**|parZoneTimeProgramTuesday1 Byte 6|parZoneTimeProgramTuesday1 Byte 7||||||
|**703**|parZoneTimeProgramTuesday1 Byte 8|parZoneTimeProgramTuesday1 Byte 9||||||
|**704**|parZoneTimeProgramTuesday1 Byte 10|parZoneTimeProgramTuesday1 Byte 11||||||
|**705**|parZoneTimeProgramTuesday1 Byte 12|parZoneTimeProgramTuesday1 Byte 13||||||
|**706**|parZoneTimeProgramTuesday1 Byte 14|parZoneTimeProgramTuesday1 Byte 15||||||
|**707**|parZoneTimeProgramTuesday1 Byte 16|parZoneTimeProgramTuesday1 Byte 17||||||
|**708**|parZoneTimeProgramTuesday1 Byte 18|||||||
|**709**|parZoneTimeProgramWednesday1 Byte 0|parZoneTimeProgramWednesday1 Byte 1||Read/Write|OCTET_STRING|3433.n|3640.n|
|**710**|parZoneTimeProgramWednesday1 Byte 2|parZoneTimeProgramWednesday1 Byte 3||||||
|**711**|parZoneTimeProgramWednesday1 Byte 4|parZoneTimeProgramWednesday1 Byte 5||||||
|**712**|parZoneTimeProgramWednesday1 Byte 6|parZoneTimeProgramWednesday1 Byte 7||||||
|**713**|parZoneTimeProgramWednesday1 Byte 8|parZoneTimeProgramWednesday1 Byte 9||||||
|**714**|parZoneTimeProgramWednesday1 Byte 10|parZoneTimeProgramWednesday1 Byte 11||||||
|**715**|parZoneTimeProgramWednesday1 Byte 12|parZoneTimeProgramWednesday1 Byte 13||||||
|**716**|parZoneTimeProgramWednesday1 Byte 14|parZoneTimeProgramWednesday1 Byte 15||||||
|**717**|parZoneTimeProgramWednesday1 Byte 16|parZoneTimeProgramWednesday1 Byte 17||||||
|**718**|parZoneTimeProgramWednesday1 Byte 18|||||||
|**719**|parZoneTimeProgramThursday1 Byte 0|parZoneTimeProgramThursday1 Byte 1||Read/Write|OCTET_STRING|3434.n|3641.n|
|**720**|parZoneTimeProgramThursday1 Byte 2|parZoneTimeProgramThursday1 Byte 3||||||
|**721**|parZoneTimeProgramThursday1 Byte 4|parZoneTimeProgramThursday1 Byte 5||||||
|**722**|parZoneTimeProgramThursday1 Byte 6|parZoneTimeProgramThursday1 Byte 7||||||
|**723**|parZoneTimeProgramThursday1 Byte 8|parZoneTimeProgramThursday1 Byte 9||||||
|**724**|parZoneTimeProgramThursday1 Byte 10|parZoneTimeProgramThursday1 Byte 11||||||
|**725**|parZoneTimeProgramThursday1 Byte 12|parZoneTimeProgramThursday1 Byte 13||||||
|**726**|parZoneTimeProgramThursday1 Byte 14|parZoneTimeProgramThursday1 Byte 15||||||
|**727**|parZoneTimeProgramThursday1 Byte 16|parZoneTimeProgramThursday1 Byte 17||||||
|**728**|parZoneTimeProgramThursday1 Byte 18|||||||
|**729**|parZoneTimeProgramFriday1 Byte 0|parZoneTimeProgramFriday1 Byte 1||Read/Write|OCTET_STRING|3435.n|3642.n|
|**730**|parZoneTimeProgramFriday1 Byte 2|parZoneTimeProgramFriday1 Byte 3||||||
|**731**|parZoneTimeProgramFriday1 Byte 4|parZoneTimeProgramFriday1 Byte 5||||||
|**732**|parZoneTimeProgramFriday1 Byte 6|parZoneTimeProgramFriday1 Byte 7||||||
|**733**|parZoneTimeProgramFriday1 Byte 8|parZoneTimeProgramFriday1 Byte 9||||||
|**734**|parZoneTimeProgramFriday1 Byte 10|parZoneTimeProgramFriday1 Byte 11||||||
|**735**|parZoneTimeProgramFriday1 Byte 12|parZoneTimeProgramFriday1 Byte 13||||||
|**736**|parZoneTimeProgramFriday1 Byte 14|parZoneTimeProgramFriday1 Byte 15||||||
|**737**|parZoneTimeProgramFriday1 Byte 16|parZoneTimeProgramFriday1 Byte 17||||||
|**738**|parZoneTimeProgramFriday1 Byte 18|||||||
|**739**|parZoneTimeProgramSaturday1 Byte 0|parZoneTimeProgramSaturday1 Byte 1||Read/Write|OCTET_STRING|3436.n|3643.n|
|**740**|parZoneTimeProgramSaturday1 Byte 2|parZoneTimeProgramSaturday1 Byte 3||||||
|**741**|parZoneTimeProgramSaturday1 Byte 4|parZoneTimeProgramSaturday1 Byte 5||||||
|**742**|parZoneTimeProgramSaturday1 Byte 6|parZoneTimeProgramSaturday1 Byte 7||||||
|**743**|parZoneTimeProgramSaturday1 Byte 8|parZoneTimeProgramSaturday1 Byte 9||||||
|**744**|parZoneTimeProgramSaturday1 Byte 10|parZoneTimeProgramSaturday1 Byte 11||||||
|**745**|parZoneTimeProgramSaturday1 Byte 12|parZoneTimeProgramSaturday1 Byte 13||||||
|**746**|parZoneTimeProgramSaturday1 Byte 14|parZoneTimeProgramSaturday1 Byte 15||||||
|**747**|parZoneTimeProgramSaturday1 Byte 16|parZoneTimeProgramSaturday1 Byte 17||||||
|**748**|parZoneTimeProgramSaturday1 Byte 18|||||||
|**749**|parZoneTimeProgramSunday1 Byte 0|parZoneTimeProgramSunday1 Byte 1||Read/Write|OCTET_STRING|3437.n|3644.n|
|**750**|parZoneTimeProgramSunday1 Byte 2|parZoneTimeProgramSunday1 Byte 3||||||
|**751**|parZoneTimeProgramSunday1 Byte 4|parZoneTimeProgramSunday1 Byte 5||||||
|**752**|parZoneTimeProgramSunday1 Byte 6|parZoneTimeProgramSunday1 Byte 7||||||
|**753**|parZoneTimeProgramSunday1 Byte 8|parZoneTimeProgramSunday1 Byte 9||||||
|**754**|parZoneTimeProgramSunday1 Byte 10|parZoneTimeProgramSunday1 Byte 11||||||
|**755**|parZoneTimeProgramSunday1 Byte 12|parZoneTimeProgramSunday1 Byte 13||||||
|**756**|parZoneTimeProgramSunday1 Byte 14|parZoneTimeProgramSunday1 Byte 15||||||
|**757**|parZoneTimeProgramSunday1 Byte 16|parZoneTimeProgramSunday1 Byte 17||||||
|**758**|parZoneTimeProgramSunday1 Byte 18|||||||
|**759**|parZoneTimeProgramMonday2  Byte 0|parZoneTimeProgramMonday2  Byte 1|Zeitprogramm 2|Read/Write|OCTET_STRING|3438.n|3645.n|
|**760**|parZoneTimeProgramMonday2  Byte 2|parZoneTimeProgramMonday2  Byte 3||||||
|**761**|parZoneTimeProgramMonday2  Byte 4|parZoneTimeProgramMonday2  Byte 5||||||
|**762**|parZoneTimeProgramMonday2  Byte 6|parZoneTimeProgramMonday2  Byte 7||||||
|**763**|parZoneTimeProgramMonday2  Byte 8|parZoneTimeProgramMonday2  Byte 9||||||
|**764**|parZoneTimeProgramMonday2  Byte 10|parZoneTimeProgramMonday2  Byte 11||||||
|**765**|parZoneTimeProgramMonday2  Byte 12|parZoneTimeProgramMonday2  Byte 13||||||
|**766**|parZoneTimeProgramMonday2  Byte 14|parZoneTimeProgramMonday2  Byte 15||||||
|**767**|parZoneTimeProgramMonday2  Byte 16|parZoneTimeProgramMonday2  Byte 17||||||
|**768**|parZoneTimeProgramMonday2  Byte 18|||||||
|**769**|parZoneTimeProgramTuesday2  Byte 0|parZoneTimeProgramTuesday2  Byte 1||Read/Write|OCTET_STRING|3439.n|3646.n|
|**770**|parZoneTimeProgramTuesday2  Byte 2|parZoneTimeProgramTuesday2  Byte 3||||||
|**771**|parZoneTimeProgramTuesday2  Byte 4|parZoneTimeProgramTuesday2  Byte 5||||||
|**772**|parZoneTimeProgramTuesday2  Byte 6|parZoneTimeProgramTuesday2  Byte 7||||||
|**773**|parZoneTimeProgramTuesday2  Byte 8|parZoneTimeProgramTuesday2  Byte 9||||||
|**774**|parZoneTimeProgramTuesday2  Byte 10|parZoneTimeProgramTuesday2  Byte 11||||||
|**775**|parZoneTimeProgramTuesday2  Byte 12|parZoneTimeProgramTuesday2  Byte 13||||||
|**776**|parZoneTimeProgramTuesday2  Byte 14|parZoneTimeProgramTuesday2  Byte 15||||||
|**777**|parZoneTimeProgramTuesday2  Byte 16|parZoneTimeProgramTuesday2  Byte 17||||||
|**778**|parZoneTimeProgramTuesday2  Byte 18|||||||
|**779**|parZoneTimeProgramWednesday2 Byte 0|parZoneTimeProgramWednesday2 Byte 1||Read/Write|OCTET_STRING|343A.n|3647.n|
|**780**|parZoneTimeProgramWednesday2 Byte 2|parZoneTimeProgramWednesday2 Byte 3||||||
|**781**|parZoneTimeProgramWednesday2 Byte 4|parZoneTimeProgramWednesday2 Byte 5||||||
|**782**|parZoneTimeProgramWednesday2 Byte 6|parZoneTimeProgramWednesday2 Byte 7||||||
|**783**|parZoneTimeProgramWednesday2 Byte 8|parZoneTimeProgramWednesday2 Byte 9||||||
|**784**|parZoneTimeProgramWednesday2 Byte 10|parZoneTimeProgramWednesday2 Byte 11||||||
|**785**|parZoneTimeProgramWednesday2 Byte 12|parZoneTimeProgramWednesday2 Byte 13||||||
|**786**|parZoneTimeProgramWednesday2 Byte 14|parZoneTimeProgramWednesday2 Byte 15||||||
|**787**|parZoneTimeProgramWednesday2 Byte 16|parZoneTimeProgramWednesday2 Byte 17||||||
|**788**|parZoneTimeProgramWednesday2 Byte 18|||||||
|**789**|parZoneTimeProgramThursday2  Byte 0|parZoneTimeProgramThursday2  Byte 1||Read/Write|OCTET_STRING|343B.n|3648.n|
|**790**|parZoneTimeProgramThursday2  Byte 2|parZoneTimeProgramThursday2  Byte 3||||||
|**791**|parZoneTimeProgramThursday2  Byte 4|parZoneTimeProgramThursday2  Byte 5||||||
|**792**|parZoneTimeProgramThursday2  Byte 6|parZoneTimeProgramThursday2  Byte 7||||||
|**793**|parZoneTimeProgramThursday2  Byte 8|parZoneTimeProgramThursday2  Byte 9||||||
|**794**|parZoneTimeProgramThursday2  Byte 10|parZoneTimeProgramThursday2  Byte 11||||||
|**795**|parZoneTimeProgramThursday2  Byte 12|parZoneTimeProgramThursday2  Byte 13||||||
|**796**|parZoneTimeProgramThursday2  Byte 14|parZoneTimeProgramThursday2  Byte 15||||||
|**797**|parZoneTimeProgramThursday2  Byte 16|parZoneTimeProgramThursday2  Byte 17||||||
|**798**|parZoneTimeProgramThursday2  Byte 18|||||||
|**799**|parZoneTimeProgramFriday2 Byte 0|parZoneTimeProgramFriday2 Byte 1||Read/Write|OCTET_STRING|343C.n|3649.n|
|**800**|parZoneTimeProgramFriday2 Byte 2|parZoneTimeProgramFriday2 Byte 3||||||
|**801**|parZoneTimeProgramFriday2 Byte 4|parZoneTimeProgramFriday2 Byte 5||||||
|**802**|parZoneTimeProgramFriday2 Byte 6|parZoneTimeProgramFriday2 Byte 7||||||
|**803**|parZoneTimeProgramFriday2 Byte 8|parZoneTimeProgramFriday2 Byte 9||||||
|**804**|parZoneTimeProgramFriday2 Byte 10|parZoneTimeProgramFriday2 Byte 11||||||
|**805**|parZoneTimeProgramFriday2 Byte 12|parZoneTimeProgramFriday2 Byte 13||||||
|**806**|parZoneTimeProgramFriday2 Byte 14|parZoneTimeProgramFriday2 Byte 15||||||
|**807**|parZoneTimeProgramFriday2 Byte 16|parZoneTimeProgramFriday2 Byte 17||||||
|**808**|parZoneTimeProgramFriday2 Byte 18|||||||
|**809**|parZoneTimeProgramSaturday2  Byte 0|parZoneTimeProgramSaturday2  Byte 1||Read/Write|OCTET_STRING|343D.n|364A.n|
|**810**|parZoneTimeProgramSaturday2  Byte 2|parZoneTimeProgramSaturday2  Byte 3||||||
|**811**|parZoneTimeProgramSaturday2  Byte 4|parZoneTimeProgramSaturday2  Byte 5||||||
|**812**|parZoneTimeProgramSaturday2  Byte 6|parZoneTimeProgramSaturday2  Byte 7||||||
|**813**|parZoneTimeProgramSaturday2  Byte 8|parZoneTimeProgramSaturday2  Byte 9||||||
|**814**|parZoneTimeProgramSaturday2  Byte 10|parZoneTimeProgramSaturday2  Byte 11||||||
|**815**|parZoneTimeProgramSaturday2  Byte 12|parZoneTimeProgramSaturday2  Byte 13||||||
|**816**|parZoneTimeProgramSaturday2  Byte 14|parZoneTimeProgramSaturday2  Byte 15||||||
|**817**|parZoneTimeProgramSaturday2  Byte 16|parZoneTimeProgramSaturday2  Byte 17||||||
|**818**|parZoneTimeProgramSaturday2  Byte 18|||||||
|**819**|parZoneTimeProgramSunday2 Byte 0|parZoneTimeProgramSunday2 Byte 1||Read/Write|OCTET_STRING|343E.n|364B.n|
|**820**|parZoneTimeProgramSunday2 Byte 2|parZoneTimeProgramSunday2 Byte 3||||||
|**821**|parZoneTimeProgramSunday2 Byte 4|parZoneTimeProgramSunday2 Byte 5||||||
|**822**|parZoneTimeProgramSunday2 Byte 6|parZoneTimeProgramSunday2 Byte 7||||||
|**823**|parZoneTimeProgramSunday2 Byte 8|parZoneTimeProgramSunday2 Byte 9||||||
|**824**|parZoneTimeProgramSunday2 Byte 10|parZoneTimeProgramSunday2 Byte 11||||||
|**825**|parZoneTimeProgramSunday2 Byte 12|parZoneTimeProgramSunday2 Byte 13||||||
|**826**|parZoneTimeProgramSunday2 Byte 14|parZoneTimeProgramSunday2 Byte 15||||||
|**827**|parZoneTimeProgramSunday2 Byte 16|parZoneTimeProgramSunday2 Byte 17||||||
|**828**|parZoneTimeProgramSunday2 Byte 18|||||||
|**829**|parZoneTimeProgramMonday3 Byte 0|parZoneTimeProgramMonday3 Byte 1|Zeitprogramm 3|Read/Write|OCTET_STRING|343F.n|364C.n|
|**830**|parZoneTimeProgramMonday3 Byte 2|parZoneTimeProgramMonday3 Byte 3||||||
|**831**|parZoneTimeProgramMonday3 Byte 4|parZoneTimeProgramMonday3 Byte 5||||||
|**832**|parZoneTimeProgramMonday3 Byte 6|parZoneTimeProgramMonday3 Byte 7||||||
|**833**|parZoneTimeProgramMonday3 Byte 8|parZoneTimeProgramMonday3 Byte 9||||||
|**834**|parZoneTimeProgramMonday3 Byte 10|parZoneTimeProgramMonday3 Byte 11||||||
|**835**|parZoneTimeProgramMonday3 Byte 12|parZoneTimeProgramMonday3 Byte 13||||||
|**836**|parZoneTimeProgramMonday3 Byte 14|parZoneTimeProgramMonday3 Byte 15||||||
|**837**|parZoneTimeProgramMonday3 Byte 16|parZoneTimeProgramMonday3 Byte 17||||||
|**838**|parZoneTimeProgramMonday3 Byte 18|||||||
|**839**|parZoneTimeProgramTuesday3 Byte 0|parZoneTimeProgramTuesday3 Byte 1||Read/Write|OCTET_STRING|3440.n|364D.n|
|**840**|parZoneTimeProgramTuesday3 Byte 2|parZoneTimeProgramTuesday3 Byte 3||||||
|**841**|parZoneTimeProgramTuesday3 Byte 4|parZoneTimeProgramTuesday3 Byte 5||||||
|**842**|parZoneTimeProgramTuesday3 Byte 6|parZoneTimeProgramTuesday3 Byte 7||||||
|**843**|parZoneTimeProgramTuesday3 Byte 8|parZoneTimeProgramTuesday3 Byte 9||||||
|**844**|parZoneTimeProgramTuesday3 Byte 10|parZoneTimeProgramTuesday3 Byte 11||||||
|**845**|parZoneTimeProgramTuesday3 Byte 12|parZoneTimeProgramTuesday3 Byte 13||||||
|**846**|parZoneTimeProgramTuesday3 Byte 14|parZoneTimeProgramTuesday3 Byte 15||||||
|**847**|parZoneTimeProgramTuesday3 Byte 16|parZoneTimeProgramTuesday3 Byte 17||||||
|**848**|parZoneTimeProgramTuesday3 Byte 18|||||||
|**849**|parZoneTimeProgramWednesday3Byte 0|parZoneTimeProgramWednesday3Byte 1||Read/Write|OCTET_STRING|3441.n|364E.n|
|**850**|parZoneTimeProgramWednesday3Byte 2|parZoneTimeProgramWednesday3Byte 3||||||
|**851**|parZoneTimeProgramWednesday3Byte 4|parZoneTimeProgramWednesday3Byte 5||||||
|**852**|parZoneTimeProgramWednesday3Byte 6|parZoneTimeProgramWednesday3Byte 7||||||
|**853**|parZoneTimeProgramWednesday3Byte 8|parZoneTimeProgramWednesday3Byte 9||||||
|**854**|parZoneTimeProgramWednesday3Byte 10|parZoneTimeProgramWednesday3Byte 11||||||
|**855**|parZoneTimeProgramWednesday3Byte 12|parZoneTimeProgramWednesday3Byte 13||||||
|**856**|parZoneTimeProgramWednesday3Byte 14|parZoneTimeProgramWednesday3Byte 15||||||
|**857**|parZoneTimeProgramWednesday3Byte 16|parZoneTimeProgramWednesday3Byte 17||||||
|**858**|parZoneTimeProgramWednesday3Byte 18|||||||
|**859**|parZoneTimeProgramThursday3 Byte 0|parZoneTimeProgramThursday3 Byte 1||Read/Write|OCTET_STRING|3442.n|364F.n|
|**860**|parZoneTimeProgramThursday3 Byte 2|parZoneTimeProgramThursday3 Byte 3||||||
|**861**|parZoneTimeProgramThursday3 Byte 4|parZoneTimeProgramThursday3 Byte 5||||||
|**862**|parZoneTimeProgramThursday3 Byte 6|parZoneTimeProgramThursday3 Byte 7||||||
|**863**|parZoneTimeProgramThursday3 Byte 8|parZoneTimeProgramThursday3 Byte 9||||||
|**864**|parZoneTimeProgramThursday3 Byte 10|parZoneTimeProgramThursday3 Byte 11||||||
|**865**|parZoneTimeProgramThursday3 Byte 12|parZoneTimeProgramThursday3 Byte 13||||||
|**866**|parZoneTimeProgramThursday3 Byte 14|parZoneTimeProgramThursday3 Byte 15||||||
|**867**|parZoneTimeProgramThursday3 Byte 16|parZoneTimeProgramThursday3 Byte 17||||||
|**868**|parZoneTimeProgramThursday3 Byte 18|||||||
|**869**|parZoneTimeProgramFriday3Byte 0|parZoneTimeProgramFriday3Byte 1||Read/Write|OCTET_STRING|3443.n|3650.n|
|**870**|parZoneTimeProgramFriday3Byte 2|parZoneTimeProgramFriday3Byte 3||||||
|**871**|parZoneTimeProgramFriday3Byte 4|parZoneTimeProgramFriday3Byte 5||||||
|**872**|parZoneTimeProgramFriday3Byte 6|parZoneTimeProgramFriday3Byte 7||||||
|**873**|parZoneTimeProgramFriday3Byte 8|parZoneTimeProgramFriday3Byte 9||||||
|**874**|parZoneTimeProgramFriday3Byte 10|parZoneTimeProgramFriday3Byte 11||||||
|**875**|parZoneTimeProgramFriday3Byte 12|parZoneTimeProgramFriday3Byte 13||||||
|**876**|parZoneTimeProgramFriday3Byte 14|parZoneTimeProgramFriday3Byte 15||||||
|**877**|parZoneTimeProgramFriday3Byte 16|parZoneTimeProgramFriday3Byte 17||||||
|**878**|parZoneTimeProgramFriday3Byte 18|||||||
|**879**|parZoneTimeProgramSaturday3 Byte 0|parZoneTimeProgramSaturday3 Byte 1||Read/Write|OCTET_STRING|3444.n|3651.n|
|**880**|parZoneTimeProgramSaturday3 Byte 2|parZoneTimeProgramSaturday3 Byte 3||||||
|**881**|parZoneTimeProgramSaturday3 Byte 4|parZoneTimeProgramSaturday3 Byte 5||||||
|**882**|parZoneTimeProgramSaturday3 Byte 6|parZoneTimeProgramSaturday3 Byte 7||||||
|**883**|parZoneTimeProgramSaturday3 Byte 8|parZoneTimeProgramSaturday3 Byte 9||||||
|**884**|parZoneTimeProgramSaturday3 Byte 10|parZoneTimeProgramSaturday3 Byte 11||||||
|**885**|parZoneTimeProgramSaturday3 Byte 12|parZoneTimeProgramSaturday3 Byte 13||||||
|**886**|parZoneTimeProgramSaturday3 Byte 14|parZoneTimeProgramSaturday3 Byte 15||||||
|**887**|parZoneTimeProgramSaturday3 Byte 16|parZoneTimeProgramSaturday3 Byte 17||||||
|**888**|parZoneTimeProgramSaturday3 Byte 18|||||||
|**889**|parZoneTimeProgramSunday3Byte 0|parZoneTimeProgramSunday3Byte 1||Read/Write|OCTET_STRING|3445.n|3652.n|
|**890**|parZoneTimeProgramSunday3Byte 2|parZoneTimeProgramSunday3Byte 3||||||
|**891**|parZoneTimeProgramSunday3Byte 4|parZoneTimeProgramSunday3Byte 5||||||
|**892**|parZoneTimeProgramSunday3Byte 6|parZoneTimeProgramSunday3Byte 7||||||
|**893**|parZoneTimeProgramSunday3Byte 8|parZoneTimeProgramSunday3Byte 9||||||
|**894**|parZoneTimeProgramSunday3Byte 10|parZoneTimeProgramSunday3Byte 11||||||
|**895**|parZoneTimeProgramSunday3Byte 12|parZoneTimeProgramSunday3Byte 13||||||
|**896**|parZoneTimeProgramSunday3Byte 14|parZoneTimeProgramSunday3Byte 15||||||
|**897**|parZoneTimeProgramSunday3Byte 16|parZoneTimeProgramSunday3Byte 17||||||
|**898**|parZoneTimeProgramSunday3Byte 18|||||||
|**899**|parZoneTimeProgramMonday4 Byte 0|parZoneTimeProgramMonday4 Byte 1|Zeitprogramm 4|Read/Write|OCTET_STRING|3446.n|Not Available|
|**900**|parZoneTimeProgramMonday4 Byte 2|parZoneTimeProgramMonday4 Byte 3||||||
|**901**|parZoneTimeProgramMonday4 Byte 4|parZoneTimeProgramMonday4 Byte 5||||||
|**902**|parZoneTimeProgramMonday4 Byte 6|parZoneTimeProgramMonday4 Byte 7||||||
|**903**|parZoneTimeProgramMonday4 Byte 8|parZoneTimeProgramMonday4 Byte 9||||||
|**904**|parZoneTimeProgramMonday4 Byte 10|parZoneTimeProgramMonday4 Byte 11||||||
|**905**|parZoneTimeProgramMonday4 Byte 12|parZoneTimeProgramMonday4 Byte 13||||||
|**906**|parZoneTimeProgramMonday4 Byte 14|parZoneTimeProgramMonday4 Byte 15||||||
|**907**|parZoneTimeProgramMonday4 Byte 16|parZoneTimeProgramMonday4 Byte 17||||||
|**908**|parZoneTimeProgramMonday4 Byte 18|||||||
|**909**|parZoneTimeProgramTuesday4 Byte 0|parZoneTimeProgramTuesday4 Byte 1||Read/Write|OCTET_STRING|3447.n|Not Available|
|**910**|parZoneTimeProgramTuesday4 Byte 2|parZoneTimeProgramTuesday4 Byte 3||||||
|**911**|parZoneTimeProgramTuesday4 Byte 4|parZoneTimeProgramTuesday4 Byte 5||||||
|**912**|parZoneTimeProgramTuesday4 Byte 6|parZoneTimeProgramTuesday4 Byte 7||||||
|**913**|parZoneTimeProgramTuesday4 Byte 8|parZoneTimeProgramTuesday4 Byte 9||||||
|**914**|parZoneTimeProgramTuesday4 Byte 10|parZoneTimeProgramTuesday4 Byte 11||||||
|**915**|parZoneTimeProgramTuesday4 Byte 12|parZoneTimeProgramTuesday4 Byte 13||||||
|**916**|parZoneTimeProgramTuesday4 Byte 14|parZoneTimeProgramTuesday4 Byte 15||||||
|**917**|parZoneTimeProgramTuesday4 Byte 16|parZoneTimeProgramTuesday4 Byte 17||||||
|**918**|parZoneTimeProgramTuesday4 Byte 18|||||||
|**919**|parZoneTimeProgramWednesday4Byte 0|parZoneTimeProgramWednesday4Byte 1||Read/Write|OCTET_STRING|3448.n|Not Available|
|**920**|parZoneTimeProgramWednesday4Byte 2|parZoneTimeProgramWednesday4Byte 3||||||
|**921**|parZoneTimeProgramWednesday4Byte 4|parZoneTimeProgramWednesday4Byte 5||||||
|**922**|parZoneTimeProgramWednesday4Byte 6|parZoneTimeProgramWednesday4Byte 7||||||
|**923**|parZoneTimeProgramWednesday4Byte 8|parZoneTimeProgramWednesday4Byte 9||||||
|**924**|parZoneTimeProgramWednesday4Byte 10|parZoneTimeProgramWednesday4Byte 11||||||
|**925**|parZoneTimeProgramWednesday4Byte 12|parZoneTimeProgramWednesday4Byte 13||||||
|**926**|parZoneTimeProgramWednesday4Byte 14|parZoneTimeProgramWednesday4Byte 15||||||
|**927**|parZoneTimeProgramWednesday4Byte 16|parZoneTimeProgramWednesday4Byte 17||||||
|**928**|parZoneTimeProgramWednesday4Byte 18|||||||
|**929**|parZoneTimeProgramThursday4 Byte 0|parZoneTimeProgramThursday4 Byte 1||Read/Write|OCTET_STRING|3449.n|Not Available|
|**930**|parZoneTimeProgramThursday4 Byte 2|parZoneTimeProgramThursday4 Byte 3||||||
|**931**|parZoneTimeProgramThursday4 Byte 4|parZoneTimeProgramThursday4 Byte 5||||||
|**932**|parZoneTimeProgramThursday4 Byte 6|parZoneTimeProgramThursday4 Byte 7||||||
|**933**|parZoneTimeProgramThursday4 Byte 8|parZoneTimeProgramThursday4 Byte 9||||||
|**934**|parZoneTimeProgramThursday4 Byte 10|parZoneTimeProgramThursday4 Byte 11||||||
|**935**|parZoneTimeProgramThursday4 Byte 12|parZoneTimeProgramThursday4 Byte 13||||||
|**936**|parZoneTimeProgramThursday4 Byte 14|parZoneTimeProgramThursday4 Byte 15||||||
|**937**|parZoneTimeProgramThursday4 Byte 16|parZoneTimeProgramThursday4 Byte 17||||||
|**938**|parZoneTimeProgramThursday4 Byte 18|||||||
|**939**|parZoneTimeProgramFriday4Byte 0|parZoneTimeProgramFriday4Byte 1||Read/Write|OCTET_STRING|344A.n|Not Available|
|**940**|parZoneTimeProgramFriday4Byte 2|parZoneTimeProgramFriday4Byte 3||||||
|**941**|parZoneTimeProgramFriday4Byte 4|parZoneTimeProgramFriday4Byte 5||||||
|**942**|parZoneTimeProgramFriday4Byte 6|parZoneTimeProgramFriday4Byte 7||||||
|**943**|parZoneTimeProgramFriday4Byte 8|parZoneTimeProgramFriday4Byte 9||||||
|**944**|parZoneTimeProgramFriday4Byte 10|parZoneTimeProgramFriday4Byte 11||||||
|**945**|parZoneTimeProgramFriday4Byte 12|parZoneTimeProgramFriday4Byte 13||||||
|**946**|parZoneTimeProgramFriday4Byte 14|parZoneTimeProgramFriday4Byte 15||||||
|**947**|parZoneTimeProgramFriday4Byte 16|parZoneTimeProgramFriday4Byte 17||||||
|**948**|parZoneTimeProgramFriday4Byte 18|||||||
|**949**|parZoneTimeProgramSaturday4 Byte 0|parZoneTimeProgramSaturday4 Byte 1||Read/Write|OCTET_STRING|344B.n|Not Available|
|**950**|parZoneTimeProgramSaturday4 Byte 2|parZoneTimeProgramSaturday4 Byte 3||||||
|**951**|parZoneTimeProgramSaturday4 Byte 4|parZoneTimeProgramSaturday4 Byte 5||||||
|**952**|parZoneTimeProgramSaturday4 Byte 6|parZoneTimeProgramSaturday4 Byte 7||||||
|**953**|parZoneTimeProgramSaturday4 Byte 8|parZoneTimeProgramSaturday4 Byte 9||||||
|**954**|parZoneTimeProgramSaturday4 Byte 10|parZoneTimeProgramSaturday4 Byte 11||||||
|**955**|parZoneTimeProgramSaturday4 Byte 12|parZoneTimeProgramSaturday4 Byte 13||||||
|**956**|parZoneTimeProgramSaturday4 Byte 14|parZoneTimeProgramSaturday4 Byte 15||||||
|**957**|parZoneTimeProgramSaturday4 Byte 16|parZoneTimeProgramSaturday4 Byte 17||||||
|**958**|parZoneTimeProgramSaturday4 Byte 18|||||||
|**959**|parZoneTimeProgramSunday4Byte 0|parZoneTimeProgramSunday4Byte 1||Read/Write|OCTET_STRING|344C.n|Not Available|
|**960**|parZoneTimeProgramSunday4Byte 2|parZoneTimeProgramSunday4Byte 3||||||
|**961**|parZoneTimeProgramSunday4Byte 4|parZoneTimeProgramSunday4Byte 5||||||
|**962**|parZoneTimeProgramSunday4Byte 6|parZoneTimeProgramSunday4Byte 7||||||
|**963**|parZoneTimeProgramSunday4Byte 8|parZoneTimeProgramSunday4Byte 9||||||
|**964**|parZoneTimeProgramSunday4Byte 10|parZoneTimeProgramSunday4Byte 11||||||
|**965**|parZoneTimeProgramSunday4Byte 12|parZoneTimeProgramSunday4Byte 13||||||
|**966**|parZoneTimeProgramSunday4Byte 14|parZoneTimeProgramSunday4Byte 15||||||
|**967**|parZoneTimeProgramSunday4Byte 16|parZoneTimeProgramSunday4Byte 17||||||
|**968**|parZoneTimeProgramSunday4Byte 18|||||||
|**969**||||||||
|**970**||||||||
|**971**|parZoneStartTimeHoliday Byte 0|parZoneStartTimeHoliday Byte 1|Startzeit Ferienbetrieb<br>ZeitStempel CIA|Read/Write|OCTET_STRING|3421.n|365E.n|
|**972**|parZoneStartTimeHoliday Byte 2|parZoneStartTimeHoliday Byte 3||||||
|**973**|parZoneStartTimeHoliday Byte 4|parZoneStartTimeHoliday Byte 5||||||
|**974**|parZoneEndTimeHoliday Byte 0|parZoneEndTimeHoliday Byte 1|Endzeit Ferienbetrieb<br>ZeitStempel|Read/Write|OCTET_STRING|3422.n|365F.n|
|**975**|parZoneEndTimeHoliday Byte 2|parZoneEndTimeHoliday Byte 3||||||
|**976**|parZoneEndTimeHoliday Byte 4|parZoneEndTimeHoliday Byte 5||||||
|**977**||||||||
|**978**|parZoneEndTimeModeChange Byte 0|parZoneEndTimeModeChange Byte 1|Uhrzeit Ende<br>Modusänderung<br>ZeitStempel CIA|Read/Write|OCTET_STRING|3423.n|3660.n|
|**979**|parZoneEndTimeModeChange Byte 2|parZoneEndTimeModeChange Byte 3||||||
|**980**|parZoneEndTimeModeChange Byte 4|parZoneEndTimeModeChange Byte 5||||||
|**981-**<br>**1099**||||||||
|||reserved for futur|use|||||
|**1100**|varZoneTflow 16-9|varZoneTflow 8-1|Temperatur des in dem<br>Kreis fließenden Wassers.<br>Im Fall von TWW ist dies<br>die Temperatur des<br>austretenden<br>Trinkwarmwassers.|Read|INTEGER16|5405.n|501A.0|
|**1101**|varZoneTemperatureSetpoint 16 -9|varZoneTemperatureSetpoint 8-1|Aktueller<br>Vorlauftemperatur-<br>Sollwert|Read|UNSIGNED16|5408.n|5604.0|
|**1102**|varZoneTRoomSetpoint 16 -9|varZoneTRoomSetpoint 8-1|Aktuell gewünschter<br>Raumtemperatur-<br>Sollwert|Read|INTEGER16|5419.n|Not Available|
|**1103**|varZoneTOutside 16 -9|varZoneTOutside 8-1|Kreis-Außentemperatur|Read|INTEGER16|542E.n|Not Available|
|**1104**|varZoneTRoom 16 -9|varZoneTRoom 8-1|Aktuelle Raumtemperatur<br>für den Kreis|Read|INTEGER16|5404.n|Not Available|
|**1105**|varZoneRoomTemperatureMeasured 16 -9|varZoneRoomTemperatureMeasured 8-1|Raumtemperaturmessung<br>mit hoher Auflösung für<br>die Regelung der<br>Raumtemperatur des<br>Kreismoduls|Read/Write|INTEGER16|5434.n|Not Available|
|**1106**||varZoneHdOnOffDemand|Ein/Aus Heizanforderung<br>aktiv<br>0: AUS|Read|ENUM8|5415.n|Not Available|
||||1: EIN|||||
|**1107**||varZoneCurrentActivities|Aktuelle Aktivität des<br>aktiven Kreises<br>0: Frostschutz<br>1: Reduziert<br>2: Komfort<br>3: Legionellenschutz|Read|ENUM8|5413.n|560F.n|
|**1108**||varZoneCurrentMode|Aktuelle Betriebsart des<br>Kreises<br>0: Zeitprogramm<br>1: Manuell<br>2: Frostschutz<br>3: Temporär<br>4: Ferien|Read|ENUM8|5410.n|560E.n|
|**1109**||varZoneCurrentHeatingMode|Aktueller Modus, in dem<br>der Kreis arbeitet.<br>0: Standby<br>1: Heizung<br>2: Kühlen|Read|ENUM8|541D.n|Not Available|
|**1110**||varZonePumpRunning|Läuft die Pumpe des<br>Kreises<br>0: NEIN<br>1: JA|Read|ENUM8|5406.n|5001.0|
|**1111**||varZoneMvdClosing|Mischventil geschlossen<br>1:ja 0: nein|Read|ENUM8|5402.n|Not Available|
|**1112**||varZoneMvdOpening|Mischventil offen 1: ja 0:<br>nein|Read|ENUM8|5403.n|Not Available|
|**1113**||varZoneSecondarySwimmingPoolpumpStatus|Status der<br>Sekundärpumpe für<br>Schwimmbad<br>0: AUS<br>1: EIN|Read|ENUM8|5437.n|Not Available|
|**1114**||varZoneElectricalBackupOutputStatus|Ausgangsstatus für<br>elektrischen<br>Zusatzerzeuger<br>0: AUS<br>1: EIN|Read|ENUM8|5438.n|Not Available|
|**1115**|varZoneCtrPumpRunHours 32-25|varZoneCtrPumpRunHours 24-17|Anzahl der Stunden, in<br>denen die Pumpe laufen<br>muss|Read|UNSIGNED32|541A.n|560D.0|
|**1116**|varZoneCtrPumpRunHours 16-9|varZoneCtrPumpRunHours 8-1|Anzahl der Stunden, in<br>denen die Pumpe laufen<br>muss|Read|UNSIGNED32|||
|**1117**|varZoneCtrPumpStarts 32-25|varZoneCtrPumpStarts 24-17|Anzahl der Pumpenstarts|Read|UNSIGNED32|541B.n|560A.0|
|**1118**|varZoneCtrPumpStarts 16-9|varZoneCtrPumpStarts 8-1|Anzahl der Pumpenstarts|Read|UNSIGNED32|||
|**1119**|varDhwTankTemperature 16-9|varDhwTankTemperature 8-1|Speichertemperatur<br>Warmwasserspeicher<br>(unterer Sensor)|Read|INTEGER16|5405.n|5601.0|
|**1120**|varDhwTankTemperatureTop 16-9|varDhwTankTemperatureTop 8-1|Speichertemperatur<br>Warmwasserspeicher<br>(oberer Sensor)|Read|INTEGER16|5433.n|5606.0|


## **10 Kaskade** 

|**Modbus**|**Daten**|**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.**<br>**SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**7000**||vaCascadeApplianceNumber|Gerätenummer in<br>Kaskade:<br>1: Master<br>3 - 254: Slave<br>255: nicht Teil einer<br>Kaskade|Read|UNSIGNED8|4008.2|
|**7001**||parCascadeMode|Betriebsart in Kaskade:<br>Automatik, Heizung,<br>Kühlen|Read/<br>Write|ENUM8|370E.0|
|**7002**||parCascadeType|Art der Kaskade:<br>TRADITIONELL oder<br>PARALLEL|Read/<br>Write|ENUM8|3706.0|
|**7003**||parCascadePermutation|Über diesen Parameter<br>wird der Führungskessel<br>bestimmt. 0: Der<br>Führungskessel wechselt<br>automatisch alle 7 Tage<br>Andere: Der<br>Führungskessel ist<br>immer der durch diesen<br>Wert definierte|Read/<br>Write|UNSIGNED8|3705.0|
|**7004**||parCascadeInterStageTime|Ein- und<br>Ausschaltverzögerung<br>der Erzeuger|Read/<br>Write|UNSIGNED8|3709.0|
|**7005**|parCascadeParallelHeatingOutsideTemperatureTrigge<br>r 16 -9|parCascadeParallelHeatingOutsideTemperatureTrigg<br>er 8 -1|Außentemperatur, ab<br>der alle Stufen im<br>Parallelbetrieb aktiviert<br>werden|Read/<br>Write|INTEGER16|3707.0|
|**7006**|parCascadeParallelCoolingOutsideTemperatureTrigge<br>r 16 -9|parCascadeParallelCoolingOutsideTemperatureTrigg<br>er 8 -1|Außentemperatur, ab<br>der alle Stufen im<br>Parallelbetrieb aktiviert<br>werden|Read/<br>Write|INTEGER16|370A.0|
|**7007**||parCascadePowerRiseTime|Anstiegszeit bis zum<br>Erreichen des Sollwerts|Read/<br>Write|UNSIGNED8|370C.0|
|**7008-**<br>**7099**|||||||
|||Für Zukunft reserviert|||||
|**7100**||varCascadeNumberProducerFirstStart|Aktive Nummer des<br>Herstellers|Read|UNSIGNED8|5700.0|
|**7101**|varProducerManagerSystemFlowTemperature 16 -9|varProducerManagerSystemFlowTemperature 8 -1|Vorlauftemperatur<br>Kaskade|Read|INTEGER16|5701.0|
|**7102**||varCascadeNumberProducersPresent|Anzahl der in der<br>Kaskade erkannten<br>Erzeuger|Read|UNSIGNED8|571C.0|
|**7103**||varCascadeNbStageAvailable|Anzahl der in der<br>Kaskade verfügbaren<br>Stufen|Read|UNSIGNED8|5716.0|
|**7104**||varCascadeNbStageRequired|Anzahl der in der<br>Kaskade erforderlichen<br>Stufen|Read|UNSIGNED8|5717.0|
|**7105**||varCascadeSystemPowerRequest Byte 1|Kaskaden-<br>Leistungsanforderung<br>durch den<br>Verbrauchermanager -<br>Leistung|Read|UNSIGNED8|571D.0|
|**7106**|varCascadeSystemPowerRequest Byte 3|varCascadeSystemPowerRequest Byte 2|Kaskaden-<br>Leistungsanforderung<br>durch den<br>Verbrauchermanager -<br>Temperatursollwert|Read|INTEGER16||
|**7107**||varCascadeSystemPowerRequest Byte 4|Kaskaden-<br>Leistungsanforderung<br>durch den<br>Verbrauchermanager -<br>HeizanforderungArt|Read|UNSIGNED8||
|**7108**||varCascadeSystemPowerSetpointCalculated Byte 1|Berechneter<br>Kaskadenleistungssollwe<br>rt - Leistung|Read|UNSIGNED8|571E.0|
|**7109**|varCascadeSystemPowerSetpointCalculated Byte 3|varCascadeSystemPowerSetpointCalculated Byte 2|Berechneter<br>Kaskadenleistungssollwe<br>rt - Temperatursollwert|Read|INTEGER16||
|**7110**||varCascadeSystemPowerSetpointCalculated Byte 4|Berechneter<br>Kaskadenleistungssollwe<br>rt - HeizanforderungArt|Read|ENUM8||
|**7111**||PowerActualReceived1|Aktuelle Leistung des<br>Gerätes 1|Read|UNSIGNED8|570B.1|
|**7112**|FlowTemperatureReceived1 16-9|FlowTemperatureReceived1 8-1|Gerät 1<br>Vorlauftemperatur|Read|INTEGER16|570C.1|
|**7113**|-|ProducerManagerStatusBitfieldReceived1|Gerät 1 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.1|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7114**|-|ProducerManagerRequestReceived1|Gerät 1 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.1|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7115**||PowerActualReceived3|Aktuelle Leistung des<br>Gerätes 3|Read|UNSIGNED8|570B.3|
|**7116**|FlowTemperatureReceived3 16-9|FlowTemperatureReceived3 8-1|Gerät 3<br>Vorlauftemperatur|Read|INTEGER16|570C.3|
|**7117**|-|ProducerManagerStatusBitfieldReceived3|Gerät 3 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.3|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7118**|-|ProducerManagerRequestReceived3|Gerät 3 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.3|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7119**||PowerActualReceived4|Aktuelle Leistung des<br>Gerätes 4|Read|UNSIGNED8|570B.4|
|**7120**|FlowTemperatureReceived4 16-9|FlowTemperatureReceived4 8-1|Gerät 4<br>Vorlauftemperatur|Read|INTEGER16|570C.4|
|**7121**|-|ProducerManagerStatusBitfieldReceived4|Gerät 4 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.4|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7122**|-|ProducerManagerRequestReceived4|Gerät 4 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.4|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7123**||PowerActualReceived5|Aktuelle Leistung des<br>Gerätes 5|Read|UNSIGNED8|570B.5|
|**7124**|FlowTemperatureReceived5 16-9|FlowTemperatureReceived5 8-1|Gerät 5<br>Vorlauftemperatur|Read|INTEGER16|570C.5|
|**7125**|-|ProducerManagerStatusBitfieldReceived5|Gerät 5 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.5|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7126**|-|ProducerManagerRequestReceived5|Gerät 5 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.5|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7127**||PowerActualReceived6|Aktuelle Leistung des<br>Gerätes 6|Read|UNSIGNED8|570B.6|
|**7128**|FlowTemperatureReceived6 16-9|FlowTemperatureReceived6 8-1|Gerät 6<br>Vorlauftemperatur|Read|INTEGER16|570C.6|
|**7129**|-|ProducerManagerStatusBitfieldReceived6|Gerät 6 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.6|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7130**|-|ProducerManagerRequestReceived6|Gerät 6 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.6|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7131**||PowerActualReceived7|Aktuelle Leistung des<br>Gerätes 7|Read|UNSIGNED8|570B.7|
|**7132**|FlowTemperatureReceived7 16-9|FlowTemperatureReceived7 8-1|Gerät 7<br>Vorlauftemperatur|Read|INTEGER16|570C.7|
|**7133**|-|ProducerManagerStatusBitfieldReceived7|Gerät 7 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.7|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7134**|-|ProducerManagerRequestReceived7|Gerät 7 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.7|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7135**||PowerActualReceived8|Aktuelle Leistung des<br>Gerätes 8|Read|UNSIGNED8|570B.8|
|**7136**|FlowTemperatureReceived8 16-9|FlowTemperatureReceived8 8-1|Gerät 8<br>Vorlauftemperatur|Read|INTEGER16|570C.8|
|**7137**|-|ProducerManagerStatusBitfieldReceived8|Gerät 8 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.8|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7138**|-|ProducerManagerRequestReceived8|Gerät 8 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.8|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7139**||PowerActualReceived9|Aktuelle Leistung des<br>Gerätes 9|Read|UNSIGNED8|570B.9|
|**7140**|FlowTemperatureReceived9 16-9|FlowTemperatureReceived9 8-1|Gerät 9<br>Vorlauftemperatur|Read|INTEGER16|570C.9|
|**7141**|-|ProducerManagerStatusBitfieldReceived9|Gerät 9 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.9|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7142**|-|ProducerManagerRequestReceived9|Gerät 9 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.9|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||
|**7143**||PowerActualReceived10|Aktuelle Leistung des<br>Gerätes 10|Read|UNSIGNED8|570B.10|
|**7144**|FlowTemperatureReceived10 16-9|FlowTemperatureReceived10 8-1|Gerät 10<br>Vorlauftemperatur|Read|INTEGER16|570C.10|
|**7145**|-|ProducerManagerStatusBitfieldReceived10|Gerät 10 Status<br>0 Pumpe aktiv|Read|UNSIGNED8|570d.10|
||||1 Leistungsmotor aktiv<br>(Brenner, Verdichter<br>oder Zusatzerzeuger)||||
||||2 TWW wird erzeugt||||
||||3 HZG möglich||||
||||4 TWW möglich||||
||||5 Kühlung möglich||||
||||6 Elektrisch möglich||||
||||7 Verriegelung<br>vorhanden||||
|**7146**|-|ProducerManagerRequestReceived10|Gerät 10 Spezielle<br>Anforderung<br>0 Frostschutz|Read|UNSIGNED8|570E.10|
||||1 Frostschutz nur Pumpe||||
||||2 Schornsteinfeger-<br>/Inbetriebnahmemodus||||
||||3 Wartungsanforderung||||


## **11 Pufferspeicher** 

|**Modbus**|**Daten**|**Daten**|**Beschreibung**|**Zugang**|**Anmerkung**|**Datenpunkte**<br>**index.**<br>**SubIndex**|
|---|---|---|---|---|---|---|
|**Adresse**|MSB|LSB|||||
|**7500**|parBufferHysteresis 16-9|parBufferHysteresis 8-1|Hysterese Beginn Pufferspeicherladung|Read/<br>Write|INTEGER16|350E.0|
|**7501**|parBufferHysteresisStopLoading 16-9|parBufferHysteresisStopLoading 8-1|Hysterese Ende Pufferspeicherladung|Read/<br>Write|INTEGER16|3513.0|
|**7502**||parBufferTankPumpPostRun|Minimale Nachlaufzeit der Pufferladepumpe|Read/<br>Write|ENUM8|350F.0|
|**7503**||parBufferControlStrategy|Verwendete Heiz-/Kühlstrategie mit<br>Pufferspeicher<br>0: Fester Sollwert<br>1: Berechneter Sollwert<br>2: Spezifische Steigung|Read/<br>Write|ENUM8|3502.0|
|**7504**|parBufferHeatingForcedSetpoint 16-9|parBufferHeatingForcedSetpoint 8-1|Fester Pufferspeichersollwert im Heizbetrieb|Read/<br>Write|UNSIGNED1<br>6|3503.0|
|**7505**|parBufferCoolingForcedSetpoint 16-9|parBufferCoolingForcedSetpoint 8-1|Fester Pufferspeichersollwert im Kühlbetrieb|Read/<br>Write|UNSIGNED1<br>6|3504.0|
|**7506**||parBufferSlope|Pufferspeicher Steigung|Read/<br>Write|UNSIGNED1<br>6|3505.0|
|**7507**|parBufferOffset 16-9|parBufferOffset 8-1|Zur Berechnung des Sollwerts hinzuzufügende<br>Verschiebung|Read/<br>Write|UNSIGNED1<br>6|350D.0|
|**7508**|parBufferTimeProgramMonday1 Byte 0|parBufferTimeProgramMonday1 Byte 1|Zeitprogramm Pufferspeicher|Read/<br>Write|OCTET_STRI<br>NG|3506.0|
|**7509**|parBufferTimeProgramMonday1 Byte 2|parBufferTimeProgramMonday1 Byte 3|||||
|**7510**|parBufferTimeProgramMonday1 Byte 4|parBufferTimeProgramMonday1 Byte 5|||||
|**7511**|parBufferTimeProgramMonday1 Byte 6|parBufferTimeProgramMonday1 Byte 7|||||
|**7512**|parBufferTimeProgramMonday1 Byte 8|parBufferTimeProgramMonday1 Byte 9|||||
|**7513**|parBufferTimeProgramMonday1 Byte<br>10|parBufferTimeProgramMonday1 Byte<br>11|||||
|**7514**|parBufferTimeProgramMonday1 Byte<br>12|parBufferTimeProgramMonday1 Byte<br>13|||||
|**7515**|parBufferTimeProgramMonday1 Byte<br>14|parBufferTimeProgramMonday1 Byte<br>15|||||
|**7516**|parBufferTimeProgramMonday1 Byte<br>16|parBufferTimeProgramMonday1 Byte<br>17|||||
|**7517**|parBufferTimeProgramMonday1 Byte<br>18||||||
|**7518**|parBufferTimeProgramTuesday1 Byte 0|parBufferTimeProgramTuesday1 Byte 1||Read/<br>Write|OCTET_STRI<br>NG|3507.0|
|**7519**|parBufferTimeProgramTuesday1 Byte 2|parBufferTimeProgramTuesday1 Byte 3|||||
|**7520**|parBufferTimeProgramTuesday1 Byte 4|parBufferTimeProgramTuesday1 Byte 5|||||
|**7521**|parBufferTimeProgramTuesday1 Byte 6|parBufferTimeProgramTuesday1 Byte 7|||||
|**7522**|parBufferTimeProgramTuesday1 Byte 8|parBufferTimeProgramTuesday1 Byte 9|||||
|**7523**|parBufferTimeProgramTuesday1 Byte<br>10|parBufferTimeProgramTuesday1 Byte<br>11|||||
|**7524**|parBufferTimeProgramTuesday1 Byte<br>12|parBufferTimeProgramTuesday1 Byte<br>13|||||
|**7525**|parBufferTimeProgramTuesday1 Byte<br>14|parBufferTimeProgramTuesday1 Byte<br>15|||||
|**7526**|parBufferTimeProgramTuesday1 Byte<br>16|parBufferTimeProgramTuesday1 Byte<br>17|||||
|**7527**|parBufferTimeProgramTuesday1 Byte<br>18||||||
|**7528**|parBufferTimeProgramWednesday1<br>Byte 0|parBufferTimeProgramWednesday1<br>Byte 1||Read/<br>Write|OCTET_STRI<br>NG|3508.0|
|**7529**|parBufferTimeProgramWednesday1<br>Byte 2|parBufferTimeProgramWednesday1<br>Byte 3|||||
|**7530**|parBufferTimeProgramWednesday1<br>Byte 4|parBufferTimeProgramWednesday1<br>Byte 5|||||
|**7531**|parBufferTimeProgramWednesday1<br>Byte 6|parBufferTimeProgramWednesday1<br>Byte 7|||||
|**7532**|parBufferTimeProgramWednesday1<br>Byte 8|parBufferTimeProgramWednesday1<br>Byte 9|||||
|**7533**|parBufferTimeProgramWednesday1<br>Byte 10|parBufferTimeProgramWednesday1<br>Byte 11|||||
|**7534**|parBufferTimeProgramWednesday1<br>Byte 12|parBufferTimeProgramWednesday1<br>Byte 13|||||
|**7535**|parBufferTimeProgramWednesday1<br>Byte 14|parBufferTimeProgramWednesday1<br>Byte 15|||||
|**7536**|parBufferTimeProgramWednesday1<br>Byte 16|parBufferTimeProgramWednesday1<br>Byte 17|||||
|**7537**|parBufferTimeProgramWednesday1<br>Byte 18||||||
|**7538**|parBufferTimeProgramThursday1 Byte<br>0|parBufferTimeProgramThursday1 Byte<br>1||Read/|OCTET_STRI<br>NG|3509.0|
|**7539**|parBufferTimeProgramThursday1 Byte<br>2|parBufferTimeProgramThursday1 Byte<br>3|||||
|**7540**|parBufferTimeProgramThursday1 Byte<br>4|parBufferTimeProgramThursday1 Byte<br>5|||||
|**7541**|parBufferTimeProgramThursday1 Byte<br>6|parBufferTimeProgramThursday1 Byte<br>7|||||
|**7542**|parBufferTimeProgramThursday1 Byte<br>8|parBufferTimeProgramThursday1 Byte<br>9|||||
|**7543**|parBufferTimeProgramThursday1 Byte<br>10|parBufferTimeProgramThursday1 Byte||Write|||
|||11|||||
|**7544**|parBufferTimeProgramThursday1 Byte<br>12|parBufferTimeProgramThursday1 Byte<br>13|||||
|**7545**|parBufferTimeProgramThursday1 Byte<br>14|parBufferTimeProgramThursday1 Byte<br>15|||||
|**7546**|parBufferTimeProgramThursday1 Byte<br>16|parBufferTimeProgramThursday1 Byte<br>17|||||
|**7547**|parBufferTimeProgramThursday1 Byte<br>18||||||
|**7548**|parBufferTimeProgramFriday1 Byte 0|parBufferTimeProgramFriday1 Byte 1||Read/<br>Write|OCTET_STRI<br>NG|350A.0|
|**7549**|parBufferTimeProgramFriday1 Byte 2|parBufferTimeProgramFriday1 Byte 3|||||
|**7550**|parBufferTimeProgramFriday1 Byte 4|parBufferTimeProgramFriday1 Byte 5|||||
|**7551**|parBufferTimeProgramFriday1 Byte 6|parBufferTimeProgramFriday1 Byte 7|||||
|**7552**|parBufferTimeProgramFriday1 Byte 8|parBufferTimeProgramFriday1 Byte 9|||||
|**7553**|parBufferTimeProgramFriday1 Byte 10|parBufferTimeProgramFriday1 Byte 11|||||
|**7554**|parBufferTimeProgramFriday1 Byte 12|parBufferTimeProgramFriday1 Byte 13|||||
|**7555**|parBufferTimeProgramFriday1 Byte 14|parBufferTimeProgramFriday1 Byte 15|||||
|**7556**|parBufferTimeProgramFriday1 Byte 16|parBufferTimeProgramFriday1 Byte 17|||||
|**7557**|parBufferTimeProgramFriday1 Byte 18||||||
|**7558**|parBufferTimeProgramSaturday1 Byte 0|parBufferTimeProgramSaturday1 Byte 1||Read/<br>Write|OCTET_STRI<br>NG|350B.0|
|**7559**|parBufferTimeProgramSaturday1 Byte 2|parBufferTimeProgramSaturday1 Byte 3|||||
|**7560**|parBufferTimeProgramSaturday1 Byte 4|parBufferTimeProgramSaturday1 Byte 5|||||
|**7561**|parBufferTimeProgramSaturday1 Byte 6|parBufferTimeProgramSaturday1 Byte 7|||||
|**7562**|parBufferTimeProgramSaturday1 Byte 8|parBufferTimeProgramSaturday1 Byte 9|||||
|**7563**|parBufferTimeProgramSaturday1 Byte<br>10|parBufferTimeProgramSaturday1 Byte<br>11|||||
|**7564**|parBufferTimeProgramSaturday1 Byte<br>12|parBufferTimeProgramSaturday1 Byte<br>13|||||
|**7565**|parBufferTimeProgramSaturday1 Byte<br>14|parBufferTimeProgramSaturday1 Byte<br>15|||||
|**7566**|parBufferTimeProgramSaturday1 Byte<br>16|parBufferTimeProgramSaturday1 Byte<br>17|||||
|**7567**|parBufferTimeProgramSaturday1 Byte<br>18||||||
|**7568**|parBufferTimeProgramSunday1 Byte 0|parBufferTimeProgramSunday1 Byte 1||Read/<br>Write|OCTET_STRI<br>NG|350C.0|
|**7569**|parBufferTimeProgramSunday1 Byte 2|parBufferTimeProgramSunday1 Byte 3|||||
|**7570**|parBufferTimeProgramSunday1 Byte 4|parBufferTimeProgramSunday1 Byte 5|||||
|**7571**|parBufferTimeProgramSunday1 Byte 6|parBufferTimeProgramSunday1 Byte 7|||||
|**7572**|parBufferTimeProgramSunday1 Byte 8|parBufferTimeProgramSunday1 Byte 9|||||
|**7573**|parBufferTimeProgramSunday1 Byte 10|parBufferTimeProgramSunday1 Byte 11|||||
|**7574**|parBufferTimeProgramSunday1 Byte 12|parBufferTimeProgramSunday1 Byte 13|||||
|**7575**|parBufferTimeProgramSunday1 Byte 14|parBufferTimeProgramSunday1 Byte 15|||||
|**7576**|parBufferTimeProgramSunday1 Byte 16|parBufferTimeProgramSunday1 Byte 17|||||
|**7577**|parBufferTimeProgramSunday1 Byte 18||||||
|**7578 -**<br>**7599**|||||||
|||Für Zukunft reserviert|||||
|**7600**|varBufferTankTemperature1 16 -9|varBufferTankTemperature1 8 -1|Gemessene Pufferspeichertemperatur unten|Read|INTEGER16|5501.1|
|**7601**|varBufferTankTemperature2 16 -9|varBufferTankTemperature2 8 -1|Gemessene Pufferspeichertemperatur oben|Read|INTEGER16|5501.2|
|**7602**||varBufferTankPumpState|Status Pufferspeicherpumpe (AUS/EIN)|Read|ENUM8|5508.0|
|**7603**||varBufferMode|Betriebsart Pufferspeicher<br>0: Trennspeicher<br>1: Wasserspeicher|Read|ENUM8|5515.0|
|**7604**||varBufferWinningHeatDemandRequest<br>Byte 1|Pufferspeicheranforderung Wärmegewinnung: die<br>von den nach dem Pufferspeicher<br>angeschlossenen Kreisen angeforderte<br>Wärmegewinnung- Leistung|Read|UNSIGNED8|5517.0|
|**7605**|varBufferWinningHeatDemandRequest<br>Byte 3|varBufferWinningHeatDemandRequest<br>Byte 2|Pufferspeicheranforderung Wärmegewinnung: die<br>von den nach dem Pufferspeicher<br>angeschlossenen Kreisen angeforderte<br>Wärmegewinnung - Temperatursollwert|Read|INTEGER16||
|**7606**||varBufferWinningHeatDemandRequest<br>Byte 4|Pufferspeicheranforderung Wärmegewinnung: die<br>von den nach dem Pufferspeicher<br>angeschlossenen Kreisen angeforderte<br>Wärmegewinnung - WärmeanforderungArt|Read|UNSIGNED8||


## © Copyright 

Alle technischen und technologischen Informationen in diesen technischen Anweisungen sowie alle Zeichnungen und technischen Beschreibungen bleiben unser Eigentum und dürfen ohne vorherige schriftliche Zustimmung nicht vervielfältigt werden. Änderungen vorbehalten. 

7740782 - v01 - 26072019 

7740782-001-01 

