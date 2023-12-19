import zmq
import random
import sys
import time


port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

# Setting a timeout for receiving messages
socket.setsockopt(zmq.RCVTIMEO, 5000)  # Timeout set to 5000 milliseconds (5 seconds)


while True:
    try:
        socket.send_string("Server message to client3")
        msg = socket.recv_string()
        print (msg)
        time.sleep(5)
    except Exception as e:
        print("client not found")
