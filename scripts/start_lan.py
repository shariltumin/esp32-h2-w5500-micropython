# boot.py
from machine import Pin, SPI
import network
import time

# Ethernet
spi = SPI(1, sck=Pin(4), mosi=Pin(5), miso=Pin(0))
# note: RGB LED at GPIO8 , UART TX at GPIO10
lan = network.LAN(spi=spi, cs=Pin(1), int=Pin(11), phy_addr=1, phy_type=network.PHY_W5500)
lan.active(True)
time.sleep(5)
print("IP:", lan.ifconfig())



