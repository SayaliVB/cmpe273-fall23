from concurrent import futures

import logging

import grpc
import address_validation_service_pb2
import address_validation_service_pb2_grpc
from address_validation_service_pb2 import ValidationResult

class ValidateAddress(address_validation_service_pb2_grpc.AddressValidationServicer):
    def ValidateAddress(self, request, context):
        print("Address Validation request made")
        print(request)
        validationresult = ValidationResult()
        validationresult.geocode.place_id = request.address.postal_code
        reply =  address_validation_service_pb2.ValidateAddressResponse()
        reply.response_id=f"Address Recieved: {request.address}!"
        #reply.result = validationresult
        #error with above: AttributeError: Assignment not allowed to message, map, or repeated field "result" in protocol message object.
        return reply

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    address_validation_service_pb2_grpc.add_AddressValidationServicer_to_server(ValidateAddress(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()