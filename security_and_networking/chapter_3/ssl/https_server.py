# The below command generates a self-signed SSL certificate (cert.pem) and a private key (key.pem) valid for 365 days using a 2048-bit RSA encryption.
## openssl req -x509 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == "__main__":
    server_address = ('localhost', 4443)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("Serving HTTPS on https://localhost:4443")
    httpd.serve_forever()
