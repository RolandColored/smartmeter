try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_rpi.RPi import GPIO


def setup_gas_sensor():
    gas_sensor_pin = 7

    def gas_callback(_):
        if GPIO.input(gas_sensor_pin) == 1:
            print('check')

    # Use physical pin numbering
    GPIO.setmode(GPIO.BOARD)
    # Set pin SensorPin to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(gas_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(gas_sensor_pin, GPIO.RISING, callback=gas_callback)


def cleanup_gas_sensor():
    GPIO.cleanup()

