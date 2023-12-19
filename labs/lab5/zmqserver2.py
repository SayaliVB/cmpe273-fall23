import zmq
 
ctx = zmq.Context()
client_socket = ctx.socket(zmq.PULL)
 
client_socket.connect('tcp://127.0.0.1:5002')

push_socket= ctx.socket(zmq.PUSH)
 
push_socket.bind('tcp://*:5012')
 
 

class GSet():
    """
    GSet implements a grow-only set CRDT. Items can be added to the set but can't be
    removed.
    """

    def __init__(self):
        self.items = set()

    def add(self, item):
        """
        Adds an item to the set.
        """
        print("Item " + item, end="")
        self.items.add(item)
        print(" added successfully!")

    def get(self):
        """
        Returns the current items in the set.
        """
        return self.items  

def main():
    gset = GSet()
    while True:
        msg = client_socket.recv_string()
        #print("Recieved from client: ", end="")
        #print (msg)
        if msg == "":
            push_socket.send_pyobj(gset.get())
        else:
            gset.add(msg)

if __name__=="__main__": 
    main()