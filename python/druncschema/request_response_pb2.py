# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/request_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from druncschema import token_pb2 as druncschema_dot_token__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"druncschema/request_response.proto\x12\x13\x64unedaq.druncschema\x1a\x17\x64runcschema/token.proto\x1a\x19google/protobuf/any.proto\"X\n\x07Request\x12)\n\x05token\x18\x01 \x01(\x0b\x32\x1a.dunedaq.druncschema.Token\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"Y\n\x08Response\x12)\n\x05token\x18\x01 \x01(\x0b\x32\x1a.dunedaq.druncschema.Token\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.request_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=111
  _globals['_REQUEST']._serialized_end=199
  _globals['_RESPONSE']._serialized_start=201
  _globals['_RESPONSE']._serialized_end=290
# @@protoc_insertion_point(module_scope)
