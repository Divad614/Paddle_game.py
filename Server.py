import socket
from _thread import *
import sys

server = '10.0.0.3'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(1)
print("Waiting for connection, Server started")

pos = [(), ()]
score = [(), ()]


def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                print("Received", reply)
                print("Sending :", reply)

            conn.sendall(str.encode(str(reply)))
        except:
            break

    print("Lost Connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
