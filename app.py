from guizero import App, Text
import picamera
from time import sleep

app = App(title="Hello world")

welcome_message = Text(app, text="PrevenBox", size=40, font="Times New Roman", color="Red")

camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.start_preview()

camera.brightness = 70

camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()


app.display()