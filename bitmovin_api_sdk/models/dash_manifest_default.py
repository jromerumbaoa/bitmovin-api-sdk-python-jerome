# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.dash_manifest import DashManifest
from bitmovin_api_sdk.models.dash_manifest_default_version import DashManifestDefaultVersion
from bitmovin_api_sdk.models.dash_profile import DashProfile
from bitmovin_api_sdk.models.manifest_type import ManifestType
import pprint
import six


class DashManifestDefault(DashManifest):
    @poscheck_model
    def __init__(self,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 id_=None,
                 type_=None,
                 outputs=None,
                 profile=None,
                 manifest_name=None,
                 namespaces=None,
                 utc_timings=None,
                 encoding_id=None,
                 version=None):
        # type: (string_types, string_types, datetime, datetime, dict, string_types, ManifestType, list[EncodingOutput], DashProfile, string_types, list[XmlNamespace], list[UtcTiming], string_types, DashManifestDefaultVersion) -> None
        super(DashManifestDefault, self).__init__(name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data, id_=id_, type_=type_, outputs=outputs, profile=profile, manifest_name=manifest_name, namespaces=namespaces, utc_timings=utc_timings)

        self._encoding_id = None
        self._version = None
        self.discriminator = None

        if encoding_id is not None:
            self.encoding_id = encoding_id
        if version is not None:
            self.version = version

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(DashManifestDefault, self), 'openapi_types'):
            types = getattr(super(DashManifestDefault, self), 'openapi_types')

        types.update({
            'encoding_id': 'string_types',
            'version': 'DashManifestDefaultVersion'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(DashManifestDefault, self), 'attribute_map'):
            attributes = getattr(super(DashManifestDefault, self), 'attribute_map')

        attributes.update({
            'encoding_id': 'encodingId',
            'version': 'version'
        })
        return attributes

    @property
    def encoding_id(self):
        # type: () -> string_types
        """Gets the encoding_id of this DashManifestDefault.

        The id of the encoding to create a default manifest from (required)

        :return: The encoding_id of this DashManifestDefault.
        :rtype: string_types
        """
        return self._encoding_id

    @encoding_id.setter
    def encoding_id(self, encoding_id):
        # type: (string_types) -> None
        """Sets the encoding_id of this DashManifestDefault.

        The id of the encoding to create a default manifest from (required)

        :param encoding_id: The encoding_id of this DashManifestDefault.
        :type: string_types
        """

        if encoding_id is not None:
            if not isinstance(encoding_id, string_types):
                raise TypeError("Invalid type for `encoding_id`, type has to be `string_types`")

        self._encoding_id = encoding_id

    @property
    def version(self):
        # type: () -> DashManifestDefaultVersion
        """Gets the version of this DashManifestDefault.

        The version of the default manifest generator

        :return: The version of this DashManifestDefault.
        :rtype: DashManifestDefaultVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        # type: (DashManifestDefaultVersion) -> None
        """Sets the version of this DashManifestDefault.

        The version of the default manifest generator

        :param version: The version of this DashManifestDefault.
        :type: DashManifestDefaultVersion
        """

        if version is not None:
            if not isinstance(version, DashManifestDefaultVersion):
                raise TypeError("Invalid type for `version`, type has to be `DashManifestDefaultVersion`")

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}
        if hasattr(super(DashManifestDefault, self), "to_dict"):
            result = super(DashManifestDefault, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = [x.to_dict() if hasattr(x, "to_dict") else x for x in value]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DashManifestDefault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
