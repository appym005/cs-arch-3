import socket
from _thread import *
import sys
import pickle
from _thread import *
import data.mongo_setup as mongo_setup
import data.dataservice as svc

mongo_setup.global_init()

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
    while True:
        try:
            msg = pickle.loads(conn.recv(2048))
            cam_id = int(msg)
            if cam_id == -1:
                conn.sendall(pickle.dumps(m))
                continue
            cam = svc.get_info(cam_id)
            if len(cam) != 0:
                print(cam[0].cam_id, cam[0].latitude, cam[0].longitude)
                m = f"{cam[0].cam_id}: {cam[0].latitude}, {cam[0].longitude}"
                conn.sendall(pickle.dumps(m))
            else:
                conn.sendall(pickle.dumps("Breach"))
            m = ''
            lc = 0

        except:
            break
    print(f"Connection lost to {lc}")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(child, (conn, ''))


