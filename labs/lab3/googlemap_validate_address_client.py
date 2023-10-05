
from __future__ import print_function

import logging

import grpc
import address_validation_service_pb2_grpc
import address_validation_service_pb2
from pb2.postal_address_pb2 import PostalAddress

def run():
    print("Let's validate some address")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = address_validation_service_pb2_grpc.AddressValidationStub(channel=channel)
        postalAddress = PostalAddress()
        postalAddress.address_lines.append("500 Race Street")
        postalAddress.address_lines.append("San Jose")
        postalAddress.address_lines.append("California")
        postalAddress.revision = 0
        postalAddress.region_code = "CH"
        postalAddress.language_code = "en"
        postalAddress.postal_code = "95126"
        #postalAddress = {"revision" : 0, "region_code":"CH", "language_code":"en", "postal_code":"95126","address_lines": "500 Race Street"}
        request = address_validation_service_pb2.ValidateAddressRequest(address=postalAddress, previous_response_id=None, enable_usps_cass=True)
        response = stub.ValidateAddress(request)
        print("Response recieved")
        print(response)

if __name__ == "__main__":
    logging.basicConfig()
    run()