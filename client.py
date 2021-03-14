import socket
import random
from threading import Thread
import os

os.system("color 0a")

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002
separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))

name = input("Enter your name: ")
print("[+]", name, "connected!")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'leave':
        break
    to_send = f"{name}{separator_token}{to_send}"
    s.send(to_send.encode())
s.close()