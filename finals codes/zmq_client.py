import zmq


context = zmq.Context()
push_socket = context.socket(zmq.PUSH)
push_socket.bind("tcp://127.0.0.1:5010")

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

push_socket.send_string("Hello")
push_socket.send(b'Hello')
push_socket.send_multipart([b'A', b'AB', b'C'])
push_socket.send_pyobj(['A', 'AB', 'C'])
push_socket.send_pyobj(Person("Alice", 20))