// This configuration is for a generic ESP32C6 board with 4MiB (or more) of flash.

#define MICROPY_HW_BOARD_NAME               "ESP32H2 Mini-1 STD"
#define MICROPY_HW_MCU_NAME                 "ESP32H2"

#define MICROPY_PY_ESPNOW		    (0)

#define MICROPY_PY_NETWORK_HOSTNAME_DEFAULT "mpy-esp32h2"

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL         (0)

