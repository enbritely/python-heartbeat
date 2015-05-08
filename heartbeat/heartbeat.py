import sys

if sys.version > '3':
  from http.server import HTTPServer
  from http.server import BaseHTTPRequestHandler
else:
  from BaseHTTPServer import HTTPServer
  from BaseHTTPServer import BaseHTTPRequestHandler

import json
import threading
import datetime

import git_sha

global starting_time
starting_time = None

class HeartbeatRequestHandler(BaseHTTPRequestHandler):
  def do_GET(self) :
    global starting_time
    if self.path == '/heartbeat' :
      self.send_response(200)
      self.send_header('Content-type:', 'text/html')
      now = datetime.datetime.now()
      uptime = str(now - starting_time)
      obj = {'status': 'running', 'build': git_sha.git_sha, 'uptime': uptime}
      self.wfile.write(('\n' + json.dumps(obj) + "\n").encode('utf-8'))

def run_heartbeat_service(port, addr=''):
  global starting_time
  starting_time = datetime.datetime.now()
  class HeartbeatServer(threading.Thread):
    def run(self):
      httpd = HTTPServer((addr, port), HeartbeatRequestHandler)
      httpd.serve_forever()
  t = HeartbeatServer()
  t.daemon = True
  t.start()

