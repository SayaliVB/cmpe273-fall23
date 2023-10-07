Implement one of the Google Map GRPC APIs called ValidateAddressLinks to an external site. in Python.

// Validates an address.
  rpc ValidateAddress(ValidateAddressRequest)
      returns (ValidateAddressResponse) {
    option (google.api.http) = {
      post: "/v1:validateAddress"
      body: "*"
    };
  }

 

You can use this exampleLinks to an external site. as your baseline for the lab.

Please name your files:

googlemap_validate_address_server.py
googlemap_validate_address_client.py
