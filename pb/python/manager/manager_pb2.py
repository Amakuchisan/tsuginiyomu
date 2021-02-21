# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='manager.proto',
  package='manager',
  syntax='proto3',
  serialized_options=b'Z0github.com/Amakuchisan/tsuginiyomu/pb/go/manager',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmanager.proto\x12\x07manager\"#\n\x14\x43reateArticleRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"!\n\x12\x43reateArticleReply\x12\x0b\n\x03url\x18\x01 \x01(\t\"\"\n\x0eGetWordRequest\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\"y\n\x0cGetWordReply\x12\x37\n\twordCount\x18\x01 \x03(\x0b\x32$.manager.GetWordReply.WordCountEntry\x1a\x30\n\x0eWordCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"=\n\x16UpdateWordcloudRequest\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\x12\x11\n\twordcloud\x18\x02 \x01(\x0c\";\n\x14UpdateWordcloudReply\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\x12\x11\n\twordcloud\x18\x02 \x01(\x0c\"%\n\x11\x43reateUserRequest\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\"6\n\x0f\x43reateUserReply\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\x12\x11\n\twordCloud\x18\x02 \x01(\x0c\"m\n\x07\x41rticle\x12\x0b\n\x03url\x18\x01 \x01(\t\x12(\n\x04noun\x18\x02 \x03(\x0b\x32\x1a.manager.Article.NounEntry\x1a+\n\tNounEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"H\n\x11\x43reateWordRequest\x12\x10\n\x08hatenaID\x18\x01 \x01(\t\x12!\n\x07\x61rticle\x18\x02 \x01(\x0b\x32\x10.manager.Article\"\"\n\x0f\x43reateWordReply\x12\x0f\n\x07\x63reated\x18\x01 \x01(\x08\x32\xf6\x02\n\x07Manager\x12\x44\n\nCreateUser\x12\x1a.manager.CreateUserRequest\x1a\x18.manager.CreateUserReply\"\x00\x12\x44\n\nCreateWord\x12\x1a.manager.CreateWordRequest\x1a\x18.manager.CreateWordReply\"\x00\x12S\n\x0fUpdateWordcloud\x12\x1f.manager.UpdateWordcloudRequest\x1a\x1d.manager.UpdateWordcloudReply\"\x00\x12M\n\rCreateArticle\x12\x1d.manager.CreateArticleRequest\x1a\x1b.manager.CreateArticleReply\"\x00\x12;\n\x07GetWord\x12\x17.manager.GetWordRequest\x1a\x15.manager.GetWordReply\"\x00\x42\x32Z0github.com/Amakuchisan/tsuginiyomu/pb/go/managerb\x06proto3'
)




_CREATEARTICLEREQUEST = _descriptor.Descriptor(
  name='CreateArticleRequest',
  full_name='manager.CreateArticleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='manager.CreateArticleRequest.url', index=0,
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
  serialized_end=61,
)


_CREATEARTICLEREPLY = _descriptor.Descriptor(
  name='CreateArticleReply',
  full_name='manager.CreateArticleReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='manager.CreateArticleReply.url', index=0,
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
  serialized_start=63,
  serialized_end=96,
)


_GETWORDREQUEST = _descriptor.Descriptor(
  name='GetWordRequest',
  full_name='manager.GetWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.GetWordRequest.hatenaID', index=0,
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
  serialized_start=98,
  serialized_end=132,
)


_GETWORDREPLY_WORDCOUNTENTRY = _descriptor.Descriptor(
  name='WordCountEntry',
  full_name='manager.GetWordReply.WordCountEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='manager.GetWordReply.WordCountEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='manager.GetWordReply.WordCountEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=255,
)

_GETWORDREPLY = _descriptor.Descriptor(
  name='GetWordReply',
  full_name='manager.GetWordReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='wordCount', full_name='manager.GetWordReply.wordCount', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETWORDREPLY_WORDCOUNTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=255,
)


_UPDATEWORDCLOUDREQUEST = _descriptor.Descriptor(
  name='UpdateWordcloudRequest',
  full_name='manager.UpdateWordcloudRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.UpdateWordcloudRequest.hatenaID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wordcloud', full_name='manager.UpdateWordcloudRequest.wordcloud', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=257,
  serialized_end=318,
)


_UPDATEWORDCLOUDREPLY = _descriptor.Descriptor(
  name='UpdateWordcloudReply',
  full_name='manager.UpdateWordcloudReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.UpdateWordcloudReply.hatenaID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wordcloud', full_name='manager.UpdateWordcloudReply.wordcloud', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=320,
  serialized_end=379,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='manager.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.CreateUserRequest.hatenaID', index=0,
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
  serialized_start=381,
  serialized_end=418,
)


_CREATEUSERREPLY = _descriptor.Descriptor(
  name='CreateUserReply',
  full_name='manager.CreateUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.CreateUserReply.hatenaID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wordCloud', full_name='manager.CreateUserReply.wordCloud', index=1,
      number=2, type=12, cpp_type=9, label=1,
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
  serialized_start=420,
  serialized_end=474,
)


_ARTICLE_NOUNENTRY = _descriptor.Descriptor(
  name='NounEntry',
  full_name='manager.Article.NounEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='manager.Article.NounEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='manager.Article.NounEntry.value', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=542,
  serialized_end=585,
)

_ARTICLE = _descriptor.Descriptor(
  name='Article',
  full_name='manager.Article',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='manager.Article.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='noun', full_name='manager.Article.noun', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ARTICLE_NOUNENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=585,
)


_CREATEWORDREQUEST = _descriptor.Descriptor(
  name='CreateWordRequest',
  full_name='manager.CreateWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hatenaID', full_name='manager.CreateWordRequest.hatenaID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='article', full_name='manager.CreateWordRequest.article', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=587,
  serialized_end=659,
)


_CREATEWORDREPLY = _descriptor.Descriptor(
  name='CreateWordReply',
  full_name='manager.CreateWordReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='created', full_name='manager.CreateWordReply.created', index=0,
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
  serialized_start=661,
  serialized_end=695,
)

_GETWORDREPLY_WORDCOUNTENTRY.containing_type = _GETWORDREPLY
_GETWORDREPLY.fields_by_name['wordCount'].message_type = _GETWORDREPLY_WORDCOUNTENTRY
_ARTICLE_NOUNENTRY.containing_type = _ARTICLE
_ARTICLE.fields_by_name['noun'].message_type = _ARTICLE_NOUNENTRY
_CREATEWORDREQUEST.fields_by_name['article'].message_type = _ARTICLE
DESCRIPTOR.message_types_by_name['CreateArticleRequest'] = _CREATEARTICLEREQUEST
DESCRIPTOR.message_types_by_name['CreateArticleReply'] = _CREATEARTICLEREPLY
DESCRIPTOR.message_types_by_name['GetWordRequest'] = _GETWORDREQUEST
DESCRIPTOR.message_types_by_name['GetWordReply'] = _GETWORDREPLY
DESCRIPTOR.message_types_by_name['UpdateWordcloudRequest'] = _UPDATEWORDCLOUDREQUEST
DESCRIPTOR.message_types_by_name['UpdateWordcloudReply'] = _UPDATEWORDCLOUDREPLY
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserReply'] = _CREATEUSERREPLY
DESCRIPTOR.message_types_by_name['Article'] = _ARTICLE
DESCRIPTOR.message_types_by_name['CreateWordRequest'] = _CREATEWORDREQUEST
DESCRIPTOR.message_types_by_name['CreateWordReply'] = _CREATEWORDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateArticleRequest = _reflection.GeneratedProtocolMessageType('CreateArticleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEARTICLEREQUEST,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateArticleRequest)
  })
_sym_db.RegisterMessage(CreateArticleRequest)

CreateArticleReply = _reflection.GeneratedProtocolMessageType('CreateArticleReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEARTICLEREPLY,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateArticleReply)
  })
_sym_db.RegisterMessage(CreateArticleReply)

GetWordRequest = _reflection.GeneratedProtocolMessageType('GetWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWORDREQUEST,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.GetWordRequest)
  })
