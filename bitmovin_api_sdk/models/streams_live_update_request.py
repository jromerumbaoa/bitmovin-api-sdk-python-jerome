# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
import pprint
import six


class StreamsLiveUpdateRequest(object):
    @poscheck_model
    def __init__(self,
                 title=None,
                 description=None,
                 config_id=None,
                 poster_url=None):
        # type: (string_types, string_types, string_types, string_types) -> None

        self._title = None
        self._description = None
        self._config_id = None
        self._poster_url = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if config_id is not None:
            self.config_id = config_id
        if poster_url is not None:
            self.poster_url = poster_url

    @property
    def openapi_types(self):
        types = {
            'title': 'string_types',
            'description': 'string_types',
            'config_id': 'string_types',
            'poster_url': 'string_types'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'title': 'title',
            'description': 'description',
            'config_id': 'configId',
            'poster_url': 'posterUrl'
        }
        return attributes

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsLiveUpdateRequest.

        The new title of the stream

        :return: The title of this StreamsLiveUpdateRequest.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsLiveUpdateRequest.

        The new title of the stream

        :param title: The title of this StreamsLiveUpdateRequest.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsLiveUpdateRequest.

        The new description of the stream

        :return: The description of this StreamsLiveUpdateRequest.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsLiveUpdateRequest.

        The new description of the stream

        :param description: The description of this StreamsLiveUpdateRequest.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def config_id(self):
        # type: () -> string_types
        """Gets the config_id of this StreamsLiveUpdateRequest.

        Id of the stream config to use

        :return: The config_id of this StreamsLiveUpdateRequest.
        :rtype: string_types
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        # type: (string_types) -> None
        """Sets the config_id of this StreamsLiveUpdateRequest.

        Id of the stream config to use

        :param config_id: The config_id of this StreamsLiveUpdateRequest.
        :type: string_types
        """

        if config_id is not None:
            if not isinstance(config_id, string_types):
                raise TypeError("Invalid type for `config_id`, type has to be `string_types`")

        self._config_id = config_id

    @property
    def poster_url(self):
        # type: () -> string_types
        """Gets the poster_url of this StreamsLiveUpdateRequest.

        URL to hosted poster image

        :return: The poster_url of this StreamsLiveUpdateRequest.
        :rtype: string_types
        """
        return self._poster_url

    @poster_url.setter
    def poster_url(self, poster_url):
        # type: (string_types) -> None
        """Sets the poster_url of this StreamsLiveUpdateRequest.

        URL to hosted poster image

        :param poster_url: The poster_url of this StreamsLiveUpdateRequest.
        :type: string_types
        """

        if poster_url is not None:
            if not isinstance(poster_url, string_types):
                raise TypeError("Invalid type for `poster_url`, type has to be `string_types`")

        self._poster_url = poster_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
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
        if not isinstance(other, StreamsLiveUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
