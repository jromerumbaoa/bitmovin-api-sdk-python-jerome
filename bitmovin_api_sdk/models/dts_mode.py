# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DtsMode(Enum):
    EXPRESS_AUDIO = "EXPRESS_AUDIO"
    DIGITAL_SURROUND = "DIGITAL_SURROUND"
