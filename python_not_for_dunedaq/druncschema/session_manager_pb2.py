# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/session_manager.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from druncschema import request_response_pb2 as druncschema_dot_request__response__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!druncschema/session_manager.proto\x12\x13\x64unedaq.druncschema\x1a\"druncschema/request_response.proto\"\x97\x01\n\x10SessionsAndUsers\x12N\n\rsession_users\x18\x01 \x03(\x0b\x32\x37.dunedaq.druncschema.SessionsAndUsers.SessionUsersEntry\x1a\x33\n\x11SessionUsersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb6\x01\n\x10\x43onfigurationKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x46\n\x05\x63type\x18\x04 \x01(\x0e\x32\x37.dunedaq.druncschema.ConfigurationKey.ConfigurationType\")\n\x11\x43onfigurationType\x12\x07\n\x03OKS\x10\x00\x12\x0b\n\x07\x44\x41QCONF\x10\x01\"a\n\x12SessionDescription\x12\x35\n\x06\x63onfig\x18\x01 \x01(\x0b\x32%.dunedaq.druncschema.ConfigurationKey\x12\x14\n\x0csession_name\x18\x02 \x01(\t2\xf8\x03\n\x0eSessionManager\x12I\n\x08\x64\x65scribe\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12M\n\x0clist_session\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12N\n\rstart_session\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12R\n\x11terminate_session\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12S\n\x12load_configuration\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12S\n\x12list_configuration\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.session_manager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SESSIONSANDUSERS_SESSIONUSERSENTRY']._loaded_options = None
  _globals['_SESSIONSANDUSERS_SESSIONUSERSENTRY']._serialized_options = b'8\001'
  _globals['_SESSIONSANDUSERS']._serialized_start=95
  _globals['_SESSIONSANDUSERS']._serialized_end=246
  _globals['_SESSIONSANDUSERS_SESSIONUSERSENTRY']._serialized_start=195
  _globals['_SESSIONSANDUSERS_SESSIONUSERSENTRY']._serialized_end=246
  _globals['_CONFIGURATIONKEY']._serialized_start=249
  _globals['_CONFIGURATIONKEY']._serialized_end=431
  _globals['_CONFIGURATIONKEY_CONFIGURATIONTYPE']._serialized_start=390
  _globals['_CONFIGURATIONKEY_CONFIGURATIONTYPE']._serialized_end=431
  _globals['_SESSIONDESCRIPTION']._serialized_start=433
  _globals['_SESSIONDESCRIPTION']._serialized_end=530
  _globals['_SESSIONMANAGER']._serialized_start=533
  _globals['_SESSIONMANAGER']._serialized_end=1037
# @@protoc_insertion_point(module_scope)
