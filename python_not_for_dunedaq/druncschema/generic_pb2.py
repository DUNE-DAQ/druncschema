# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/generic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64runcschema/generic.proto\x12\x13\x64unedaq.druncschema\"\x07\n\x05\x45mpty\"\x19\n\tPlainText\x12\x0c\n\x04text\x18\x01 \x01(\t\"\x1f\n\x0fPlainTextVector\x12\x0c\n\x04text\x18\x01 \x03(\t\"\x1a\n\nStacktrace\x12\x0c\n\x04text\x18\x01 \x03(\t\"y\n\x0fStringStringMap\x12:\n\x03map\x18\x01 \x03(\x0b\x32-.dunedaq.druncschema.StringStringMap.MapEntry\x1a*\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x18\n\x07int_msg\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1a\n\tfloat_msg\x12\r\n\x05value\x18\x01 \x01(\x02\"\x1b\n\nstring_msg\x12\r\n\x05value\x18\x01 \x01(\t\"\x19\n\x08\x62ool_msg\x12\r\n\x05value\x18\x01 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.generic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STRINGSTRINGMAP_MAPENTRY._options = None
  _STRINGSTRINGMAP_MAPENTRY._serialized_options = b'8\001'
  _globals['_EMPTY']._serialized_start=50
  _globals['_EMPTY']._serialized_end=57
  _globals['_PLAINTEXT']._serialized_start=59
  _globals['_PLAINTEXT']._serialized_end=84
  _globals['_PLAINTEXTVECTOR']._serialized_start=86
  _globals['_PLAINTEXTVECTOR']._serialized_end=117
  _globals['_STACKTRACE']._serialized_start=119
  _globals['_STACKTRACE']._serialized_end=145
  _globals['_STRINGSTRINGMAP']._serialized_start=147
  _globals['_STRINGSTRINGMAP']._serialized_end=268
  _globals['_STRINGSTRINGMAP_MAPENTRY']._serialized_start=226
  _globals['_STRINGSTRINGMAP_MAPENTRY']._serialized_end=268
  _globals['_INT_MSG']._serialized_start=270
  _globals['_INT_MSG']._serialized_end=294
  _globals['_FLOAT_MSG']._serialized_start=296
  _globals['_FLOAT_MSG']._serialized_end=322
  _globals['_STRING_MSG']._serialized_start=324
  _globals['_STRING_MSG']._serialized_end=351
  _globals['_BOOL_MSG']._serialized_start=353
  _globals['_BOOL_MSG']._serialized_end=378
# @@protoc_insertion_point(module_scope)
