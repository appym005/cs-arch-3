import socket
from _thread import *
import sys
import pickle

server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(0)
print("Waiting for a connection, Server started")

m = ""

def child(conn, w):
    global m
    lc = -1
    global m
    while True:
        try:
            msg = pickle.loads(conn.recv(2048))
            if msg == 'Not me':
                conn.sendall(pickle.dumps(m))
            
                continue
            else:
                m = msg
                conn.sendall(pickle.dumps(m))
                lc = m.split()[0]
            print(m)
            m = ''
            

        except:
            break
    print(f"Connection lost to {lc}")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(child, (conn, ''))


