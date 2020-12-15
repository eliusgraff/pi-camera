#here is the start right here
import io
import time
import picamera

my_stream = io.BytesIO()

with picamera.PiCamera() as camera:
	camera.resolution = (640,480)
	camera.framerate = 10
	camera.start_preview()
	camera.capture(my_stream, 'jpeg')
	time.sleep(10)
	camera.stop_preview()

my_stream.close()
