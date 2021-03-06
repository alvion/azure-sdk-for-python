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


class ClientDiscoveryForServiceSpecification(Model):
    """Class to represent shoebox service specification in json client discovery.

    :param log_specifications: List of log specifications of this operation.
    :type log_specifications:
     list[~azure.mgmt.recoveryservices.models.ClientDiscoveryForLogSpecification]
    """

    _attribute_map = {
        'log_specifications': {'key': 'logSpecifications', 'type': '[ClientDiscoveryForLogSpecification]'},
    }

    def __init__(self, **kwargs):
        super(ClientDiscoveryForServiceSpecification, self).__init__(**kwargs)
        self.log_specifications = kwargs.get('log_specifications', None)