_sym_db.RegisterMessage(GetWordRequest)

GetWordReply = _reflection.GeneratedProtocolMessageType('GetWordReply', (_message.Message,), {

  'WordCountEntry' : _reflection.GeneratedProtocolMessageType('WordCountEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETWORDREPLY_WORDCOUNTENTRY,
    '__module__' : 'manager_pb2'
    # @@protoc_insertion_point(class_scope:manager.GetWordReply.WordCountEntry)
    })
  ,
  'DESCRIPTOR' : _GETWORDREPLY,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.GetWordReply)
  })
_sym_db.RegisterMessage(GetWordReply)
_sym_db.RegisterMessage(GetWordReply.WordCountEntry)

UpdateWordcloudRequest = _reflection.GeneratedProtocolMessageType('UpdateWordcloudRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEWORDCLOUDREQUEST,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.UpdateWordcloudRequest)
  })
_sym_db.RegisterMessage(UpdateWordcloudRequest)

UpdateWordcloudReply = _reflection.GeneratedProtocolMessageType('UpdateWordcloudReply', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEWORDCLOUDREPLY,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.UpdateWordcloudReply)
  })
_sym_db.RegisterMessage(UpdateWordcloudReply)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserReply = _reflection.GeneratedProtocolMessageType('CreateUserReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREPLY,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateUserReply)
  })
