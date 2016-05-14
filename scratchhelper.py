from flask import Flask
from flask import request
from flask import render_template
from socket import gethostname
from threading import Thread

from time import sleep


app = Flask(__name__)

busyId = -1

@app.route('/poll')
def poll():
  global busyId
  ret = "ok 0"
  
  if busyId > -1:
    ret = "_busy " + str(busyId)

  return ret
  
@app.route('/move/<wheel>/<speed>')
def move(wheel, speed):
  return "_result 0"

@app.route('/stop/<wheel>')
def stop(wheel):
  return "_result 0"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', threaded=True)
