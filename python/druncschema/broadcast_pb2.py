# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/broadcast.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from druncschema import generic_pb2 as druncschema_dot_generic__pb2
from druncschema import request_response_pb2 as druncschema_dot_request__response__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x64runcschema/broadcast.proto\x12\x13\x64unedaq.druncschema\x1a\x19\x64runcschema/generic.proto\x1a\"druncschema/request_response.proto\x1a\x19google/protobuf/any.proto\"\x8a\x01\n\x10\x42roadcastMessage\x12\x0f\n\x07\x65mitter\x18\x01 \x01(\t\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\".dunedaq.druncschema.BroadcastType\x12\"\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0f\n\x07session\x18\x04 \x01(\t\"6\n\x10\x42roadcastRequest\x12\"\n\x1a\x62roadcast_receiver_address\x18\x01 \x01(\t\"$\n\x11\x42roadcastResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08*\x95\x03\n\rBroadcastType\x12\x07\n\x03\x41\x43K\x10\x00\x12\x14\n\x10RECEIVER_REMOVED\x10\x01\x12\x12\n\x0eRECEIVER_ADDED\x10\x02\x12\x10\n\x0cSERVER_READY\x10\x03\x12\x13\n\x0fSERVER_SHUTDOWN\x10\x04\x12\x10\n\x0cTEXT_MESSAGE\x10\x0f\x12\x1b\n\x17\x43OMMAND_EXECUTION_START\x10\x05\x12\x1d\n\x19\x43OMMAND_EXECUTION_SUCCESS\x10\x06\x12\x14\n\x10\x45XCEPTION_RAISED\x10\x07\x12\x1e\n\x1aUNHANDLED_EXCEPTION_RAISED\x10\x08\x12\x11\n\rSTATUS_UPDATE\x10\t\x12\x1c\n\x18SUBPROCESS_STATUS_UPDATE\x10\n\x12\t\n\x05\x44\x45\x42UG\x10\x0b\x12!\n\x1d\x43HILD_COMMAND_EXECUTION_START\x10\x0c\x12#\n\x1f\x43HILD_COMMAND_EXECUTION_SUCCESS\x10\r\x12\"\n\x1e\x43HILD_COMMAND_EXECUTION_FAILED\x10\x0e\x32l\n\x11\x42roadcastReceiver\x12W\n\x10handle_broadcast\x12%.dunedaq.druncschema.BroadcastMessage\x1a\x1a.dunedaq.druncschema.Empty\"\x00\x32\x9b\x02\n\x0f\x42roadcastSender\x12V\n\x15\x61\x64\x64_to_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12[\n\x1aremove_from_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12S\n\x12get_broadcast_list\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.broadcast_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BROADCASTTYPE']._serialized_start=378
  _globals['_BROADCASTTYPE']._serialized_end=783
  _globals['_BROADCASTMESSAGE']._serialized_start=143
  _globals['_BROADCASTMESSAGE']._serialized_end=281
  _globals['_BROADCASTREQUEST']._serialized_start=283
  _globals['_BROADCASTREQUEST']._serialized_end=337
  _globals['_BROADCASTRESPONSE']._serialized_start=339
  _globals['_BROADCASTRESPONSE']._serialized_end=375
  _globals['_BROADCASTRECEIVER']._serialized_start=785
  _globals['_BROADCASTRECEIVER']._serialized_end=893
  _globals['_BROADCASTSENDER']._serialized_start=896
  _globals['_BROADCASTSENDER']._serialized_end=1179
# @@protoc_insertion_point(module_scope)
