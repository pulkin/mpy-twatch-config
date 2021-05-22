from machine import Pin, I2C
I2C(scl=Pin(22), sda=Pin(21)).writeto_mem(0x35, 0x33, b"\xC0")
del Pin, I2C
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#import test

