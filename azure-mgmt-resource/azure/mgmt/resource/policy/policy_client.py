# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ..version import VERSION


class PolicyClientConfiguration(AzureConfiguration):
    """Configuration for PolicyClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(PolicyClientConfiguration, self).__init__(base_url)

        self.add_user_agent('policyclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class PolicyClient(MultiApiClientMixin, SDKClient):
    """To manage and control access to your resources, you can define customized policies and assign them at a scope.

    :ivar config: Configuration for client.
    :vartype config: PolicyClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION='2018-03-01'
    _PROFILE_TAG = "azure.mgmt.resource.policy.PolicyClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = PolicyClientConfiguration(credentials, subscription_id, base_url)
        super(PolicyClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2015-10-01-preview: :mod:`v2015_10_01_preview.models<azure.mgmt.resource.policy.v2015_10_01_preview.models>`
           * 2016-04-01: :mod:`v2016_04_01.models<azure.mgmt.resource.policy.v2016_04_01.models>`
           * 2016-12-01: :mod:`v2016_12_01.models<azure.mgmt.resource.policy.v2016_12_01.models>`
           * 2017-06-01-preview: :mod:`v2017_06_01_preview.models<azure.mgmt.resource.policy.v2017_06_01_preview.models>`
           * 2018-03-01: :mod:`v2018_03_01.models<azure.mgmt.resource.policy.v2018_03_01.models>`
        """
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview import models
            return models
        elif api_version == '2016-04-01':
            from .v2016_04_01 import models
            return models
        elif api_version == '2016-12-01':
            from .v2016_12_01 import models
            return models
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview import models
            return models
        elif api_version == '2018-03-01':
            from .v2018_03_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def policy_assignments(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyAssignmentsOperations>`
           * 2016-04-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyAssignmentsOperations>`
           * 2016-12-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyAssignmentsOperations>`
           * 2017-06-01-preview: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicyAssignmentsOperations>`
           * 2018-03-01: :class:`PolicyAssignmentsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyAssignmentsOperations>`
        """
        api_version = self._get_api_version('policy_assignments')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicyAssignmentsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyAssignmentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_definitions(self):
        """Instance depends on the API version:

           * 2015-10-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2015_10_01_preview.operations.PolicyDefinitionsOperations>`
           * 2016-04-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_04_01.operations.PolicyDefinitionsOperations>`
           * 2016-12-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2016_12_01.operations.PolicyDefinitionsOperations>`
           * 2017-06-01-preview: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicyDefinitionsOperations>`
           * 2018-03-01: :class:`PolicyDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicyDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_definitions')
        if api_version == '2015-10-01-preview':
            from .v2015_10_01_preview.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-04-01':
            from .v2016_04_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2016-12-01':
            from .v2016_12_01.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicyDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicyDefinitionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def policy_set_definitions(self):
        """Instance depends on the API version:

           * 2017-06-01-preview: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2017_06_01_preview.operations.PolicySetDefinitionsOperations>`
           * 2018-03-01: :class:`PolicySetDefinitionsOperations<azure.mgmt.resource.policy.v2018_03_01.operations.PolicySetDefinitionsOperations>`
        """
        api_version = self._get_api_version('policy_set_definitions')
        if api_version == '2017-06-01-preview':
            from .v2017_06_01_preview.operations import PolicySetDefinitionsOperations as OperationClass
        elif api_version == '2018-03-01':
            from .v2018_03_01.operations import PolicySetDefinitionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
