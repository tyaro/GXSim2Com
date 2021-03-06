# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: melsec.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='melsec.proto',
  package='melseccom',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cmelsec.proto\x12\tmelseccom\"\x1b\n\x0cHelloMessage\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1f\n\nReplyHello\x12\x11\n\treply_msg\x18\x01 \x01(\t\"&\n\x07ReadMsg\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x05\"\x1e\n\tReplyRead\x12\x11\n\treply_msg\x18\x01 \x01(\t\")\n\x08WriteMsg\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"\x1f\n\nReplyWrite\x12\x11\n\treply_msg\x18\x01 \x01(\t2\xe3\x03\n\x10MelsecComService\x12@\n\x08HelloMsg\x12\x17.melseccom.HelloMessage\x1a\x15.melseccom.ReplyHello\"\x00(\x01\x30\x01\x12@\n\x0e\x42lockReadFloat\x12\x12.melseccom.ReadMsg\x1a\x14.melseccom.ReplyRead\"\x00(\x01\x30\x01\x12?\n\rBlockReadWord\x12\x12.melseccom.ReadMsg\x1a\x14.melseccom.ReplyRead\"\x00(\x01\x30\x01\x12>\n\x0c\x42lockReadBit\x12\x12.melseccom.ReadMsg\x1a\x14.melseccom.ReplyRead\"\x00(\x01\x30\x01\x12\x43\n\x0f\x42lockWriteFloat\x12\x13.melseccom.WriteMsg\x1a\x15.melseccom.ReplyWrite\"\x00(\x01\x30\x01\x12\x42\n\x0e\x42lockWriteWord\x12\x13.melseccom.WriteMsg\x1a\x15.melseccom.ReplyWrite\"\x00(\x01\x30\x01\x12\x41\n\rBlockWriteBit\x12\x13.melseccom.WriteMsg\x1a\x15.melseccom.ReplyWrite\"\x00(\x01\x30\x01\x62\x06proto3'
)




_HELLOMESSAGE = _descriptor.Descriptor(
  name='HelloMessage',
  full_name='melseccom.HelloMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='melseccom.HelloMessage.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=54,
)


_REPLYHELLO = _descriptor.Descriptor(
  name='ReplyHello',
  full_name='melseccom.ReplyHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_msg', full_name='melseccom.ReplyHello.reply_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=87,
)


_READMSG = _descriptor.Descriptor(
  name='ReadMsg',
  full_name='melseccom.ReadMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='melseccom.ReadMsg.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='melseccom.ReadMsg.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=127,
)


_REPLYREAD = _descriptor.Descriptor(
  name='ReplyRead',
  full_name='melseccom.ReplyRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_msg', full_name='melseccom.ReplyRead.reply_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=159,
)


_WRITEMSG = _descriptor.Descriptor(
  name='WriteMsg',
  full_name='melseccom.WriteMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='melseccom.WriteMsg.device', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='melseccom.WriteMsg.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=202,
)


_REPLYWRITE = _descriptor.Descriptor(
  name='ReplyWrite',
  full_name='melseccom.ReplyWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply_msg', full_name='melseccom.ReplyWrite.reply_msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=235,
)

DESCRIPTOR.message_types_by_name['HelloMessage'] = _HELLOMESSAGE
DESCRIPTOR.message_types_by_name['ReplyHello'] = _REPLYHELLO
DESCRIPTOR.message_types_by_name['ReadMsg'] = _READMSG
DESCRIPTOR.message_types_by_name['ReplyRead'] = _REPLYREAD
DESCRIPTOR.message_types_by_name['WriteMsg'] = _WRITEMSG
DESCRIPTOR.message_types_by_name['ReplyWrite'] = _REPLYWRITE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloMessage = _reflection.GeneratedProtocolMessageType('HelloMessage', (_message.Message,), {
  'DESCRIPTOR' : _HELLOMESSAGE,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.HelloMessage)
  })
_sym_db.RegisterMessage(HelloMessage)

ReplyHello = _reflection.GeneratedProtocolMessageType('ReplyHello', (_message.Message,), {
  'DESCRIPTOR' : _REPLYHELLO,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.ReplyHello)
  })
_sym_db.RegisterMessage(ReplyHello)

ReadMsg = _reflection.GeneratedProtocolMessageType('ReadMsg', (_message.Message,), {
  'DESCRIPTOR' : _READMSG,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.ReadMsg)
  })
_sym_db.RegisterMessage(ReadMsg)

ReplyRead = _reflection.GeneratedProtocolMessageType('ReplyRead', (_message.Message,), {
  'DESCRIPTOR' : _REPLYREAD,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.ReplyRead)
  })
_sym_db.RegisterMessage(ReplyRead)

WriteMsg = _reflection.GeneratedProtocolMessageType('WriteMsg', (_message.Message,), {
  'DESCRIPTOR' : _WRITEMSG,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.WriteMsg)
  })
_sym_db.RegisterMessage(WriteMsg)

ReplyWrite = _reflection.GeneratedProtocolMessageType('ReplyWrite', (_message.Message,), {
  'DESCRIPTOR' : _REPLYWRITE,
  '__module__' : 'melsec_pb2'
  # @@protoc_insertion_point(class_scope:melseccom.ReplyWrite)
  })
_sym_db.RegisterMessage(ReplyWrite)



_MELSECCOMSERVICE = _descriptor.ServiceDescriptor(
  name='MelsecComService',
  full_name='melseccom.MelsecComService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=238,
  serialized_end=721,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloMsg',
    full_name='melseccom.MelsecComService.HelloMsg',
    index=0,
    containing_service=None,
    input_type=_HELLOMESSAGE,
    output_type=_REPLYHELLO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockReadFloat',
    full_name='melseccom.MelsecComService.BlockReadFloat',
    index=1,
    containing_service=None,
    input_type=_READMSG,
    output_type=_REPLYREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockReadWord',
    full_name='melseccom.MelsecComService.BlockReadWord',
    index=2,
    containing_service=None,
    input_type=_READMSG,
    output_type=_REPLYREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockReadBit',
    full_name='melseccom.MelsecComService.BlockReadBit',
    index=3,
    containing_service=None,
    input_type=_READMSG,
    output_type=_REPLYREAD,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockWriteFloat',
    full_name='melseccom.MelsecComService.BlockWriteFloat',
    index=4,
    containing_service=None,
    input_type=_WRITEMSG,
    output_type=_REPLYWRITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockWriteWord',
    full_name='melseccom.MelsecComService.BlockWriteWord',
    index=5,
    containing_service=None,
    input_type=_WRITEMSG,
    output_type=_REPLYWRITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockWriteBit',
    full_name='melseccom.MelsecComService.BlockWriteBit',
    index=6,
    containing_service=None,
    input_type=_WRITEMSG,
    output_type=_REPLYWRITE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MELSECCOMSERVICE)

DESCRIPTOR.services_by_name['MelsecComService'] = _MELSECCOMSERVICE

# @@protoc_insertion_point(module_scope)