_sym_db.RegisterMessage(CreateUserReply)

Article = _reflection.GeneratedProtocolMessageType('Article', (_message.Message,), {

  'NounEntry' : _reflection.GeneratedProtocolMessageType('NounEntry', (_message.Message,), {
    'DESCRIPTOR' : _ARTICLE_NOUNENTRY,
    '__module__' : 'manager_pb2'
    # @@protoc_insertion_point(class_scope:manager.Article.NounEntry)
    })
  ,
  'DESCRIPTOR' : _ARTICLE,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.Article)
  })
_sym_db.RegisterMessage(Article)
_sym_db.RegisterMessage(Article.NounEntry)

CreateWordRequest = _reflection.GeneratedProtocolMessageType('CreateWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORDREQUEST,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateWordRequest)
  })
_sym_db.RegisterMessage(CreateWordRequest)

CreateWordReply = _reflection.GeneratedProtocolMessageType('CreateWordReply', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORDREPLY,
  '__module__' : 'manager_pb2'
  # @@protoc_insertion_point(class_scope:manager.CreateWordReply)
  })
_sym_db.RegisterMessage(CreateWordReply)


DESCRIPTOR._options = None
_GETWORDREPLY_WORDCOUNTENTRY._options = None
_ARTICLE_NOUNENTRY._options = None

_MANAGER = _descriptor.ServiceDescriptor(
  name='Manager',
  full_name='manager.Manager',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=698,
  serialized_end=1072,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='manager.Manager.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateWord',
    full_name='manager.Manager.CreateWord',
    index=1,
    containing_service=None,
    input_type=_CREATEWORDREQUEST,
    output_type=_CREATEWORDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateWordcloud',
    full_name='manager.Manager.UpdateWordcloud',
    index=2,
    containing_service=None,
    input_type=_UPDATEWORDCLOUDREQUEST,
    output_type=_UPDATEWORDCLOUDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateArticle',
    full_name='manager.Manager.CreateArticle',
    index=3,
    containing_service=None,
    input_type=_CREATEARTICLEREQUEST,
    output_type=_CREATEARTICLEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetWord',
    full_name='manager.Manager.GetWord',
    index=4,
    containing_service=None,
    input_type=_GETWORDREQUEST,
    output_type=_GETWORDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGER)

DESCRIPTOR.services_by_name['Manager'] = _MANAGER

# @@protoc_insertion_point(module_scope)
