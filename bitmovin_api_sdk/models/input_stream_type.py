# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class InputStreamType(Enum):
    INGEST = "INGEST"
    CONCATENATION = "CONCATENATION"
    TRIMMING_TIME_BASED = "TRIMMING_TIME_BASED"
    TRIMMING_TIME_CODE_TRACK = "TRIMMING_TIME_CODE_TRACK"
    TRIMMING_H264_PICTURE_TIMING = "TRIMMING_H264_PICTURE_TIMING"
    SIDECAR_DOLBY_VISION_METADATA = "SIDECAR_DOLBY_VISION_METADATA"
    AUDIO_MIX = "AUDIO_MIX"
    FILE = "FILE"
    CAPTION_CEA608 = "CAPTION_CEA608"
    CAPTION_CEA708 = "CAPTION_CEA708"
    DVB_TELETEXT = "DVB_TELETEXT"
    DOLBY_ATMOS = "DOLBY_ATMOS"
