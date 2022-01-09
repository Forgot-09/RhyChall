from flask import Flask, render_template
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
                os.remove(filename)
                return 0
            while data:
                file.write(data)
                data = sock.recv(1024)
    except Exception as e:
        log(e, 1)

app = Flask(__name__)

@app.route('/')
def home():
    if not os.path.isfile("templates/index.html"):
        back.send("send templates/index.html".encode())
        recvFile(back, "templates/index.html")
    if not os.path.isfile("static/index.css"):
        back.send("send static/index.css".encode())
        recvFile(back, "static/index.css")
    if not os.path.isfile("static/index.js"):
        back.send("send static/index.js".encode())
        recvFile(back, "static/index.js")
    return render_template("index.html")

if __name__ == '__main__':
    app.run()