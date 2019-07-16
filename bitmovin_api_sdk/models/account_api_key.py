# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
import pprint
import six


class AccountApiKey(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 value=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, string_types) -> None
        super(AccountApiKey, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._value = None
        self.discriminator = None

        if value is not None:
            self.value = value

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(AccountApiKey, self), 'openapi_types'):
            types = getattr(super(AccountApiKey, self), 'openapi_types')

        types.update({
            'value': 'string_types'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(AccountApiKey, self), 'attribute_map'):
            attributes = getattr(super(AccountApiKey, self), 'attribute_map')

        attributes.update({
            'value': 'value'
        })
        return attributes

    @property
    def value(self):
        # type: () -> string_types
        """Gets the value of this AccountApiKey.

        Key value for authentication with the Bitmovin API (required)

        :return: The value of this AccountApiKey.
        :rtype: string_types
        """
        return self._value

    @value.setter
    def value(self, value):
        # type: (string_types) -> None
        """Sets the value of this AccountApiKey.

        Key value for authentication with the Bitmovin API (required)

        :param value: The value of this AccountApiKey.
        :type: string_types
        """

        if value is not None:
            if not isinstance(value, string_types):
                raise TypeError("Invalid type for `value`, type has to be `string_types`")

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}
        if hasattr(super(AccountApiKey, self), "to_dict"):
            result = super(AccountApiKey, self).to_dict()

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
        if not isinstance(other, AccountApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
