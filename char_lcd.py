#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4

# Button Pressing
button_signal = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# BeagleBone Black configuration:
# lcd_rs        = 'P8_8'
# lcd_en        = 'P8_10'
# lcd_d4        = 'P8_18'
# lcd_d5        = 'P8_16'
# lcd_d6        = 'P8_14'
# lcd_d7        = 'P8_12'
# lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight, button_signal)

# Making the cursor hidden and not allowing any blink
lcd.show_cursor(False)
lcd.blink(False)
lcd.clear()

def buttonPressed():
    return GPIO.input(button_signal) == GPIO.HIGH


def displayData(_time, _cap):
    print("Button is pressed")

    # Clear the screen for resets
    lcd.clear()
      
    # Print Bus Stop Detials
    lcd.message('TOMS CREEK\nSTOP:1313')

    # Wait 2.5 Seconds
    time.sleep(2.5)

    # Clear the screen.
    lcd.clear()
    # Print Bus Time Details and Capacity
    lcd.message('ETA: ')
    lcd.message(_time)
    lcd.message('\n')
    lcd.message('Capacity: ')
    lcd.message(_cap)

    time.sleep(2.5)

    lcd.clear()
    lcd.message('Goodbye!')
    time.sleep(1.5)
    lcd.clear()
    # Turn backlight on.
    lcd.set_backlight(1)

    lcd.set_cursor(0,0)
    BUS_IMG1 = '/ [][][][][]{ }|'
    BUS_IMG2 = '|_()__VT__(){ }/'
    lcd.message("")
    for i in range(16):
        printStr = BUS_IMG1[16-i-1:] + '\n' + BUS_IMG2[16-i-1:]
        lcd.clear()
        lcd.message(printStr)
        time.sleep(0.25)

    for i in range(16):
        printStr = " " * i + BUS_IMG1[:16-i] + '\n' + " " * i + BUS_IMG2[:16-i]
        lcd.clear()
        lcd.message(printStr)
        time.sleep(0.25)

