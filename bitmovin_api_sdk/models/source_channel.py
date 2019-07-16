# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.source_channel_type import SourceChannelType
import pprint
import six


class SourceChannel(object):
    @poscheck_model
    def __init__(self,
                 gain=None,
                 type_=None,
                 channel_number=None):
        # type: (float, SourceChannelType, int) -> None

        self._gain = None
        self._type = None
        self._channel_number = None
        self.discriminator = None

        if gain is not None:
            self.gain = gain
        if type_ is not None:
            self.type = type_
        if channel_number is not None:
            self.channel_number = channel_number

    @property
    def openapi_types(self):
        types = {
            'gain': 'float',
            'type': 'SourceChannelType',
            'channel_number': 'int'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'gain': 'gain',
            'type': 'type',
            'channel_number': 'channelNumber'
        }
        return attributes

    @property
    def gain(self):
        # type: () -> float
        """Gets the gain of this SourceChannel.

        Gain for this source channel. Default is 1.0.

        :return: The gain of this SourceChannel.
        :rtype: float
        """
        return self._gain

    @gain.setter
    def gain(self, gain):
        # type: (float) -> None
        """Sets the gain of this SourceChannel.

        Gain for this source channel. Default is 1.0.

        :param gain: The gain of this SourceChannel.
        :type: float
        """

        if gain is not None:
            if not isinstance(gain, (float, int)):
                raise TypeError("Invalid type for `gain`, type has to be `float`")

        self._gain = gain

    @property
    def type(self):
        # type: () -> SourceChannelType
        """Gets the type of this SourceChannel.


        :return: The type of this SourceChannel.
        :rtype: SourceChannelType
        """
        return self._type

    @type.setter
    def type(self, type_):
        # type: (SourceChannelType) -> None
        """Sets the type of this SourceChannel.


        :param type_: The type of this SourceChannel.
        :type: SourceChannelType
        """

        if type_ is not None:
            if not isinstance(type_, SourceChannelType):
                raise TypeError("Invalid type for `type`, type has to be `SourceChannelType`")

        self._type = type_

    @property
    def channel_number(self):
        # type: () -> int
        """Gets the channel_number of this SourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :return: The channel_number of this SourceChannel.
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        # type: (int) -> None
        """Sets the channel_number of this SourceChannel.

        Number of this source channel. If type is 'CHANNEL_NUMBER', this must be set.

        :param channel_number: The channel_number of this SourceChannel.
        :type: int
        """

        if channel_number is not None:
            if not isinstance(channel_number, int):
                raise TypeError("Invalid type for `channel_number`, type has to be `int`")

        self._channel_number = channel_number

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, SourceChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
