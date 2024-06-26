# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model


class AnalyticsHttpRequestType(Enum):
    DRM_LICENSE_WIDEVINE_ = "DRM_LICENSE_WIDEVINE,"
    MEDIA_THUMBNAILS_ = "MEDIA_THUMBNAILS,"
    MEDIA_VIDEO_ = "MEDIA_VIDEO,"
    MEDIA_AUDIO_ = "MEDIA_AUDIO,"
    MEDIA_PROGRESSIVE_ = "MEDIA_PROGRESSIVE,"
    MEDIA_SUBTITLES_ = "MEDIA_SUBTITLES,"
    MANIFEST_DASH_ = "MANIFEST_DASH,"
    MANIFEST_HLS_MASTER_ = "MANIFEST_HLS_MASTER,"
    MANIFEST_HLS_VARIANT_ = "MANIFEST_HLS_VARIANT,"
    MANIFEST_SMOOTH_ = "MANIFEST_SMOOTH,"
    KEY_HLS_AES_ = "KEY_HLS_AES,"
    UNKNOWN = "UNKNOWN"
