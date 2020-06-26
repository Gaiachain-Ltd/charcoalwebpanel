# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entity.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import agent_pb2 as agent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entity.proto',
  package='gaiachain',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0c\x65ntity.proto\x12\tgaiachain\x1a\x0b\x61gent.proto\"\xef\x01\n\x07Package\x12\n\n\x02id\x18\x01 \x01(\t\x12,\n\x04type\x18\x02 \x01(\x0e\x32\x1e.gaiachain.Package.PackageType\x12#\n\x08\x65ntities\x18\x03 \x03(\x0b\x32\x11.gaiachain.Entity\x12 \n\x04plot\x18\x04 \x01(\x0b\x32\x12.gaiachain.Package\x12#\n\x07harvest\x18\x05 \x01(\x0b\x32\x12.gaiachain.Package\">\n\x0bPackageType\x12\r\n\tZERO_TYPE\x10\x00\x12\x08\n\x04PLOT\x10\x01\x12\x0b\n\x07HARVEST\x10\x02\x12\t\n\x05TRUCK\x10\x03\"\xc2\x05\n\x06\x45ntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\x12(\n\x06status\x18\x05 \x01(\x0e\x32\x18.gaiachain.Entity.Status\x12\x16\n\x0e\x62\x65ginning_date\x18\x07 \x01(\x04\x12\x0e\n\x06parcel\x18\x08 \x01(\t\x12\x0f\n\x07village\x18\t \x01(\t\x12\x13\n\x0btree_specie\x18\n \x01(\t\x12\x13\n\x0b\x65nding_date\x18\x0b \x01(\x04\x12\x17\n\x0fnumber_of_trees\x18\x0c \x01(\x04\x12\x0c\n\x04oven\x18\r \x01(\t\x12\x11\n\toven_type\x18\x0e \x01(\t\x12\x13\n\x0boven_height\x18\x0f \x01(\x04\x12\x12\n\noven_width\x18\x10 \x01(\x04\x12\x13\n\x0boven_length\x18\x11 \x01(\x04\x12\x10\n\x08\x65nd_date\x18\x12 \x01(\x04\x12\x14\n\x0cloading_date\x18\x13 \x01(\x04\x12\x14\n\x0cplate_number\x18\x14 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x15 \x01(\t\x12\x0c\n\x04\x62\x61gs\x18\x16 \x03(\t\x12\x18\n\x10\x64ocuments_photos\x18\x17 \x03(\t\x12\x16\n\x0ereceipt_photos\x18\x18 \x03(\t\x12\x16\n\x0ereception_date\x18\x19 \x01(\x04\x12%\n\x08location\x18\x1a \x01(\x0b\x32\x13.gaiachain.Location\x12\x1e\n\x04user\x18\x1b \x01(\x0b\x32\x10.gaiachain.Agent\"\xa1\x01\n\x06Status\x12\x0f\n\x0bZERO_STATUS\x10\x00\x12\x15\n\x11LOGGING_BEGINNING\x10\x01\x12\x12\n\x0eLOGGING_ENDING\x10\x02\x12\x1b\n\x17\x43\x41RBONIZATION_BEGINNING\x10\x03\x12\x18\n\x14\x43\x41RBONIZATION_ENDING\x10\x04\x12\x15\n\x11LOADING_TRANSPORT\x10\x05\x12\r\n\tRECEPTION\x10\x06\"\xdc\x01\n\x0cReplantation\x12 \n\x04plot\x18\x01 \x01(\x0b\x32\x12.gaiachain.Package\x12\x15\n\rtrees_planted\x18\x02 \x01(\x04\x12\x13\n\x0btree_specie\x18\x03 \x01(\t\x12\x1e\n\x04user\x18\x04 \x01(\x0b\x32\x10.gaiachain.Agent\x12%\n\x08location\x18\x05 \x01(\x0b\x32\x13.gaiachain.Location\x12\x16\n\x0e\x62\x65ginning_date\x18\x06 \x01(\x04\x12\x13\n\x0b\x65nding_date\x18\x07 \x01(\x04\x12\n\n\x02id\x18\x08 \x01(\x04\"%\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0c\n\x04long\x18\x02 \x01(\x01\x62\x06proto3'
  ,
  dependencies=[agent__pb2.DESCRIPTOR,])



_PACKAGE_PACKAGETYPE = _descriptor.EnumDescriptor(
  name='PackageType',
  full_name='gaiachain.Package.PackageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZERO_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLOT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARVEST', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUCK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=218,
  serialized_end=280,
)
_sym_db.RegisterEnumDescriptor(_PACKAGE_PACKAGETYPE)

_ENTITY_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='gaiachain.Entity.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZERO_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGGING_BEGINNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGGING_ENDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARBONIZATION_BEGINNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARBONIZATION_ENDING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOADING_TRANSPORT', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECEPTION', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=828,
  serialized_end=989,
)
_sym_db.RegisterEnumDescriptor(_ENTITY_STATUS)


