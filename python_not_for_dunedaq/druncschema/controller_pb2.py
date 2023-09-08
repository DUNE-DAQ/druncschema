# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/controller.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from druncschema import request_response_pb2 as druncschema_dot_request__response__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x64runcschema/controller.proto\x12\x13\x64unedaq.druncschema\x1a\"druncschema/request_response.proto\x1a\x19google/protobuf/any.proto\"y\n\x0fStringStringMap\x12:\n\x03map\x18\x01 \x03(\x0b\x32-.dunedaq.druncschema.StringStringMap.MapEntry\x1a*\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\x0f\x43ommandResponse\x12-\n\x07\x63ommand\x18\x01 \x01(\x0b\x32\x1c.dunedaq.druncschema.Command\x12\x14\n\x0c\x63ommand_code\x18\x02 \x01(\x05\x12%\n\x07payload\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"W\n\x07\x43ommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\targuments\x18\x02 \x03(\x0b\x32\x1d.dunedaq.druncschema.Argument\x12\x0c\n\x04help\x18\x03 \x01(\t\"G\n\x16ListOfCommandsResponse\x12-\n\x07\x63ommand\x18\x02 \x03(\x0b\x32\x1c.dunedaq.druncschema.Command\"\xd5\x01\n\x08\x41rgument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.dunedaq.druncschema.Argument.ArgumentType\x12!\n\x03\x64\x65\x66\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12#\n\x05value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0c\n\x04help\x18\x05 \x01(\t\"+\n\x0c\x41rgumentType\x12\r\n\tMANDATORY\x10\x00\x12\x0c\n\x08OPTIONAL\x10\x01\x32\xf6\x05\n\nController\x12\x43\n\x02ls\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12V\n\x15\x61\x64\x64_to_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12[\n\x1aremove_from_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12S\n\x12get_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12Q\n\x10get_command_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12P\n\x0f\x65xecute_command\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12M\n\x0ctake_control\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12R\n\x11surrender_control\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12Q\n\x10who_is_in_charge\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.controller_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STRINGSTRINGMAP_MAPENTRY._options = None
  _STRINGSTRINGMAP_MAPENTRY._serialized_options = b'8\001'
  _globals['_STRINGSTRINGMAP']._serialized_start=116
  _globals['_STRINGSTRINGMAP']._serialized_end=237
  _globals['_STRINGSTRINGMAP_MAPENTRY']._serialized_start=195
  _globals['_STRINGSTRINGMAP_MAPENTRY']._serialized_end=237
  _globals['_COMMANDRESPONSE']._serialized_start=239
  _globals['_COMMANDRESPONSE']._serialized_end=364
  _globals['_COMMAND']._serialized_start=366
  _globals['_COMMAND']._serialized_end=453
  _globals['_LISTOFCOMMANDSRESPONSE']._serialized_start=455
  _globals['_LISTOFCOMMANDSRESPONSE']._serialized_end=526
  _globals['_ARGUMENT']._serialized_start=529
  _globals['_ARGUMENT']._serialized_end=742
  _globals['_ARGUMENT_ARGUMENTTYPE']._serialized_start=699
  _globals['_ARGUMENT_ARGUMENTTYPE']._serialized_end=742
  _globals['_CONTROLLER']._serialized_start=745
  _globals['_CONTROLLER']._serialized_end=1503
# @@protoc_insertion_point(module_scope)