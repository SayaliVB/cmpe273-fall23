import zmq

context = zmq.Context()

pull_socket = context.socket(zmq.PULL)
pull_socket.connect("tcp://127.0.0.1:5010")

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

message = pull_socket.recv_string()
print("Sent from client: "+ message)

#recieve bytes
message = pull_socket.recv()
print("Sent from client: "+ str(message)) 

message = pull_socket.recv_multipart()
print("Sent from client: "+ str(message))

message = pull_socket.recv_pyobj()
print("Sent from client: "+ str(message)) 

message = pull_socket.recv_pyobj()
print("Sent from client: "+ str(message)) 