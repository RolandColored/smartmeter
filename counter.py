import RPi.GPIO as GPIO
import datetime
import time

SensorPin = 7


def button_callback(channel):
    if GPIO.input(SensorPin) == 1:
        print(datetime.datetime.now())


# Use physical pin numbering
GPIO.setmode(GPIO.BOARD)
# Set pin SensorPin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(SensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(SensorPin, GPIO.RISING, callback=button_callback)

while True:
    # don't let script exit
    time.sleep(1)

GPIO.cleanup()  # Clean up
