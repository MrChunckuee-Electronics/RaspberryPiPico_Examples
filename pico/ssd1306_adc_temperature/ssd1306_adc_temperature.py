 # Display Image & text on I2C driven ssd1306 OLED display
from machine import Pin, Timer, I2C, ADC
from ssd1306 import SSD1306_I2C
from time import sleep
import framebuf

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 /(65535)

led = Pin(25, Pin.OUT)
timer = Timer()

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c = I2C(0)                                            # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display


# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 96, 0)

# Add some text
oled.text("Raspberry Pi",5,5)
oled.text("Pico",5,15)
oled.text("Testing ADC",5,25)
oled.text("by MrChunckuee",5,35)

# Finally update the oled display so the image & text is displayed
oled.show()

#Toggle LED on board using timer
def blink(timer):
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    
    # The temperature sensor measures the Vbe voltage of a biased
    # bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope
    # of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    
    oled.fill_rect(44, 44, 72, 9, 0) # fill_rect(x-init, y-init, width, height, opts)
    # Only print two decimal
    oled.text(str("TEMP: {:.2f}".format(float(temperature))) + "C",5,45)
    print("Temperatura interna del RP2040 = {:.2f}".format(temperature) + " C")
    
    oled.show()
    sleep(5)