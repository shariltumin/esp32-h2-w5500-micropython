# No Wifi and ESPNOW
freeze("$(PORT_DIR)/modules", ("_boot.py", "flashbdev.py", "inisetup.py", "machine.py"), opt=3)

include("$(MPY_DIR)/extmod/asyncio", opt=3)

# Useful networking-related packages.
require("bundle-networking", opt=3)

# Require some micropython-lib modules.
require("aioespnow", opt=3)
require("dht", opt=3)
require("ds18x20", opt=3)
require("neopixel", opt=3)
require("onewire", opt=3)
require("umqtt.robust", opt=3)
require("umqtt.simple", opt=3)
require("upysh", opt=3)
