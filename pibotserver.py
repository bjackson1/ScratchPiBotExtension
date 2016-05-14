from flask import Flask
from flask import request
from flask import render_template
from socket import gethostname
from threading import Thread

from time import sleep
import RPi.GPIO as GPIO





class gpiocontrol:

    def __init__(self, pin):
        self.pin = int(pin)
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin, gpio.OUT)

    # def get(self):
    #   return gpio.input(self.pin)

    def set(self, state):
        gpio.output(self.pin, state)



app = Flask(__name__)

busyId = -1
leftForwardControl = gpiocontrol(24)
rightForwardControl = gpiocontrol(19)

@app.route('/poll')
def poll():
  global busyId
  ret = "ok 0"
  
  if busyId > -1:
    ret = "_busy " + str(busyId)

  return ret
  
@app.route('/move/<wheel>/<speed>')
def move(wheel, speed):
  if wheel == "left":
    leftForwardControl.set(True)

  return "_result 0"

@app.route('/stop/<wheel>')
def stop(wheel):
  if wheel == "left":
    leftForwardControl.set(False)

  return "_result 0"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', threaded=True)




