from http.server import BaseHTTPRequestHandler,HTTPServer
import os

port = 8000
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        hostname = 'temp'
        if 'HOSTNAME' in os.environ: hostname = os.environ['HOSTNAME']
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hi! I\'m " + bytes(hostname, 'utf-8') )


httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print('Starting server at %d' % (port))
httpd.serve_forever()

