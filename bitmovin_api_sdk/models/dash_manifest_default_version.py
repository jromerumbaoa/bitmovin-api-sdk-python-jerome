# coding: utf-8

from enum import Enum
from six import string_types
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DashManifestDefaultVersion(Enum):
    V1 = "V1"
