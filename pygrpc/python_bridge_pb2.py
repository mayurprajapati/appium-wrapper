# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: python_bridge.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13python_bridge.proto\"9\n\nSumRequest\x12\x14\n\x0c\x66irst_number\x18\x01 \x01(\x05\x12\x15\n\rsecond_number\x18\x02 \x01(\x05\"\x1d\n\x0bSumResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"5\n\x19\x44riverDebugAddressRequest\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\"!\n\x0e\x43ommonResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32O\n\x0cPythonBridge\x12?\n\x10resolveRecaptcha\x12\x1a.DriverDebugAddressRequest\x1a\x0f.CommonResponseB\x16\n\x12grpc.bridge.pythonP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'python_bridge_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022grpc.bridge.pythonP\001'
  _globals['_SUMREQUEST']._serialized_start=23
  _globals['_SUMREQUEST']._serialized_end=80
  _globals['_SUMRESPONSE']._serialized_start=82
  _globals['_SUMRESPONSE']._serialized_end=111
  _globals['_DRIVERDEBUGADDRESSREQUEST']._serialized_start=113
  _globals['_DRIVERDEBUGADDRESSREQUEST']._serialized_end=166
  _globals['_COMMONRESPONSE']._serialized_start=168
  _globals['_COMMONRESPONSE']._serialized_end=201
  _globals['_PYTHONBRIDGE']._serialized_start=203
  _globals['_PYTHONBRIDGE']._serialized_end=282
# @@protoc_insertion_point(module_scope)
