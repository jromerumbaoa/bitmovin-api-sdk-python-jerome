# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.models.response_envelope import ResponseEnvelope
from bitmovin_api_sdk.models.response_error import ResponseError
from bitmovin_api_sdk.models.smooth_manifest_default import SmoothManifestDefault


class DefaultApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(DefaultApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

    def create(self, smooth_manifest_default, **kwargs):
        # type: (SmoothManifestDefault, dict) -> SmoothManifestDefault
        """Create Default Smooth Streaming Manifest

        :param smooth_manifest_default: A Default Manifest is the easiest way to create a manifest file. Its contents will be configured automatically, depending on what output your encoding creates (muxings, thumbnails, sprites, subtitles, DRM information). If you need more control, create a Custom Manifest resource instead. See [documentation](https://developer.bitmovin.com/encoding/docs/default-vs-custom-manifest) page for a comparison
        :type smooth_manifest_default: SmoothManifestDefault, required
        :return: Smooth Streaming Manifest
        :rtype: SmoothManifestDefault
        """

        return self.api_client.post(
            '/encoding/manifests/smooth/default',
            smooth_manifest_default,
            type=SmoothManifestDefault,
            **kwargs
        )
