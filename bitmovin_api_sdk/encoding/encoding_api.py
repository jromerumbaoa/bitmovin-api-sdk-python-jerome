# coding: utf-8

from __future__ import absolute_import

from bitmovin_api_sdk.common import BaseApi, BitmovinApiLoggerBase
from bitmovin_api_sdk.common.poscheck import poscheck_except
from bitmovin_api_sdk.encoding.inputs.inputs_api import InputsApi
from bitmovin_api_sdk.encoding.outputs.outputs_api import OutputsApi
from bitmovin_api_sdk.encoding.configurations.configurations_api import ConfigurationsApi
from bitmovin_api_sdk.encoding.filters.filters_api import FiltersApi
from bitmovin_api_sdk.encoding.encodings.encodings_api import EncodingsApi
from bitmovin_api_sdk.encoding.manifests.manifests_api import ManifestsApi
from bitmovin_api_sdk.encoding.infrastructure.infrastructure_api import InfrastructureApi
from bitmovin_api_sdk.encoding.statistics.statistics_api import StatisticsApi
from bitmovin_api_sdk.encoding.errorDefinitions.error_definitions_api import ErrorDefinitionsApi


class EncodingApi(BaseApi):
    @poscheck_except(2)
    def __init__(self, api_key, tenant_org_id=None, base_url=None, logger=None):
        # type: (str, str, str, BitmovinApiLoggerBase) -> None

        super(EncodingApi, self).__init__(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.inputs = InputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.outputs = OutputsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.configurations = ConfigurationsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.filters = FiltersApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.encodings = EncodingsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.manifests = ManifestsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.infrastructure = InfrastructureApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.statistics = StatisticsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )

        self.errorDefinitions = ErrorDefinitionsApi(
            api_key=api_key,
            tenant_org_id=tenant_org_id,
            base_url=base_url,
            logger=logger
        )
