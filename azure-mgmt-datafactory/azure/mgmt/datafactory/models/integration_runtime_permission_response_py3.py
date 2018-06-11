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

from msrest.serialization import Model


class IntegrationRuntimePermissionResponse(Model):
    """The response of granting/revoking integration runtime permission operation.

    :param shared_integration_runtime_count: The number of the integration
     runtimes to which the given data factory has been granted access.
    :type shared_integration_runtime_count: int
    """

    _attribute_map = {
        'shared_integration_runtime_count': {'key': 'sharedIntegrationRuntimeCount', 'type': 'int'},
    }

    def __init__(self, *, shared_integration_runtime_count: int=None, **kwargs) -> None:
        super(IntegrationRuntimePermissionResponse, self).__init__(**kwargs)
        self.shared_integration_runtime_count = shared_integration_runtime_count
