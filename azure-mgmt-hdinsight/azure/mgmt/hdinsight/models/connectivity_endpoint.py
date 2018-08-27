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


class ConnectivityEndpoint(Model):
    """The connectivity properties.

    :param name: The name of the endpoint.
    :type name: str
    :param protocol: The protocol of the endpoint.
    :type protocol: str
    :param location: The location of the endpoint.
    :type location: str
    :param port: The port to connect to.
    :type port: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'protocol': {'key': 'protocol', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'port': {'key': 'port', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ConnectivityEndpoint, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.protocol = kwargs.get('protocol', None)
        self.location = kwargs.get('location', None)
        self.port = kwargs.get('port', None)