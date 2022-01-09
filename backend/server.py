from socket import *
from log import log

HOST = "127.0.0.1"
PORT = 3000

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORT))
