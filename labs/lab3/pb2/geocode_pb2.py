# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: geocode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb2.viewport_pb2 as viewport__pb2
import pb2.latlng_pb2 as latlng__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rgeocode.proto\x12 google.maps.addressvalidation.v1\x1a\x0eviewport.proto\x1a\x0clatlng.proto\"\xde\x01\n\x07Geocode\x12%\n\x08location\x18\x01 \x01(\x0b\x32\x13.google.type.LatLng\x12=\n\tplus_code\x18\x02 \x01(\x0b\x32*.google.maps.addressvalidation.v1.PlusCode\x12)\n\x06\x62ounds\x18\x04 \x01(\x0b\x32\x19.google.geo.type.Viewport\x12\x1b\n\x13\x66\x65\x61ture_size_meters\x18\x05 \x01(\x02\x12\x10\n\x08place_id\x18\x06 \x01(\t\x12\x13\n\x0bplace_types\x18\x07 \x03(\t\"6\n\x08PlusCode\x12\x13\n\x0bglobal_code\x18\x01 \x01(\t\x12\x15\n\rcompound_code\x18\x02 \x01(\tB\x89\x02\n$com.google.maps.addressvalidation.v1B\x0cGeocodeProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xf8\x01\x01\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'geocode_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.google.maps.addressvalidation.v1B\014GeocodeProtoP\001ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\370\001\001\242\002\007GMPAVV1\252\002 Google.Maps.AddressValidation.V1\312\002 Google\\Maps\\AddressValidation\\V1\352\002#Google::Maps::AddressValidation::V1'
  _globals['_GEOCODE']._serialized_start=82
  _globals['_GEOCODE']._serialized_end=304
  _globals['_PLUSCODE']._serialized_start=306
  _globals['_PLUSCODE']._serialized_end=360
# @@protoc_insertion_point(module_scope)
