# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class TuInterDepth(Enum):
    D1 = "1"
    D2 = "2"
    D3 = "3"
    D4 = "4"
