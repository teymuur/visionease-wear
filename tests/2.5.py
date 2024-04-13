from picamera2 import Picamera2 as PiCamera, Preview
import time
camera = PiCamera()
camera_config = camera.create_still_configuration(main={"size":(1920,1080)}, lores={"size":(640,580)})
camera.configure(camera_config)
camera.start_preview(Preview.DRM)
camera.start()
time.sleep(2)
camera.capture_file("test2.jpg")
print("done")







