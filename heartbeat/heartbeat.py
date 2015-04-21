from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import json
import threading

import git_sha

class HeartbeatRequestHandler (BaseHTTPRequestHandler) :
  def do_GET(self) :
    if self.path == "/heartbeat" :
      self.send_response(200)
      self.send_header("Content-type:", "text/html")
      self.wfile.write("\n")
      obj = {"status": "running", "build": git_sha.git_sha}
      json.dump(obj, self.wfile)
      self.wfile.write("\n")

def run_heartbeat_service(port, addr=''):
  """Starts a HTTP server for prometheus metrics as a daemon thread."""
  class HeartbeatServer(threading.Thread):
    def run(self):
      httpd = HTTPServer((addr, port), HeartbeatRequestHandler)
      httpd.serve_forever()
  t = HeartbeatServer()
  t.daemon = True
  t.start()

