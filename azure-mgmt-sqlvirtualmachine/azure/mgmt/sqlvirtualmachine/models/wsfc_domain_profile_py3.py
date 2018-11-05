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


class WSFCDomainProfile(Model):
    """The Active Directory domain profile.

    :param domain_fqdn: Fully qualified name of the domain.
    :type domain_fqdn: str
    :param ou_path: OU path in which the nodes and cluster will be present.
    :type ou_path: str
    :param cluster_bootstrap_account: Account name used for creating cluster
     (at minimum needs permissions to 'Create Computer Objects' in domain).
    :type cluster_bootstrap_account: str
    :param cluster_operator_account: Account name used for operating cluster
     i.e. will be part of administrators group on all the participating virtual
     machines in the cluster.
    :type cluster_operator_account: str
    :param sql_service_account: Account name under which SQL service will run
     on all participating SQL virtual machines in the cluster.
    :type sql_service_account: str
    :param file_share_witness_path: Optional path for fileshare witness.
    :type file_share_witness_path: str
    :param storage_account_url: Fully qualified ARM resource id of the witness
     storage account.
    :type storage_account_url: str
    :param storage_account_primary_key: Primary key of the witness storage
     account.
    :type storage_account_primary_key: str
    """

    _attribute_map = {
        'domain_fqdn': {'key': 'domainFqdn', 'type': 'str'},
        'ou_path': {'key': 'ouPath', 'type': 'str'},
        'cluster_bootstrap_account': {'key': 'clusterBootstrapAccount', 'type': 'str'},
        'cluster_operator_account': {'key': 'clusterOperatorAccount', 'type': 'str'},
        'sql_service_account': {'key': 'sqlServiceAccount', 'type': 'str'},
        'file_share_witness_path': {'key': 'fileShareWitnessPath', 'type': 'str'},
        'storage_account_url': {'key': 'storageAccountUrl', 'type': 'str'},
        'storage_account_primary_key': {'key': 'storageAccountPrimaryKey', 'type': 'str'},
    }

    def __init__(self, *, domain_fqdn: str=None, ou_path: str=None, cluster_bootstrap_account: str=None, cluster_operator_account: str=None, sql_service_account: str=None, file_share_witness_path: str=None, storage_account_url: str=None, storage_account_primary_key: str=None, **kwargs) -> None:
        super(WSFCDomainProfile, self).__init__(**kwargs)
        self.domain_fqdn = domain_fqdn
        self.ou_path = ou_path
        self.cluster_bootstrap_account = cluster_bootstrap_account
        self.cluster_operator_account = cluster_operator_account
        self.sql_service_account = sql_service_account
        self.file_share_witness_path = file_share_witness_path
        self.storage_account_url = storage_account_url
        self.storage_account_primary_key = storage_account_primary_key
