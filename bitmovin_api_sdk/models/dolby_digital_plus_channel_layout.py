# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class DolbyDigitalPlusChannelLayout(Enum):
    NONE = "NONE"
    MONO = "MONO"
    CL_STEREO = "STEREO"
    CL_SURROUND = "SURROUND"
    CL_3_1 = "3.1"
    CL_BACK_SURROUND = "BACK_SURROUND"
    CL_BACK_SURROUND_LFE = "BACK_SURROUND_LFE"
    CL_QUAD = "QUAD"
    CL_QUAD_LFE = "QUAD_LFE"
    CL_4_0 = "4.0"
    CL_4_1 = "4.1"
    CL_5_0 = "5.0"
    CL_5_1 = "5.1"
