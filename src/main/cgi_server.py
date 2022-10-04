# This is a sample Python script.
import cgi
from http.server import HTTPServer, CGIHTTPRequestHandler

server_adress = ("", 8000)
httpi = HTTPServer(server_adress, CGIHTTPRequestHandler)

httpi.serve_forever()
