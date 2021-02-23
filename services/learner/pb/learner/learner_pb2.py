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
  serialized_pb=b'\n\rlearner.proto\x12\x07learner\"!\n\x0cLearnRequest\x12\x11\n\thatena_id\x18\x01 \x01(\t\"\x1d\n\nLearnReply\x12\x0f\n\x07learned\x18\x01 \x01(\x08\"+\n\x16\x43reateWordCloudRequest\x12\x11\n\thatena_id\x18\x01 \x01(\t\")\n\x14\x43reateWordCloudReply\x12\x11\n\twordcloud\x18\x01 \x01(\x0c\")\n\x14GetSuggestionRequest\x12\x11\n\thatena_id\x18\x01 \x01(\t\"8\n\nSuggestion\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\r\">\n\x12GetSuggestionReply\x12(\n\x0bsuggestions\x18\x01 \x03(\x0b\x32\x13.learner.Suggestion2\xe4\x01\n\x07Learner\x12\x35\n\x05Learn\x12\x15.learner.LearnRequest\x1a\x13.learner.LearnReply\"\x00\x12M\n\rGetSuggestion\x12\x1d.learner.GetSuggestionRequest\x1a\x1b.learner.GetSuggestionReply\"\x00\x12S\n\x0f\x43reateWordCloud\x12\x1f.learner.CreateWordCloudRequest\x1a\x1d.learner.CreateWordCloudReply\"\x00\x62\x06proto3'
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


_GETSUGGESTIONREQUEST = _descriptor.Descriptor(
  name='GetSuggestionRequest',
  full_name='learner.GetSuggestionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatena_id', full_name='learner.GetSuggestionRequest.hatena_id', index=0,
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
  serialized_start=180,
  serialized_end=221,
)


_SUGGESTION = _descriptor.Descriptor(
  name='Suggestion',
  full_name='learner.Suggestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='learner.Suggestion.link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='learner.Suggestion.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='learner.Suggestion.score', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=223,
  serialized_end=279,
)


_GETSUGGESTIONREPLY = _descriptor.Descriptor(
  name='GetSuggestionReply',
  full_name='learner.GetSuggestionReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='suggestions', full_name='learner.GetSuggestionReply.suggestions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=281,
  serialized_end=343,
)

_GETSUGGESTIONREPLY.fields_by_name['suggestions'].message_type = _SUGGESTION
DESCRIPTOR.message_types_by_name['LearnRequest'] = _LEARNREQUEST
DESCRIPTOR.message_types_by_name['LearnReply'] = _LEARNREPLY
DESCRIPTOR.message_types_by_name['CreateWordCloudRequest'] = _CREATEWORDCLOUDREQUEST
DESCRIPTOR.message_types_by_name['CreateWordCloudReply'] = _CREATEWORDCLOUDREPLY
DESCRIPTOR.message_types_by_name['GetSuggestionRequest'] = _GETSUGGESTIONREQUEST
DESCRIPTOR.message_types_by_name['Suggestion'] = _SUGGESTION
DESCRIPTOR.message_types_by_name['GetSuggestionReply'] = _GETSUGGESTIONREPLY
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

GetSuggestionRequest = _reflection.GeneratedProtocolMessageType('GetSuggestionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSUGGESTIONREQUEST,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.GetSuggestionRequest)
  })
_sym_db.RegisterMessage(GetSuggestionRequest)

Suggestion = _reflection.GeneratedProtocolMessageType('Suggestion', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTION,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.Suggestion)
  })
_sym_db.RegisterMessage(Suggestion)

GetSuggestionReply = _reflection.GeneratedProtocolMessageType('GetSuggestionReply', (_message.Message,), {
  'DESCRIPTOR' : _GETSUGGESTIONREPLY,
  '__module__' : 'learner_pb2'
  # @@protoc_insertion_point(class_scope:learner.GetSuggestionReply)
  })
_sym_db.RegisterMessage(GetSuggestionReply)



_LEARNER = _descriptor.ServiceDescriptor(
  name='Learner',
  full_name='learner.Learner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=346,
  serialized_end=574,
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
    name='GetSuggestion',
    full_name='learner.Learner.GetSuggestion',
    index=1,
    containing_service=None,
    input_type=_GETSUGGESTIONREQUEST,
    output_type=_GETSUGGESTIONREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateWordCloud',
    full_name='learner.Learner.CreateWordCloud',
    index=2,
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
