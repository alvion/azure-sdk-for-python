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

from .tracked_resource import TrackedResource


class SqlVirtualMachineGroup(TrackedResource):
    """A SQL virtual machine group.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :ivar provisioning_state: Provisioning state to track the aysnc operation
     status.
    :vartype provisioning_state: str
    :param sql_image_offer: SQL image offer.
    :type sql_image_offer: str
    :param sql_image_sku: SQL image sku. Possible values include: 'Developer',
     'Express', 'Standard', 'Enterprise', 'Web'
    :type sql_image_sku: str or
     ~azure.mgmt.sqlvirtualmachine.models.SqlImageSku
    :ivar scale_type: Scale type: HA or ReadOnly. Possible values include:
     'HA'
    :vartype scale_type: str or ~azure.mgmt.sqlvirtualmachine.models.ScaleType
    :ivar cluster_manager_type: Type of the cluster manager: Windows Server
     Failover Cluster (WSFC) | NONE, implied by the scale type of the group and
     the OS type. Possible values include: 'WSFC'
    :vartype cluster_manager_type: str or
     ~azure.mgmt.sqlvirtualmachine.models.ClusterManagerType
    :ivar cluster_configuration: Cluster type. Possible values include:
     'Domainful'
    :vartype cluster_configuration: str or
     ~azure.mgmt.sqlvirtualmachine.models.ClusterConfiguration
    :param wsfc_domain_profile: Cluster AD domain profile.
    :type wsfc_domain_profile:
     ~azure.mgmt.sqlvirtualmachine.models.WSFCDomainProfile
    :param domainless_profile: Cluster domainless profile.
    :type domainless_profile:
     ~azure.mgmt.sqlvirtualmachine.models.DomainlessProfile
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'scale_type': {'readonly': True},
        'cluster_manager_type': {'readonly': True},
        'cluster_configuration': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'sql_image_offer': {'key': 'properties.sqlImageOffer', 'type': 'str'},
        'sql_image_sku': {'key': 'properties.sqlImageSku', 'type': 'str'},
        'scale_type': {'key': 'properties.scaleType', 'type': 'str'},
        'cluster_manager_type': {'key': 'properties.clusterManagerType', 'type': 'str'},
        'cluster_configuration': {'key': 'properties.clusterConfiguration', 'type': 'str'},
        'wsfc_domain_profile': {'key': 'properties.wsfcDomainProfile', 'type': 'WSFCDomainProfile'},
        'domainless_profile': {'key': 'properties.domainlessProfile', 'type': 'DomainlessProfile'},
    }

    def __init__(self, **kwargs):
        super(SqlVirtualMachineGroup, self).__init__(**kwargs)
        self.provisioning_state = None
        self.sql_image_offer = kwargs.get('sql_image_offer', None)
        self.sql_image_sku = kwargs.get('sql_image_sku', None)
        self.scale_type = None
        self.cluster_manager_type = None
        self.cluster_configuration = None
        self.wsfc_domain_profile = kwargs.get('wsfc_domain_profile', None)
        self.domainless_profile = kwargs.get('domainless_profile', None)
