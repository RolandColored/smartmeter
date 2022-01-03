from sensor import Sensor

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_rpi.RPi import GPIO


class SensorGas(Sensor):
    def __init__(self):
        super().__init__()
        self.name = 'gas'

    def setup_gas_sensor(self):
        gas_sensor_pin = 7

        def gas_callback(_):
            if GPIO.input(gas_sensor_pin) == 1:
                self.counter += 1

        # Use physical pin numbering
        GPIO.setmode(GPIO.BOARD)
        # Set pin SensorPin to be an input pin and set initial value to be pulled low (off)
        GPIO.setup(gas_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(gas_sensor_pin, GPIO.RISING, callback=gas_callback)

    def cleanup(self) -> None:
        GPIO.cleanup()

