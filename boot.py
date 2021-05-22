from machine import Pin, I2C
i2c = I2C(scl=Pin(22), sda=Pin(21))
i2c.writeto_mem(0x35, 0x33, b"\xC0")
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#import test

