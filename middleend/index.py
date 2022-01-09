from flask import Flask
from socket import *
from log import log
import os

HOST = "127.0.0.1"
PORT = 3000

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
back, addr = sock.accept()

def recvFile(sock:socket, filename):
    try:
        with open(filename, "wb") as file:
            data = sock.recv(1024)
            if data.decode() == "no file":
                log(f"요청한 파일이 없음 : {filename}", 2)
                return 0
            while data:
                file.write(data)
                data = sock.recv(1024)
    except Exception as e:
        log(e, 1)

app = Flask(__name__)

@app.route('/')
def home():
    if os.path.isfile("index.html"):
        back.send("send index.html".encode())
        recvFile(back, "index.html")
    if os.path.isfile("index.css"):
        back.send("send index.css".encode())
        recvFile(back, "index.css")
    if os.path.isfile("index.js"):
        back.send("send index.js".encode())
        recvFile(back, "index.js")

if __name__ == '__main__':
    app.run()