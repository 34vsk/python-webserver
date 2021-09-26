import os
import io
from urllib.parse import urlparse, parse_qs
from http.server import CGIHTTPRequestHandler, BaseHTTPRequestHandler, HTTPServer


# server port (documentation: https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)
# port numbers 0 to 1023 are reserved for privileged services and designated as well-known ports
# it's a good practice to use port numbers range from 1023 to 65535 for local servers
PORT = 9000

# change current working directory to './static'
os.chdir('./static')


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # handle GET requests
    def do_GET(self):
        # get current working directory
        root = os.getcwd()
        # serve index.html page for '/' path
        if self.path == '/':
            filename = root + '/index.html'
        # serve other files
        else:
            filename = root + self.path

        # set 200 status code (200 -> everything is ok)
        self.send_response(200)
        # set file type (required for browsers to understand how to work with received file)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        # read file and send it to browser
        with open(filename, 'rb') as fh:
            html = fh.read()
            self.wfile.write(html)

    # handle POST requests
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        parsed_body = parse_qs(body)
        self.send_response(200)
        self.end_headers()
        message = parsed_body[b'message'][0].decode("utf-8")
        print("Message received: "+message)


def start_server():
    server = HTTPServer(server_address=('', PORT),
                        RequestHandlerClass=SimpleHTTPRequestHandler)
    # start server
    server.serve_forever()


# Handle Ctrl+C event
try:
    print("Starting http server...")
    start_server()

# press Ctrl+C to stop server
except KeyboardInterrupt:
    print('\nShutting down http server...')
    # exit code 0 means graceful shutdown
    exit(0)
