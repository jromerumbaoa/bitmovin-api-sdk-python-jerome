# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class ProfileH264(Enum):
    BASELINE = "BASELINE"
    MAIN = "MAIN"
    HIGH = "HIGH"
