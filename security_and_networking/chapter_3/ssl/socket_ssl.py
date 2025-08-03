import ssl
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context()
secure_socket = context.wrap_socket(sock, server_hostname="www.google.com")
data = bytearray()

try:
    secure_socket.connect(("www.google.com", 443))
    print(f"Cipher: {secure_socket.cipher()}")
    secure_socket.write(b"GET / HTTP/1.1 \r\n")
    secure_socket.write(b"Host: www.google.com\n\n")
    data = secure_socket.read()
    print(data.decode("utf-8"))
except Exception as exception:
    print("Exception: ", exception)
