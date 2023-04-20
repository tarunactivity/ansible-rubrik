# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InternalSnapshotGarbageCollectStatusConfig(Model):
    """InternalSnapshotGarbageCollectStatusConfig.

    :param snappable_id:
    :type snappable_id: str
    :param snapshot_ids: Snapshots IDs to check for garbage collection
    :type snapshot_ids: list of str
    """

    _validation = {
        'snappable_id': {'required': True},
        'snapshot_ids': {'required': True},
    }

    _attribute_map = {
        'snappable_id': {'key': 'snappableId', 'type': 'str'},
        'snapshot_ids': {'key': 'snapshotIds', 'type': '[str]'},
    }

    def __init__(self, snappable_id, snapshot_ids):
        self.snappable_id = snappable_id
        self.snapshot_ids = snapshot_ids
