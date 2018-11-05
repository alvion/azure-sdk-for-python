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


class AutoBackupSettings(Model):
    """Auto backup settings.

    :param enable: Enable or disable autobackup on SQL virtual machine.
    :type enable: bool
    :param enable_encryption: Enable or disable encryption for backup on SQL
     virtual machine.
    :type enable_encryption: bool
    :param retention_period: Retention period of backup.
    :type retention_period: int
    :param storage_account_url: Storage account url where backup will be taken
     to.
    :type storage_account_url: str
    :param storage_access_key: Storage account key where backup will be taken
     to.
    :type storage_access_key: str
    :param password: Password for encryption on backup.
    :type password: str
    :param backup_system_dbs: Include or exclude system databases from auto
     backup.
    :type backup_system_dbs: bool
    :param backup_schedule_type: Backup schedule type. Possible values
     include: 'Manual', 'Automated'
    :type backup_schedule_type: str or
     ~azure.mgmt.sqlvirtualmachine.models.BackupScheduleType
    :param full_backup_frequency: Full backup frequency. Possible values
     include: 'Daily', 'Weekly'
    :type full_backup_frequency: str or
     ~azure.mgmt.sqlvirtualmachine.models.FullBackupFrequencyType
    :param full_backup_start_time: Full backup startup time.
    :type full_backup_start_time: int
    :param full_backup_window_hours: Full backup window hours.
    :type full_backup_window_hours: int
    :param log_backup_frequency: Log backup frequency.
    :type log_backup_frequency: int
    """

    _attribute_map = {
        'enable': {'key': 'enable', 'type': 'bool'},
        'enable_encryption': {'key': 'enableEncryption', 'type': 'bool'},
        'retention_period': {'key': 'retentionPeriod', 'type': 'int'},
        'storage_account_url': {'key': 'storageAccountUrl', 'type': 'str'},
        'storage_access_key': {'key': 'storageAccessKey', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'backup_system_dbs': {'key': 'backupSystemDbs', 'type': 'bool'},
        'backup_schedule_type': {'key': 'backupScheduleType', 'type': 'str'},
        'full_backup_frequency': {'key': 'fullBackupFrequency', 'type': 'str'},
        'full_backup_start_time': {'key': 'fullBackupStartTime', 'type': 'int'},
        'full_backup_window_hours': {'key': 'fullBackupWindowHours', 'type': 'int'},
        'log_backup_frequency': {'key': 'logBackupFrequency', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AutoBackupSettings, self).__init__(**kwargs)
        self.enable = kwargs.get('enable', None)
        self.enable_encryption = kwargs.get('enable_encryption', None)
        self.retention_period = kwargs.get('retention_period', None)
        self.storage_account_url = kwargs.get('storage_account_url', None)
        self.storage_access_key = kwargs.get('storage_access_key', None)
        self.password = kwargs.get('password', None)
        self.backup_system_dbs = kwargs.get('backup_system_dbs', None)
        self.backup_schedule_type = kwargs.get('backup_schedule_type', None)
        self.full_backup_frequency = kwargs.get('full_backup_frequency', None)
        self.full_backup_start_time = kwargs.get('full_backup_start_time', None)
        self.full_backup_window_hours = kwargs.get('full_backup_window_hours', None)
        self.log_backup_frequency = kwargs.get('log_backup_frequency', None)
