# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .managed_volume_export import ManagedVolumeExport


class ManagedVolumeSnapshotExportSummary(ManagedVolumeExport):
    """ManagedVolumeSnapshotExportSummary.

    :param is_active: Is export active.
    :type is_active: bool
    :param channels: Channels of this export.
    :type channels: list of :class:`ManagedVolumeChannelConfig
     <rubriklib_int.models.ManagedVolumeChannelConfig>`
    :param config:
    :type config: :class:`ManagedVolumeExportConfig
     <rubriklib_int.models.ManagedVolumeExportConfig>`
    :param id: ID of managed volume snapshot export
    :type id: str
    :param snapshot_id: Snapshot this export is based off.
    :type snapshot_id: str
    :param snapshot_date: Date of the snapshot this export is based off.
    :type snapshot_date: datetime
    :param source_managed_volume_id: ID of the managed volume this export
     belongs to.
    :type source_managed_volume_id: str
    :param source_managed_volume_name: Name of the managed volume this export
     belongs to.
    :type source_managed_volume_name: str
    :param exported_date: Exported date of the managed volume snapshot.
    :type exported_date: datetime
    """

    _validation = {
        'is_active': {'required': True},
        'channels': {'required': True},
        'config': {'required': True},
    }

    _attribute_map = {
        'is_active': {'key': 'isActive', 'type': 'bool'},
        'channels': {'key': 'channels', 'type': '[ManagedVolumeChannelConfig]'},
        'config': {'key': 'config', 'type': 'ManagedVolumeExportConfig'},
        'id': {'key': 'id', 'type': 'str'},
        'snapshot_id': {'key': 'snapshotId', 'type': 'str'},
        'snapshot_date': {'key': 'snapshotDate', 'type': 'iso-8601'},
        'source_managed_volume_id': {'key': 'sourceManagedVolumeId', 'type': 'str'},
        'source_managed_volume_name': {'key': 'sourceManagedVolumeName', 'type': 'str'},
        'exported_date': {'key': 'exportedDate', 'type': 'iso-8601'},
    }

    def __init__(self, is_active, channels, config, id=None, snapshot_id=None, snapshot_date=None, source_managed_volume_id=None, source_managed_volume_name=None, exported_date=None):
        super(ManagedVolumeSnapshotExportSummary, self).__init__(is_active=is_active, channels=channels, config=config)
        self.id = id
        self.snapshot_id = snapshot_id
        self.snapshot_date = snapshot_date
        self.source_managed_volume_id = source_managed_volume_id
        self.source_managed_volume_name = source_managed_volume_name
        self.exported_date = exported_date
