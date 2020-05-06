import socket
import random
import pickle
import data.mongo_setup as mongo_setup
import data.dataservice as svc

mongo_setup.global_init()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "127.0.0.1"
port = 5555
addr = (server, port)

client.connect(addr)

while True:
    x = int(input())
    try:

        data = svc.get_info(x)
        id = data[0].cam_id
        lat = data[0].latitude
        long = data[0].longitude
        print(id, lat, long)
        client.send(pickle.dumps(str(id)+" "+lat+" "+long))
        print("x")
    except:
        print("Something fishy")
