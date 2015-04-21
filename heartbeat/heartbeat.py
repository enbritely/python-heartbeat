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
      self.wfile.write('\n')
      now = datetime.datetime.now()
      uptime = str(now - starting_time)
      obj = {'status': 'running', 'build': git_sha.git_sha, 'uptime': uptime}
      json.dump(obj, self.wfile)
      self.wfile.write("\n")

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

