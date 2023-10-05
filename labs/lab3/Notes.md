# Hello World code:

Files we'll be working on:
/grpc/examples/protos/helloworld.proto
/grpc/examples/python/helloworld/greeter_client.py
/grpc/examples/python/helloworld/greeter_server.py

<details>

<summary> helloworld.proto </summary>
message HelloRequest{}:
    parameters which request will take
message HelloReply {}:
    parameters which response will send
        ```Numbers: 
        The numbered tags are used to match fields when serializing and deserializing the data.
        Obviously, if you change the numbering scheme, and apply this change to both serializer and deserializer, there is no issue.

        Consider though, if you saved data with the first numbering scheme, and loaded it with the second one, it would try to load one field into another, and deserialization would likely fail.

        Now, why is this useful? Let's say you need to add another field to your data, long after the schema is already in use,
        Because you explicitly give it a number, your deserializer is still able to load data serialized with the old numbering scheme, ignoring deserialization of non-existent data.```
service Greeter{}:
    define the apis-> either Unary Calls, Client Side, Server Side or Multi-directional Streaming
</details>

<details>

<summary> greeter_server.py </summary>

Greeter(helloworld_pb2_grpc.GreeterServicer){}:
    implement methods from proto
def serve():
    setup server
    ```futures.ThreadPoolExecutor(max_workers=10) : max number of threads```
    ```helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server) : add defined greeter service to server to direct request```
</details>

<details>

<summary> greeter_client.py </summary>

grpc.insecure_channel("localhost:50051"): 
    connect

create request with necessary parameteres
get response and display

</details>


<details>

<summary> helloworld_pb2_grpc.py </summary>

will contain client stub 
GreeterStub : defines how call is made to the server
 
</details>

<details>

<summary> helloworld_pb2.py </summary>

Stores all the requests and responses
 
</details>


Follow:
https://protobuf.dev/programming-guides/proto2/
https://grpc.io/docs/languages/python/quickstart/
https://www.youtube.com/watch?v=rmhdyk7mazc -> first 5 mins
https://www.youtube.com/watch?v=WB37L7PjI5k


For Address validation grpc:

download address_validation_servicce and all the proto dependencies for it.
change the import paths as all the protos are in one folder for us

generate tools for address_validation_service.proto

```python3 -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. protos/address_validation_service.proto```

generate pb2 for other protos:
eg:
```python3 -m grpc_tools.protoc -I protos --python_out=pb2 protos/annotations.proto```
```python3 -m grpc_tools.protoc -I protos --python_out=pb2 protos/client.proto```