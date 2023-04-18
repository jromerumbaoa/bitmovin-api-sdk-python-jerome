# coding: utf-8

from enum import Enum
from datetime import datetime
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.streams_config_response import StreamsConfigResponse
from bitmovin_api_sdk.models.streams_live_life_cycle import StreamsLiveLifeCycle
import pprint
import six


class StreamsLiveResponse(object):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 stream_key=None,
                 title=None,
                 description=None,
                 created_at=None,
                 life_cycle=None,
                 config=None):
        # type: (string_types, string_types, string_types, string_types, datetime, StreamsLiveLifeCycle, StreamsConfigResponse) -> None

        self._id = None
        self._stream_key = None
        self._title = None
        self._description = None
        self._created_at = None
        self._life_cycle = None
        self._config = None
        self.discriminator = None

        if id_ is not None:
            self.id = id_
        if stream_key is not None:
            self.stream_key = stream_key
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if config is not None:
            self.config = config

    @property
    def openapi_types(self):
        types = {
            'id': 'string_types',
            'stream_key': 'string_types',
            'title': 'string_types',
            'description': 'string_types',
            'created_at': 'datetime',
            'life_cycle': 'StreamsLiveLifeCycle',
            'config': 'StreamsConfigResponse'
        }

        return types

    @property
    def attribute_map(self):
        attributes = {
            'id': 'id',
            'stream_key': 'streamKey',
            'title': 'title',
            'description': 'description',
            'created_at': 'createdAt',
            'life_cycle': 'lifeCycle',
            'config': 'config'
        }
        return attributes

    @property
    def id(self):
        # type: () -> string_types
        """Gets the id of this StreamsLiveResponse.

        The identifier of the stream

        :return: The id of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._id

    @id.setter
    def id(self, id_):
        # type: (string_types) -> None
        """Sets the id of this StreamsLiveResponse.

        The identifier of the stream

        :param id_: The id of this StreamsLiveResponse.
        :type: string_types
        """

        if id_ is not None:
            if not isinstance(id_, string_types):
                raise TypeError("Invalid type for `id`, type has to be `string_types`")

        self._id = id_

    @property
    def stream_key(self):
        # type: () -> string_types
        """Gets the stream_key of this StreamsLiveResponse.

        The streamKey of the stream

        :return: The stream_key of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._stream_key

    @stream_key.setter
    def stream_key(self, stream_key):
        # type: (string_types) -> None
        """Sets the stream_key of this StreamsLiveResponse.

        The streamKey of the stream

        :param stream_key: The stream_key of this StreamsLiveResponse.
        :type: string_types
        """

        if stream_key is not None:
            if not isinstance(stream_key, string_types):
                raise TypeError("Invalid type for `stream_key`, type has to be `string_types`")

        self._stream_key = stream_key

    @property
    def title(self):
        # type: () -> string_types
        """Gets the title of this StreamsLiveResponse.

        The title of the stream

        :return: The title of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._title

    @title.setter
    def title(self, title):
        # type: (string_types) -> None
        """Sets the title of this StreamsLiveResponse.

        The title of the stream

        :param title: The title of this StreamsLiveResponse.
        :type: string_types
        """

        if title is not None:
            if not isinstance(title, string_types):
                raise TypeError("Invalid type for `title`, type has to be `string_types`")

        self._title = title

    @property
    def description(self):
        # type: () -> string_types
        """Gets the description of this StreamsLiveResponse.

        The description of the stream

        :return: The description of this StreamsLiveResponse.
        :rtype: string_types
        """
        return self._description

    @description.setter
    def description(self, description):
        # type: (string_types) -> None
        """Sets the description of this StreamsLiveResponse.

        The description of the stream

        :param description: The description of this StreamsLiveResponse.
        :type: string_types
        """

        if description is not None:
            if not isinstance(description, string_types):
                raise TypeError("Invalid type for `description`, type has to be `string_types`")

        self._description = description

    @property
    def created_at(self):
        # type: () -> datetime
        """Gets the created_at of this StreamsLiveResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :return: The created_at of this StreamsLiveResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        # type: (datetime) -> None
        """Sets the created_at of this StreamsLiveResponse.

        Creation timestamp, returned as UTC expressed in ISO 8601 format: YYYY-MM-DDThh:mm:ssZ

        :param created_at: The created_at of this StreamsLiveResponse.
        :type: datetime
        """

        if created_at is not None:
            if not isinstance(created_at, datetime):
                raise TypeError("Invalid type for `created_at`, type has to be `datetime`")

        self._created_at = created_at

    @property
    def life_cycle(self):
        # type: () -> StreamsLiveLifeCycle
        """Gets the life_cycle of this StreamsLiveResponse.

        The life cycle of the stream

        :return: The life_cycle of this StreamsLiveResponse.
        :rtype: StreamsLiveLifeCycle
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        # type: (StreamsLiveLifeCycle) -> None
        """Sets the life_cycle of this StreamsLiveResponse.

        The life cycle of the stream

        :param life_cycle: The life_cycle of this StreamsLiveResponse.
        :type: StreamsLiveLifeCycle
        """

        if life_cycle is not None:
            if not isinstance(life_cycle, StreamsLiveLifeCycle):
                raise TypeError("Invalid type for `life_cycle`, type has to be `StreamsLiveLifeCycle`")

        self._life_cycle = life_cycle

    @property
    def config(self):
        # type: () -> StreamsConfigResponse
        """Gets the config of this StreamsLiveResponse.


        :return: The config of this StreamsLiveResponse.
        :rtype: StreamsConfigResponse
        """
        return self._config

    @config.setter
    def config(self, config):
        # type: (StreamsConfigResponse) -> None
        """Sets the config of this StreamsLiveResponse.


        :param config: The config of this StreamsLiveResponse.
        :type: StreamsConfigResponse
        """

        if config is not None:
            if not isinstance(config, StreamsConfigResponse):
                raise TypeError("Invalid type for `config`, type has to be `StreamsConfigResponse`")

        self._config = config

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
        if not isinstance(other, StreamsLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
