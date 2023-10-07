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
    
        ```
        Numbers: 
        The numbered tags are used to match fields when serializing and deserializing the data.
        Obviously, if you change the numbering scheme, and apply this change to both serializer and deserializer, there is no issue.

        Consider though, if you saved data with the first numbering scheme, and loaded it with the second one, it would try to load one field into another, and deserialization would likely fail.

        Now, why is this useful? Let's say you need to add another field to your data, long after the schema is already in use,
        Because you explicitly give it a number, your deserializer is still able to load data serialized with the old numbering scheme, ignoring deserialization of non-existent data.
        ```
        
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

grpc.insecure_channel("localhost:50051"): connect

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

https://stackoverflow.com/questions/54348065/repeatedscalarfieldcontainer-object-has-no-attribute-add


# For Address validation grpc:

Step 1:

download address_validation_servicce and all the proto dependencies for it.
change the import paths as all the protos are in one folder for us


Step 2:

generate tools for address_validation_service.proto
```python3 -m grpc_tools.protoc -I protos --python_out=. --pyi_out=. --grpc_python_out=. protos/address_validation_service.proto```


Step 3:

generate pb2 for other protos:

eg:

```python3 -m grpc_tools.protoc -I protos --python_out=pb2 protos/annotations.proto```
```python3 -m grpc_tools.protoc -I protos --python_out=pb2 protos/client.proto```


Step 4:

update the import path to pb2.__

eg:
```
import pb2.field_behavior_pb2 as field__behavior__pb2
import pb2.postal_address_pb2 as postal__address__pb2
```


Step 5:

Write the server and client

```
reply.response_id #response_id is the field in address_validation_service.proto response format
```

In client, the request will take 3 parameters. the address parameter is of type postal address.

```
ValidateAddressRequest(address=postalAddress, previous_response_id=None, enable_usps_cass=True)
```


In postal_address.proto: the structure of request is defined

hence create dictionary

```
postalAddress = {"revision" : 0, "region_code":"CH", "language_code":"en", "postal_code":"95126","address_lines": "500 Race Street"}
```

The address_lines is of type repeated string hence add multiple strings to it.
postalAddress = PostalAddress()
postalAddress.address_lines.append("500 Race Street")
postalAddress.address_lines.append("San Jose")
postalAddress.address_lines.append("California")
