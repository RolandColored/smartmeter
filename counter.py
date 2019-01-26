import datetime
import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    from fake_rpi.RPi import GPIO
try:
    from picamera import PiCamera
except ImportError:
    from fake_rpi.picamera import PiCamera


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


def capture_water_images():
    camera = PiCamera(resolution=(2592, 1944))

    # Camera warm-up time
    time.sleep(2)

    for filename in camera.capture_continuous('../data/water/{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
        print('Captured %s' % filename)
        time.sleep(600)


if __name__ == '__main__':
    with open('../data/gas.csv', 'a') as fh:
        setup_gas_sensor(fh)

        try:
            capture_water_images()
        finally:
            print('Cleaning up')
            GPIO.cleanup()
