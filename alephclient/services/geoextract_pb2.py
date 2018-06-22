# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alephclient/services/geoextract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alephclient.services import common_pb2 as alephclient_dot_services_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alephclient/services/geoextract.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n%alephclient/services/geoextract.proto\x1a!alephclient/services/common.proto\" \n\x0b\x43ountryTags\x12\x11\n\tcountries\x18\x01 \x03(\t27\n\nGeoExtract\x12)\n\x10\x45xtractCountries\x12\x05.Text\x1a\x0c.CountryTags(\x01\x62\x06proto3')
  ,
  dependencies=[alephclient_dot_services_dot_common__pb2.DESCRIPTOR,])




_COUNTRYTAGS = _descriptor.Descriptor(
  name='CountryTags',
  full_name='CountryTags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='countries', full_name='CountryTags.countries', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['CountryTags'] = _COUNTRYTAGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CountryTags = _reflection.GeneratedProtocolMessageType('CountryTags', (_message.Message,), dict(
  DESCRIPTOR = _COUNTRYTAGS,
  __module__ = 'alephclient.services.geoextract_pb2'
  # @@protoc_insertion_point(class_scope:CountryTags)
  ))
_sym_db.RegisterMessage(CountryTags)



_GEOEXTRACT = _descriptor.ServiceDescriptor(
  name='GeoExtract',
  full_name='GeoExtract',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=110,
  serialized_end=165,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExtractCountries',
    full_name='GeoExtract.ExtractCountries',
    index=0,
    containing_service=None,
    input_type=alephclient_dot_services_dot_common__pb2._TEXT,
    output_type=_COUNTRYTAGS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GEOEXTRACT)

DESCRIPTOR.services_by_name['GeoExtract'] = _GEOEXTRACT

# @@protoc_insertion_point(module_scope)
