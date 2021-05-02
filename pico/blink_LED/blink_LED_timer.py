from machine import Pin, Timer

print("blink LED on board using timer")
print("@MrChunckuee - mrchunckuee.blogspot.com")

led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)