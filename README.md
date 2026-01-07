# MicroPython ESP32-H2-MINI-1 Firmware  
**Ethernet + ADC for ESP32-H2**

## File Structure
```
esp32-h2-w5500-micropython
├── boards
│   └── ESP32_H2_STD
│       ├── manifest.py
│       ├── mpconfigboard.cmake
│       ├── mpconfigboard.h
│       └── sdkconfig.board
├── build-ESP32_H2_STD
│   ├── firmware.bin
│   └── sdkconfig
├── esp32_common.cmake-STD-H2
├── log
│   ├── start_lan.txt
│   ├── sysinfo.txt
│   └── test_adc.txt
├── machine_adc.c-STD-H2
├── machine_pin.h-STD-H2
├── mpb_esp32h2_mini1.sh
├── mpconfigport.h-STD-H2
├── README.md
└── scripts
    ├── start_lan.py
    ├── sysinfo.py
    └── test_adc.py

```

To build MicroPython firmware, just run
```bash
./mpb_esp32h2_mini1.sh
```
This will **patch** some files and run `make`.

You need to change:
```
export IDF_PATH="$HOME/disk/esp/esp-idf-551"
```
to where you have installed your "ESP-IDF"

Production-ready MicroPython firmware for **ESP32-H2-MINI-1** with:
- ✅ **W5500 100Mbps Ethernet** (SPI)
- ✅ **5x 12-bit ADC channels** (GPIO0-4) 
- ✅ **10x GPIO** (GPIO0-5,8-11)
- ✅ **Full TCP/MQTT/HTTP stack**
- ✅ **No WiFi bloat** (Ethernet-only)

## Features

| Feature | Status | Pins |
|:--------|:-------|:-----|
| W5500 Ethernet | ✅ 100Mbps | GPIO4(SCLK),5(MOSI),0(MISO),1(CS),11(INT) |
| ADC (12-bit) | ✅ 5 channels | GPIO0-4 |
| GPIO Digital | ✅ 10 pins | GPIO0-5,8-11 |
| UART | ✅ | GPIO10(TX),11(RX) |
| SPI | ✅ | GPIO0-5 |
| I2C | ✅ | GPIO8-9 available |

## 🚨 Hardware Limitations Fixed
```
❌ GPIO6-7,15-21: SPI Flash (locked)
❌ GPIO5 ADC: Hardware limitation (fixed mapping)
❌ WiFi: No WiFi
❌ machine.ADC(): Guru crash (custom table fix)
```

## Quick Start

### 1. Flash Firmware
```bash
git clone https://github.com/shariltumin/esp32h2-mini1-micropython
cd build-ESP32_H2_STD
esptool --chip esp32h2 --port /dev/ttyACM0 erase_flash
esptool --chip esp32h2 --port /dev/ttyACM0 write_flash -z 0x0 firmware.bin
```

You need the latest version of esptool (>=5.1.0)

### 2. W5500 Wiring
```
H2-MINI-1    W5500 Module
-----------  ------------
IO4(G4)   →  SCLK
IO5(G5)   →  MOSI  
IO0(G0)   →  MISO
IO8(G1)   →  CS
IO9(G11)  →  INT
3V3       →  3.3V
GND       →  GND
```

### 3. Test Ethernet + ADC

#### ADC
Run `scripts/test_adc.py`

#### Ethernet
Run `scripts/start_lan.py`

#### Run log
See `log/`

## 🛠 Critical Fixes Applied

### 1. GPIO Mapping (`machine_pin.h`)
```c
#elif CONFIG_IDF_TARGET_ESP32H2
#define MICROPY_HW_ENABLE_GPIO0  (1)
#define MICROPY_HW_ENABLE_GPIO1  (1)
// ... GPIO0-5,8-11 enabled
```

### 2. ADC Table (`machine_adc.c`)
```c
#elif CONFIG_IDF_TARGET_ESP32H2
    {{&machine_adc_type}, ADCBLOCK1, ADC_CHANNEL_0, GPIO_NUM_0},
    // GPIO0-4 → ADC1_CH0-4 (5 channels)
```

### 3. Ethernet-only (`mpconfigport.h`)
```c
#define MICROPY_PY_MACHINE_ADC    (1)  // Fixed!
#define MICROPY_PY_NETWORK_WLAN   (0)  // Clean
```

### 4. Peripherals

#### UART
```python
>>> uart = machine.UART(1)
>>> uart
UART(1, baudrate=115211, bits=8, parity=None, stop=1, tx=10, rx=9, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=0, timeout_char=0, irq=0)
```

#### SPI
```python
>>> spi = machine.SPI(1)
>>> spi
SPI(id=1, baudrate=500000, polarity=0, phase=0, bits=8, firstbit=0, sck=4, mosi=5, miso=0)
```

#### I2C
```python
>>> i2c = machine.I2C(1)
>>> i2c
I2C(1, scl=9, sda=8, freq=400000, timeout=50000)
```

## Communication

### Lan W5500

```python
from machine import Pin, SPI
import network

# Ethernet
spi = SPI(1, sck=Pin(4), mosi=Pin(5), miso=Pin(0))
lan = network.LAN(spi=spi, cs=Pin(1), int=Pin(11), phy_addr=1, phy_type=network.PHY_W5500)
lan.active(True)
```

### Bluetooth BLE

```bash
>>> ble = bluetooth.BLE()
>>> ble.
active          config          gap_advertise   gap_connect
gap_disconnect  gap_pair        gap_passkey     gap_scan
gattc_discover_characteristics  gattc_discover_descriptors
gattc_discover_services         gattc_exchange_mtu
gattc_read      gattc_write     gatts_indicate  gatts_notify
gatts_read      gatts_register_services         gatts_set_buffer
gatts_write     irq
```
## Production Applications

```
🏭 Factory Sensor Gateway
- 5x Analog Sensors → Ethernet → Cloud
- 100Mbps MQTT publishing
- 368KB RAM for buffers

🔥 Industrial Monitoring
- Temperature/Pressure/Voltage
- W5500 reliability > WiFi (not aviable)

💡 Smart Building
- Ethernet backbone + analog room sensors
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `invalid pin` | Use GPIO0-5,8-11 only |
| ADC Guru crash | Fixed by `machine_adc.c` table |
| No Ethernet | Check W5500 wiring (IO4/5/0/1/11), phy_addr=1, phy_type=network.PHY_W5500 |
| WiFi STAT_* | Cosmetic - Ethernet works fine |

## License

MIT License 

