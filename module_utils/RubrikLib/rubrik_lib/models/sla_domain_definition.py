# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SlaDomainDefinition(Model):
    """SlaDomainDefinition.

    :param name:
    :type name: str
    :param frequencies:
    :type frequencies: list of :class:`SlaFrequency
     <rubriklib.models.SlaFrequency>`
    :param allowed_backup_windows:
    :type allowed_backup_windows: list of :class:`BackupWindow
     <rubriklib.models.BackupWindow>`
    :param first_full_allowed_backup_windows:
    :type first_full_allowed_backup_windows: list of :class:`BackupWindow
     <rubriklib.models.BackupWindow>`
    :param local_retention_limit:
    :type local_retention_limit: long
    :param archival_specs:
    :type archival_specs: list of :class:`ArchivalSpec
     <rubriklib.models.ArchivalSpec>`
    :param replication_specs:
    :type replication_specs: list of :class:`ReplicationSpec
     <rubriklib.models.ReplicationSpec>`
    """

    _validation = {
        'name': {'required': True},
        'frequencies': {'required': True},
        'first_full_allowed_backup_windows': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'frequencies': {'key': 'frequencies', 'type': '[SlaFrequency]'},
        'allowed_backup_windows': {'key': 'allowedBackupWindows', 'type': '[BackupWindow]'},
        'first_full_allowed_backup_windows': {'key': 'firstFullAllowedBackupWindows', 'type': '[BackupWindow]'},
        'local_retention_limit': {'key': 'localRetentionLimit', 'type': 'long'},
        'archival_specs': {'key': 'archivalSpecs', 'type': '[ArchivalSpec]'},
        'replication_specs': {'key': 'replicationSpecs', 'type': '[ReplicationSpec]'},
    }

    def __init__(self, name, frequencies, first_full_allowed_backup_windows, allowed_backup_windows=None, local_retention_limit=None, archival_specs=None, replication_specs=None):
        self.name = name
        self.frequencies = frequencies
        self.allowed_backup_windows = allowed_backup_windows
        self.first_full_allowed_backup_windows = first_full_allowed_backup_windows
        self.local_retention_limit = local_retention_limit
        self.archival_specs = archival_specs
        self.replication_specs = replication_specs
