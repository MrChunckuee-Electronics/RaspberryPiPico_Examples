# Library and information by
# Mike Causer - https://github.com/mcauser/micropython-max7219

'''
Connections:
MAX7219    Pico Name   Pico GPIO   Pico PIN#
VCC        VBUS                    40
GND        GND                     38
CS         SPI0 CSn    GP5         7
CLK        SPI0 SCK    GP6         9
DIN        SPI0 TX     GP7         10
'''

import max7219
from machine import Pin, SPI
from time import sleep

num_display = 4

cs_pin = Pin(5, Pin.OUT)

spi = SPI(0)

display = max7219.Matrix8x8(spi, cs_pin, num_display)

while True:
    display.fill(0)
    display.text('1234',0,1,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('abcd',0,1,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('WXYZ',0,1,1)
    display.show()
    sleep(3)
    
    display.fill(0)
    display.text('*#+?',0,1,1)
    display.show()
    sleep(3)
    

    
    


