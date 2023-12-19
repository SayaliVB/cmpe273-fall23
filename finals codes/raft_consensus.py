import random
import threading
import time
import zmq

# Global variables
cluster = {}
leader = None
term = 0
entry_queue = []

# ZMQ Context
context = zmq.Context()


class LogEntry:
    def __init__(self, term, command):
        self.term = term
        self.command = command


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.state = "follower"
        self.voted_for = None
        self.term = 0
        self.log = []
        self.replicator_socket = context.socket(zmq.PAIR)

    def become_candidate(self):
        self.state = "candidate"
        self.voted_for = self.node_id
        self.term += 1
        print(f"{self.node_id} became candidate for term {self.term}")

    def become_leader(self):
        global leader
        self.state = "leader"
        leader = self.node_id
        print(f"{self.node_id} became leader for term {self.term}")

    def become_follower(self):
        self.state = "follower"

    def request_vote(self, candidate_id, candidate_term):
        if candidate_term > self.term:
            self.term = candidate_term
            self.voted_for = candidate_id
        return self.voted_for == candidate_id

    def notify_membership_changes(self, new_cluster):
        global cluster
        cluster = new_cluster
        print(f"{self.node_id}: Updated cluster state: {new_cluster.keys()}")

    def append_entry(self, entry):
        self.log.append(entry)
        print(f"{self.node_id}: Appended entry {entry.command} to the log")

    def replicate_entries(self, entries):
        for entry in entries:
            self.append_entry(entry)

    def bind_replicator_socket(self, port):
        self.replicator_socket.bind(f"tcp://*:{port}")

    def connect_replicator_socket(self, port):
        self.replicator_socket.connect(f"tcp://localhost:{port}")


def election_timeout(node):
    while True:
        time.sleep(random.uniform(0.5, 1.5))
        if node.state == "follower":
            node.become_candidate()
            votes = 1
            for peer_node in cluster.values():
                if peer_node != node:
                    vote_granted = peer_node.request_vote(node.node_id, node.term)
                    if vote_granted:
                        votes += 1
            if votes > len(cluster) // 2:
                node.become_leader()
                # Replicate new entries as leader
                while node.state == "leader":
                    for command in entry_queue:
                        new_entry = LogEntry(node.term, command)
                        node.append_entry(new_entry)
                        node.replicator_socket.send_pyobj(new_entry)
                        entry_queue.remove(command)
                    time.sleep(1)


def add_node(node_id, replicator_port):
    global cluster
    new_node = Node(node_id)
    if node_id in cluster:
        new_node.replicator_socket = cluster[node_id].replicator_socket
    else:
        new_node.connect_replicator_socket(replicator_port)
    cluster[node_id] = new_node
    return new_node


def remove_node(node_id):
    global cluster
    if node_id in cluster:
        del cluster[node_id]


def update_membership(node_id_list, replicator_ports):
    new_cluster = {nid: add_node(nid, replicator_ports[nid]) for nid in node_id_list}
    for node in new_cluster.values():
        node.notify_membership_changes(new_cluster)
    return new_cluster


def add_entry(command):
    global entry_queue
    entry_queue.append(command)


# Initialization
initial_nodes = ["A", "B", "C"]
replicator_ports = {"A": 5556, "B": 5557, "C": 5558, "D": 5559, "E": 5560}
for node_id, port in zip(initial_nodes, replicator_ports.values()):
    node = Node(node_id)
    cluster[node_id] = node
    # For this simple example, only localhost communication is assumed
    node.bind_replicator_socket(port)
    threading.Thread(target=election_timeout, args=(node,)).start()

time.sleep(5)
add_entry("command_1")
add_entry("command_2")

time.sleep(5)
new_nodes = ["A", "B", "C", "D", "E"]
print("Adding nodes D and E")
update_membership(new_nodes, replicator_ports)

add_entry("command_3")
add_entry("command_4")

time.sleep(5)
new_nodes = ["A", "C", "D", "E"]
print("Removing node B")
update_membership(new_nodes, replicator_ports)