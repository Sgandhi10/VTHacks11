import RPi.GPIO as GPIO
import time
from grove_rgb_lcd import *


setText("Hello World")
time.sleep(100)

while (True):
    setText("Hello World")
    setRGB(0,128,64)
    for c in range(0,255):
        setRGB(c,255-c,0)
        time.sleep(0.01)
    setRGB(0,255,0)
    setText("Bye bye")
    time.sleep(1.5)

BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:

    while True:
        time.sleep(0.1)
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button is pressed")

        else:
            print("Button is not pressed")
except KeyboardInterrupt:
    GPIO.cleanup()


