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


class SQLWorkloadTypeUpdateSettings(Model):
    """SQL workload type update settings.

    :param sql_workload_type: SQL Server workload type. Possible values
     include: 'GENERAL', 'OLTP', 'DW'
    :type sql_workload_type: str or
     ~azure.mgmt.sqlvirtualmachine.models.SqlWorkloadType
    """

    _attribute_map = {
        'sql_workload_type': {'key': 'sqlWorkloadType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SQLWorkloadTypeUpdateSettings, self).__init__(**kwargs)
        self.sql_workload_type = kwargs.get('sql_workload_type', None)
