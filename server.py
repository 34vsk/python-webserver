import os
from http.server import HTTPServer, CGIHTTPRequestHandler
os.chdir('./static')
server_object = HTTPServer(server_address=(
    '', 9000), RequestHandlerClass=CGIHTTPRequestHandler)
server_object.serve_forever()
