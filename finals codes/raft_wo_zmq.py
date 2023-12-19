import random
import threading
import time

# Global variables
cluster = {}
leader = None
term = 0
entry_queue = []


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

def add_node(node_id):
    global cluster
    new_node = Node(node_id)
    cluster[node_id] = new_node
    return new_node

def remove_node(node_id):
    global cluster
    if node_id in cluster:
        del cluster[node_id]

def update_membership(node_id_list):
    new_cluster = {nid: cluster[nid] if nid in cluster else add_node(nid) for nid in node_id_list}
    for node in new_cluster.values():
        node.notify_membership_changes(new_cluster)
    return new_cluster

def add_entry(command):
    global entry_queue
    entry_queue.append(command)

def process_entries():
    # Continuously process the entry queue
    while True:
        if leader:
            leader_node = cluster[leader]
            if leader_node.state == "leader":
                for command in entry_queue:
                    new_entry = LogEntry(leader_node.term, command)
                    leader_node.append_entry(new_entry)
                    for peer_node in cluster.values():
                        if peer_node != leader_node:
                            peer_node.replicate_entries([new_entry])
                    entry_queue.remove(command)

# Initialization
initial_nodes = ["A", "B", "C"]
for node_id in initial_nodes:
    node = Node(node_id)
    cluster[node_id] = node
    threading.Thread(target=election_timeout, args=(node,)).start()

# Process entry queue
threading.Thread(target=process_entries, daemon=True).start()

# Example: Add some entries to the queue
time.sleep(5)
add_entry("command_1")
add_entry("command_2")

time.sleep(5)
new_nodes = ["A", "B", "C", "D", "E"]
print("Adding nodes D and E")
update_membership(new_nodes)

# Add some more entries to the queue
add_entry("command_3")
add_entry("command_4")

time.sleep(5)
new_nodes = ["A", "C", "D", "E"]
print("Removing node B")
update_membership(new_nodes)