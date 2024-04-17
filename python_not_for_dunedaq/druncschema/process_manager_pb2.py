# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: druncschema/process_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from druncschema import request_response_pb2 as druncschema_dot_request__response__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!druncschema/process_manager.proto\x12\x13\x64unedaq.druncschema\x1a\"druncschema/request_response.proto\"G\n\x12ProcessRestriction\x12\x15\n\rallowed_hosts\x18\x01 \x03(\t\x12\x1a\n\x12\x61llowed_host_types\x18\x02 \x03(\t\";\n\x1a\x43ommandNotificationMessage\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\"-\n\x1aGenericNotificationMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xb9\x01\n\x15\x45xceptionNotification\x12\x12\n\nerror_text\x18\x01 \x01(\t\x12I\n\x0bstack_trace\x18\x02 \x03(\x0b\x32\x34.dunedaq.druncschema.ExceptionNotification.StackLine\x1a\x41\n\tStackLine\x12\x11\n\tline_text\x18\x01 \x01(\t\x12\x13\n\x0bline_number\x18\x02 \x01(\t\x12\x0c\n\x04\x66ile\x18\x03 \x01(\t\"O\n\nLogRequest\x12\x30\n\x05query\x18\x01 \x01(\x0b\x32!.dunedaq.druncschema.ProcessQuery\x12\x0f\n\x07how_far\x18\x02 \x01(\x05\"G\n\x07LogLine\x12.\n\x04uuid\x18\x01 \x01(\x0b\x32 .dunedaq.druncschema.ProcessUUID\x12\x0c\n\x04line\x18\x02 \x01(\t\"\x1b\n\x0bProcessUUID\x12\x0c\n\x04uuid\x18\x01 \x01(\t\"n\n\x0fProcessMetadata\x12.\n\x04uuid\x18\x01 \x01(\x0b\x32 .dunedaq.druncschema.ProcessUUID\x12\x0c\n\x04user\x18\x02 \x01(\t\x12\x0f\n\x07session\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\"m\n\x0cProcessQuery\x12/\n\x05uuids\x18\x01 \x03(\x0b\x32 .dunedaq.druncschema.ProcessUUID\x12\r\n\x05names\x18\x02 \x03(\t\x12\x0c\n\x04user\x18\x03 \x01(\t\x12\x0f\n\x07session\x18\x04 \x01(\t\"\xd7\x02\n\x12ProcessDescription\x12\x36\n\x08metadata\x18\x01 \x01(\x0b\x32$.dunedaq.druncschema.ProcessMetadata\x12=\n\x03\x65nv\x18\x02 \x03(\x0b\x32\x30.dunedaq.druncschema.ProcessDescription.EnvEntry\x12U\n\x18\x65xecutable_and_arguments\x18\x03 \x03(\x0b\x32\x33.dunedaq.druncschema.ProcessDescription.ExecAndArgs\x1a\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t\x1a)\n\x0b\x45xecAndArgs\x12\x0c\n\x04\x65xec\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcd\x02\n\x0fProcessInstance\x12\x44\n\x13process_description\x18\x01 \x01(\x0b\x32\'.dunedaq.druncschema.ProcessDescription\x12\x44\n\x13process_restriction\x18\x02 \x01(\x0b\x32\'.dunedaq.druncschema.ProcessRestriction\x12\x44\n\x0bstatus_code\x18\x03 \x01(\x0e\x32/.dunedaq.druncschema.ProcessInstance.StatusCode\x12\x13\n\x0breturn_code\x18\x04 \x01(\x05\x12.\n\x04uuid\x18\x05 \x01(\x0b\x32 .dunedaq.druncschema.ProcessUUID\"#\n\nStatusCode\x12\x0b\n\x07RUNNING\x10\x00\x12\x08\n\x04\x44\x45\x41\x44\x10\x01\"\x99\x01\n\x0b\x42ootRequest\x12\x44\n\x13process_description\x18\x01 \x01(\x0b\x32\'.dunedaq.druncschema.ProcessDescription\x12\x44\n\x13process_restriction\x18\x02 \x01(\x0b\x32\'.dunedaq.druncschema.ProcessRestriction\"K\n\x13ProcessInstanceList\x12\x34\n\x06values\x18\x01 \x03(\x0b\x32$.dunedaq.druncschema.ProcessInstance2\x89\x04\n\x0eProcessManager\x12I\n\x08\x64\x65scribe\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12\x45\n\x04\x62oot\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12H\n\x07restart\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12\x45\n\x04kill\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12\x46\n\x05\x66lush\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12\x43\n\x02ps\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x12G\n\x04logs\x12\x1c.dunedaq.druncschema.Request\x1a\x1d.dunedaq.druncschema.Response\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'druncschema.process_manager_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROCESSDESCRIPTION_ENVENTRY._options = None
  _PROCESSDESCRIPTION_ENVENTRY._serialized_options = b'8\001'
  _globals['_PROCESSRESTRICTION']._serialized_start=94
  _globals['_PROCESSRESTRICTION']._serialized_end=165
  _globals['_COMMANDNOTIFICATIONMESSAGE']._serialized_start=167
  _globals['_COMMANDNOTIFICATIONMESSAGE']._serialized_end=226
  _globals['_GENERICNOTIFICATIONMESSAGE']._serialized_start=228
  _globals['_GENERICNOTIFICATIONMESSAGE']._serialized_end=273
  _globals['_EXCEPTIONNOTIFICATION']._serialized_start=276
  _globals['_EXCEPTIONNOTIFICATION']._serialized_end=461
  _globals['_EXCEPTIONNOTIFICATION_STACKLINE']._serialized_start=396
  _globals['_EXCEPTIONNOTIFICATION_STACKLINE']._serialized_end=461
  _globals['_LOGREQUEST']._serialized_start=463
  _globals['_LOGREQUEST']._serialized_end=542
  _globals['_LOGLINE']._serialized_start=544
  _globals['_LOGLINE']._serialized_end=615
  _globals['_PROCESSUUID']._serialized_start=617
  _globals['_PROCESSUUID']._serialized_end=644
  _globals['_PROCESSMETADATA']._serialized_start=646
  _globals['_PROCESSMETADATA']._serialized_end=756
  _globals['_PROCESSQUERY']._serialized_start=758
  _globals['_PROCESSQUERY']._serialized_end=867
  _globals['_PROCESSDESCRIPTION']._serialized_start=870
  _globals['_PROCESSDESCRIPTION']._serialized_end=1213
  _globals['_PROCESSDESCRIPTION_STRINGLIST']._serialized_start=1098
  _globals['_PROCESSDESCRIPTION_STRINGLIST']._serialized_end=1126
  _globals['_PROCESSDESCRIPTION_EXECANDARGS']._serialized_start=1128
  _globals['_PROCESSDESCRIPTION_EXECANDARGS']._serialized_end=1169
  _globals['_PROCESSDESCRIPTION_ENVENTRY']._serialized_start=1171
  _globals['_PROCESSDESCRIPTION_ENVENTRY']._serialized_end=1213
  _globals['_PROCESSINSTANCE']._serialized_start=1216
  _globals['_PROCESSINSTANCE']._serialized_end=1549
  _globals['_PROCESSINSTANCE_STATUSCODE']._serialized_start=1514
  _globals['_PROCESSINSTANCE_STATUSCODE']._serialized_end=1549
  _globals['_BOOTREQUEST']._serialized_start=1552
  _globals['_BOOTREQUEST']._serialized_end=1705
  _globals['_PROCESSINSTANCELIST']._serialized_start=1707
  _globals['_PROCESSINSTANCELIST']._serialized_end=1782
  _globals['_PROCESSMANAGER']._serialized_start=1785
  _globals['_PROCESSMANAGER']._serialized_end=2306
# @@protoc_insertion_point(module_scope)
