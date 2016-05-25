from flask import Flask
from flask import request
from flask import render_template
from socket import gethostname
from threading import Thread

from time import sleep
import urllib2


app = Flask(__name__)

busyId = -1

@app.route('/poll')
def poll():
  global busyId
  ret = "ok 0"
  
  if busyId > -1:
    ret = "_busy " + str(busyId)

  print(ret)
  return ret
  
#  127.0.0.1 - - [14/May/2016 10:45:13] "GET /move/9/both/forward/6/fast HTTP/1.1" 404 -

@app.route('/move/<id>/<wheel>/<direction>/<time>/<speed>')
def move(id, wheel, direction, time, speed):
  global busyId
  busyId = id
  res = urllib2.urlopen('http://192.168.1.68:5000/move/' + wheel + '/' + direction + '/' + time + '/' + speed)
  busyId = -1

  print(res)
  return res

@app.route('/turn/<id>/<turndirection>/<time>/<speed>')
def turn(id, turndirection, time, speed):
  global busyId
  busyId = id
  urllib2.urlopen('http://192.168.1.68:5000/turn/' + turndirection + '/' + time + '/' + speed)
  busyId = -1

  return "_result 0"

@app.route('/stop/<wheel>')
def stop(wheel):
  urllib2.urlopen('http://192.168.1.68:5000/stop/' + wheel)
  return "_result 0"

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', threaded=True)
