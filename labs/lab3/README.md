Implement one of the Google Map GRPC APIs called ValidateAddressLinks to an external site. in Python.
https://github.com/googleapis/googleapis/blob/master/google/maps/addressvalidation/v1/address_validation_service.proto

// Validates an address.
  rpc ValidateAddress(ValidateAddressRequest)
      returns (ValidateAddressResponse) {
    option (google.api.http) = {
      post: "/v1:validateAddress"
      body: "*"
    };
  }

 

You can use this exampleLinks to an external site. as your baseline for the lab.
https://grpc.io/docs/languages/python/quickstart/

Please name your files:

googlemap_validate_address_server.py
googlemap_validate_address_client.py
