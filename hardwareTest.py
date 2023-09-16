import RPi.GPIO as GPIO
import time

BUTTON_PIN = 27
GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.1)
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
         print("Button is pressed")

    else:
         print("Button is not pressed")