_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='gaiachain.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gaiachain.Package.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='gaiachain.Package.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entities', full_name='gaiachain.Package.entities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plot', full_name='gaiachain.Package.plot', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='harvest', full_name='gaiachain.Package.harvest', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PACKAGE_PACKAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=280,
)


_ENTITY = _descriptor.Descriptor(
  name='Entity',
  full_name='gaiachain.Entity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gaiachain.Entity.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='gaiachain.Entity.timestamp', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='gaiachain.Entity.status', index=2,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginning_date', full_name='gaiachain.Entity.beginning_date', index=3,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parcel', full_name='gaiachain.Entity.parcel', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='village', full_name='gaiachain.Entity.village', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tree_specie', full_name='gaiachain.Entity.tree_specie', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ending_date', full_name='gaiachain.Entity.ending_date', index=7,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_trees', full_name='gaiachain.Entity.number_of_trees', index=8,
      number=12, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oven', full_name='gaiachain.Entity.oven', index=9,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oven_type', full_name='gaiachain.Entity.oven_type', index=10,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oven_height', full_name='gaiachain.Entity.oven_height', index=11,
      number=15, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oven_width', full_name='gaiachain.Entity.oven_width', index=12,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='oven_length', full_name='gaiachain.Entity.oven_length', index=13,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='gaiachain.Entity.end_date', index=14,
      number=18, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loading_date', full_name='gaiachain.Entity.loading_date', index=15,
      number=19, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plate_number', full_name='gaiachain.Entity.plate_number', index=16,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination', full_name='gaiachain.Entity.destination', index=17,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bags', full_name='gaiachain.Entity.bags', index=18,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='documents_photos', full_name='gaiachain.Entity.documents_photos', index=19,
      number=23, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receipt_photos', full_name='gaiachain.Entity.receipt_photos', index=20,
      number=24, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reception_date', full_name='gaiachain.Entity.reception_date', index=21,
      number=25, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='gaiachain.Entity.location', index=22,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='gaiachain.Entity.user', index=23,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENTITY_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=283,
  serialized_end=989,
)


_REPLANTATION = _descriptor.Descriptor(
  name='Replantation',
  full_name='gaiachain.Replantation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plot', full_name='gaiachain.Replantation.plot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trees_planted', full_name='gaiachain.Replantation.trees_planted', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tree_specie', full_name='gaiachain.Replantation.tree_specie', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='gaiachain.Replantation.user', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='gaiachain.Replantation.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginning_date', full_name='gaiachain.Replantation.beginning_date', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ending_date', full_name='gaiachain.Replantation.ending_date', index=6,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='gaiachain.Replantation.id', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=992,
  serialized_end=1212,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='gaiachain.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lat', full_name='gaiachain.Location.lat', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long', full_name='gaiachain.Location.long', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1214,
  serialized_end=1251,
)

_PACKAGE.fields_by_name['type'].enum_type = _PACKAGE_PACKAGETYPE
_PACKAGE.fields_by_name['entities'].message_type = _ENTITY
_PACKAGE.fields_by_name['plot'].message_type = _PACKAGE
_PACKAGE.fields_by_name['harvest'].message_type = _PACKAGE
_PACKAGE_PACKAGETYPE.containing_type = _PACKAGE
_ENTITY.fields_by_name['status'].enum_type = _ENTITY_STATUS
_ENTITY.fields_by_name['location'].message_type = _LOCATION
_ENTITY.fields_by_name['user'].message_type = agent__pb2._AGENT
_ENTITY_STATUS.containing_type = _ENTITY
_REPLANTATION.fields_by_name['plot'].message_type = _PACKAGE
_REPLANTATION.fields_by_name['user'].message_type = agent__pb2._AGENT
_REPLANTATION.fields_by_name['location'].message_type = _LOCATION
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE
DESCRIPTOR.message_types_by_name['Entity'] = _ENTITY
DESCRIPTOR.message_types_by_name['Replantation'] = _REPLANTATION
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Package = _reflection.GeneratedProtocolMessageType('Package', (_message.Message,), {
  'DESCRIPTOR' : _PACKAGE,
  '__module__' : 'entity_pb2'
  # @@protoc_insertion_point(class_scope:gaiachain.Package)
  })
_sym_db.RegisterMessage(Package)

Entity = _reflection.GeneratedProtocolMessageType('Entity', (_message.Message,), {
  'DESCRIPTOR' : _ENTITY,
  '__module__' : 'entity_pb2'
  # @@protoc_insertion_point(class_scope:gaiachain.Entity)
  })
_sym_db.RegisterMessage(Entity)

Replantation = _reflection.GeneratedProtocolMessageType('Replantation', (_message.Message,), {
  'DESCRIPTOR' : _REPLANTATION,
  '__module__' : 'entity_pb2'
  # @@protoc_insertion_point(class_scope:gaiachain.Replantation)
  })
_sym_db.RegisterMessage(Replantation)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'entity_pb2'
  # @@protoc_insertion_point(class_scope:gaiachain.Location)
  })
_sym_db.RegisterMessage(Location)


# @@protoc_insertion_point(module_scope)
