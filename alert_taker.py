import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "127.0.0.1"
port = 5555
addr = (server, port)

client.connect(addr)


while True:
    client.send(pickle.dumps('Not me'))
    x = pickle.loads(client.recv(2048))
    if len(x) > 0:
        print("Got:", x)

