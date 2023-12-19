import zmq
import time
 
 
ctx = zmq.Context()

push1_socket= ctx.socket(zmq.PUSH)
 
push1_socket.bind('tcp://*:5001')
push1_socket.setsockopt(zmq.SNDHWM, 0)

push2_socket= ctx.socket(zmq.PUSH)
 
push2_socket.bind('tcp://*:5002')
push2_socket.setsockopt(zmq.SNDHWM, 0)

server1_socket = ctx.socket(zmq.PULL)
 
server1_socket.connect('tcp://127.0.0.1:5011')

server2_socket = ctx.socket(zmq.PULL)
 
server2_socket.connect('tcp://127.0.0.1:5012')


class GSet():
    """
    GSet implements a grow-only set CRDT. Items can be added to the set but can't be
    removed.
    """

    def __init__(self):
        self.items = set()

    def merge(self, other):
        """
        Merges another GSet with this one.
        """
        if not isinstance(other, set):
            raise ValueError("Incompatible CRDT for merge(), expected Set")
        self.items = self.items.union(other)
        return self

def main():
    #pause to start the servers
    time.sleep(1)

    gset = GSet()
    datalist = ["One", "Two", "Three", "Four", "Five"]

    for x in datalist:
        msg = x
        print("Sent from client: ", end="")
        print(msg)

        try:
            push1_socket.send_string(msg, zmq.NOBLOCK)
        except:
            print("No receivers for server 1, message not sent.")
        
        try:
            push2_socket.send_string(msg, zmq.NOBLOCK)
        except:
            print("No receivers for server 2, message not sent.")

        #Pause 1 second
        time.sleep(1)
    
    #get data
    push1_socket.send_string("")
    msg_server1 = server1_socket.recv_pyobj()
    print("Recieved from server1: ", end="")
    print(msg_server1)

    push2_socket.send_string("")
    msg_server2 = server2_socket.recv_pyobj()
    print("Recieved from server2: ", end="")
    print(msg_server2)

    if len(msg_server2.difference(msg_server1))==0:
        print("Same sets")
    else:
        gset.merge(msg_server1)
        gset.merge(msg_server2)
        if len(gset.items.difference(msg_server1)) !=0:
            for x in gset.items.difference(msg_server1):
                msg = x
                print("Re-sent from client: ", end="")
                print(msg)

                try:
                    push1_socket.send_string(msg, zmq.NOBLOCK)
                except:
                    print("No receivers for server 1, message not sent.")
                
                #Pause 1 second
                time.sleep(1)
            #get data
            push1_socket.send_string("")
            msg_server1 = server1_socket.recv_pyobj()
            print("Recieved from server1: ", end="")
            print(msg_server1)
        if len(gset.items.difference(msg_server2)) !=0:
            for x in gset.items.difference(msg_server2):
                msg = x
                print("Re-sent from client: ", end="")
                print(msg)

                try:
                    push2_socket.send_string(msg, zmq.NOBLOCK)
                except:
                    print("No receivers for server 2, message not sent.")
                
                #Pause 1 second
                time.sleep(1)
            push2_socket.send_string("")
            msg_server2 = server2_socket.recv_pyobj()
            print("Recieved from server2: ", end="")
            print(msg_server2)    
        


if __name__=="__main__": 
    main()