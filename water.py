from time import sleep

try:
    from picamera import PiCamera
except ImportError:
    from fake_rpi.picamera import PiCamera

camera = PiCamera(resolution=(2592, 1944))

# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
