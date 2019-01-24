import datetime
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_rpi.RPi import GPIO


def setup_gas_sensor(file_handle):
    gas_sensor_pin = 7

    def gas_callback(_):
        if GPIO.input(gas_sensor_pin) == 1:
            file_handle.write(str(datetime.datetime.now())+',0.01\n')
            file_handle.flush()

    # Use physical pin numbering
    GPIO.setmode(GPIO.BOARD)
    # Set pin SensorPin to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(gas_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(gas_sensor_pin, GPIO.RISING, callback=gas_callback)


if __name__ == '__main__':
    with open('gas.csv', 'a') as fh:
        setup_gas_sensor(fh)

        try:
            while True:
                # don't let script exit
                time.sleep(1)
        finally:
            print('Cleaning up')
            GPIO.cleanup()
