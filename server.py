import os
from http.server import CGIHTTPRequestHandler, HTTPServer


# server port (documentation: https://www.cloudflare.com/learning/network-layer/what-is-a-computer-port/)
# port numbers 0 to 1023 are reserved for privileged services and designated as well-known ports
# it's a good practice to use port numbers range from 1023 to 65535 for local servers
PORT = 9000


def start_server():
    # change current working directory to './static'
    os.chdir('./static')

    server = HTTPServer(server_address=('', PORT),
                        RequestHandlerClass=CGIHTTPRequestHandler)
    # serve './static' folder
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
