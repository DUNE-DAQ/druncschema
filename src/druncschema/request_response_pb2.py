# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: request_response.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import druncschema.token_pb2 as token__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16request_response.proto\x1a\x0btoken.proto\x1a\x19google/protobuf/any.proto\"R\n\x07Request\x12\x15\n\x05token\x18\x01 \x01(\x0b\x32\x06.Token\x12\'\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x42\x07\n\x05_data\"S\n\x08Response\x12\x15\n\x05token\x18\x01 \x01(\x0b\x32\x06.Token\x12\'\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x88\x01\x01\x42\x07\n\x05_datab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'request_response_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=66
  _REQUEST._serialized_end=148
  _RESPONSE._serialized_start=150
  _RESPONSE._serialized_end=233
# @@protoc_insertion_point(module_scope)
