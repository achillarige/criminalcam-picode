import threading
import requests
import subprocess
import picamera
import base64
import time
import json

ip = "64.165.34.2"
url = "https://criminalcam-nihaleg.c9users.io/upload"


def sendImage():
  takePic()
  getLocation()
  r = requests.post(url,{"image":convertImageToBase64(),"latitude":getLocation()["latitude"],"longitude":getLocation()["longitude"]})

def takePic():
  camera = picamera.PiCamera()
  try:
   camera.start_preview()
   time.sleep(1)
   camera.capture('image_test.jpg', resize=(500,281))
   camera.stop_preview()
   pass
  finally:
   camera.close()

def convertImageToBase64():
 with open("image_test.jpg", "rb") as image_file:
   encoded = base64.b64encode(image_file.read())
   return encoded

def getLocation():
  send_url = "http://freegeoip.net/json/"
  return json.loads(requests.get(send_url).text)

while True:
  sendImage()
