import random
from threading import Thread
import time
import zmq

import concurrent.futures

cluster ={}
leader = None
term = 0

context = zmq.Context()


class Raft:
    def __init__(self, port) -> None:
        self.term = 0
        self.node = port 
        self.socket = context.socket(zmq.PAIR)
        self.socket.bind(f"tcp://127.0.0.1:{port}")

        self.voted_for = None
        self.votes = 0

        self.timeout = random.randrange(2,5)
        print(port + " : "+  str(self.timeout))
        self.socket.setsockopt(zmq.RCVTIMEO, self.timeout*1000)
        self.state = "Follower"
        


    def send_heartbeat(self):
        global cluster
        while self.state == "Leader":
            for node1 in cluster.keys():
                if(node1!= self.node):
                    self.send_ping(node1)
            time.sleep(1)
    def send_ping(self, node):
        socket = context.socket(zmq.PAIR)
        socket.connect(f"tcp://127.0.0.1:{node}")
        socket.send_string("alive")
        print(f'{self.node} sent heartbeat to {node}')


    def recieve_ping(self):
        while self.state != "Leader":
            try:
                self.socket.recv_string()
                print(f'{self.node} recieved heartbeat')
            except Exception as e:
                start_election(self)
    
    def request_vote(self, node, term):
        if self.term < term:
            self.term = term
            self.voted_for = node
            print(f'{self.node} voted for {self.voted_for} ')
        return self.voted_for == node
    
def add_node(self, node):
    cluster[node] = Raft(node)

def start_election(node):
    global leader
    global term

    time.sleep(node.timeout)
    node.votes=0
    if node.state == "Follower" and leader is None:
        node.state = "Candidate"
        node.votes += 1
        node.term = term +1
        for node1 in cluster.values():
            if(node1.node!= node.node):
                voted_node = node1.request_vote(node.node, node.term)
                print(f'{node.node} {node1.node}')
                if voted_node:
                    node.votes += 1
        print("Thread "+ node.node +" count: "+ str(node.votes))
        if(node.votes> (len(cluster)/2)) and leader is None:
            print(f'{node.node} is the new leader')
            node.state = "Leader"
            time.sleep(2)
            term +=1

            print("Thread "+ node.node + " is stating to send")
            Thread(target = node.send_heartbeat()).start()
        else:
            node.state = "Follower"
    if(node.state != "Leader"):
        time.sleep(6)
        print("Thread "+ node.node + " is stating to receive")
        Thread(target = node.recieve_ping()).start()


initial_nodes = ["5000", "5001", "5002"]
for port in initial_nodes:
    node = Raft(port)
    cluster[port] = node
    Thread(target=start_election, args=(node,)).start()

    

    


