from time import sleep
from machine import Pin

print("blink LED on board using delays")
print("@MrChunckuee - mrchunckuee.blogspot.com")

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    sleep(0.5)
#     led.high()
#     sleep(0.5)
#     led.low()
#     sleep(0.5)