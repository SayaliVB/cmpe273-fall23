import datetime
from threading import Thread
import time
import zmq

context = zmq.Context()

class GossipNode:
    def __init__(self, port, connected_nodes) -> None:

        self.node = context.socket(zmq.PAIR)
        self.node.bind("tcp://*:%s" % port)
        self.node.RCVTIMEO = 1000
        self.connected_nodes = connected_nodes

        self.previous_message = ''

        Thread(target=self.input_rumor).start()
        
        Thread(target=self.receive_rumor).start()
    
    def input_rumor(self):
        while True:
            msg = input("Enter string")

            print("Entered: "+ msg)
            self.previous_message = msg+str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            
            print("Transmit: "+ msg)

            self.transmit_rumor(msg)
    
    def receive_rumor(self, message = ''):
        while True:
            msg = self.node.recv_string()

            if(self.previous_message == msg):
                continue

            self.previous_message = msg
            print("Received: "+ msg)
            print("Relay: "+ msg)

            self.transmit_rumor(msg)
    
    def transmit_rumor(self, msg):
        for node in self.connected_nodes:
            time.sleep(2)
            print(f'tcp://localhost:{node}')
            socket = context.socket(zmq.PAIR)
            socket.connect("tcp://localhost:%s" % node)
            socket.send_string(msg)
            print("sent")
    

