# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.media_info_type_response import MediaInfoTypeResponse
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError


class TypeApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(TypeApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def get(self, manifest_id, media_id, **kwargs):
        # type: (string_types, string_types, dict) -> MediaInfoTypeResponse
        """HLS Media Type

        :param manifest_id: Id of the hls manifest.
        :type manifest_id: string_types, required
        :param media_id: Id of the video media.
        :type media_id: string_types, required
        :return: Media-type
        :rtype: MediaInfoTypeResponse
        """

        return self.api_client.get(
            '/encoding/manifests/hls/{manifest_id}/media/{media_id}/type',
            path_params={'manifest_id': manifest_id, 'media_id': media_id},
            type=MediaInfoTypeResponse,
            **kwargs
        )
