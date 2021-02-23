# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: learner.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='learner.proto',
  package='learner',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlearner.proto\x12\x07learner\"!\n\x0cLearnRequest\x12\x11\n\thatena_id\x18\x01 \x01(\t\"\x1d\n\nLearnReply\x12\x0f\n\x07learned\x18\x01 \x01(\x08\"+\n\x16\x43reateWordCloudRequest\x12\x11\n\thatena_id\x18\x01 \x01(\t\")\n\x14\x43reateWordCloudReply\x12\x11\n\twordcloud\x18\x01 \x01(\x0c\x32\x95\x01\n\x07Learner\x12\x35\n\x05Learn\x12\x15.learner.LearnRequest\x1a\x13.learner.LearnReply\"\x00\x12S\n\x0f\x43reateWordCloud\x12\x1f.learner.CreateWordCloudRequest\x1a\x1d.learner.CreateWordCloudReply\"\x00\x62\x06proto3'
)




_LEARNREQUEST = _descriptor.Descriptor(
  name='LearnRequest',
  full_name='learner.LearnRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatena_id', full_name='learner.LearnRequest.hatena_id', index=0,
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
  serialized_start=26,
  serialized_end=59,
)


_LEARNREPLY = _descriptor.Descriptor(
  name='LearnReply',
  full_name='learner.LearnReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='learned', full_name='learner.LearnReply.learned', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=61,
  serialized_end=90,
)


_CREATEWORDCLOUDREQUEST = _descriptor.Descriptor(
  name='CreateWordCloudRequest',
  full_name='learner.CreateWordCloudRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatena_id', full_name='learner.CreateWordCloudRequest.hatena_id', index=0,
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
  serialized_start=92,
  serialized_end=135,
)


_CREATEWORDCLOUDREPLY = _descriptor.Descriptor(
  name='CreateWordCloudReply',
  full_name='learner.CreateWordCloudReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wordcloud', full_name='learner.CreateWordCloudReply.wordcloud', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=137,
  serialized_end=178,
)

DESCRIPTOR.message_types_by_name['LearnRequest'] = _LEARNREQUEST
DESCRIPTOR.message_types_by_name['LearnReply'] = _LEARNREPLY
DESCRIPTOR.message_types_by_name['CreateWordCloudRequest'] = _CREATEWORDCLOUDREQUEST
DESCRIPTOR.message_types_by_name['CreateWordCloudReply'] = _CREATEWORDCLOUDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LearnRequest = _reflection.GeneratedProtocolMessageType('LearnRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEARNREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.LearnRequest)
  })
_sym_db.RegisterMessage(LearnRequest)

LearnReply = _reflection.GeneratedProtocolMessageType('LearnReply', (_message.Message,), {
  'DESCRIPTOR' : _LEARNREPLY,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.LearnReply)
  })
_sym_db.RegisterMessage(LearnReply)

CreateWordCloudRequest = _reflection.GeneratedProtocolMessageType('CreateWordCloudRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORDCLOUDREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.CreateWordCloudRequest)
  })
_sym_db.RegisterMessage(CreateWordCloudRequest)

CreateWordCloudReply = _reflection.GeneratedProtocolMessageType('CreateWordCloudReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORDCLOUDREPLY,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.CreateWordCloudReply)
  })
_sym_db.RegisterMessage(CreateWordCloudReply)



_LEARNER = _descriptor.ServiceDescriptor(
  name='Learner',
  full_name='learner.Learner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=181,
  serialized_end=330,
  methods=[
  _descriptor.MethodDescriptor(
    name='Learn',
    full_name='learner.Learner.Learn',
    index=0,
    containing_service=None,
    input_type=_LEARNREQUEST,
    output_type=_LEARNREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateWordCloud',
    full_name='learner.Learner.CreateWordCloud',
    index=1,
    containing_service=None,
    input_type=_CREATEWORDCLOUDREQUEST,
    output_type=_CREATEWORDCLOUDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEARNER)

DESCRIPTOR.services_by_name['Learner'] = _LEARNER

# @@protoc_insertion_point(module_scope)
