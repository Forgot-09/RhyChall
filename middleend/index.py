from flask import Flask, render_template
from socket import *
from log import log
import os
import ssl

HOST = "127.0.0.1"
PORT = 3000

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(1)
log("백엔드 연결 대기중...")
back, addr = sock.accept()

def recvFile(sock:socket, filename):
    file = open(filename, "wb")
    sock.send(f"send {filename}".encode())
    log(f"파일 요청 : {filename}")
    data = sock.recv(1024)
    if data == "no file":
        log(f"요청한 파일 없음 : {filename}", 2)
        return 0
    try:
        while data:
            file.write(data)
            print(file.read())
            data = sock.recv(1024)
        log(f"파일 받음 : {filename}")
    except Exception as e:
        log(e, 1)

app = Flask(__name__)

@app.route('/')
def home():
    if not os.path.isfile("templates/index.html"):
        recvFile(back, "templates/index.html")
    if not os.path.isfile("static/index.css"):
        recvFile(back, "static/index.css")
    if not os.path.isfile("static/index.js"):
        recvFile(back, "static/index.js")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(ssl_context='adhoc')