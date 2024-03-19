from machine import Pin
from time import sleep

from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/speedaddict/esp32-blink-ota/main/"
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "code.py")
ota_updater.download_and_install_update_if_available()

led = Pin(2, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(.1)
