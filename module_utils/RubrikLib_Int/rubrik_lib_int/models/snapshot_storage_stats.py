# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SnapshotStorageStats(Model):
    """SnapshotStorageStats.

    :param logical_bytes: Amount of logical bytes the snapshot represents.
    :type logical_bytes: long
    :param ingested_bytes: Amount of bytes ingested to our system for the
     snapshot.
    :type ingested_bytes: long
    :param physical_bytes: Amount of bytes physically stored in our system for
     the snapshot.
    :type physical_bytes: long
    """

    _validation = {
        'logical_bytes': {'required': True},
        'ingested_bytes': {'required': True},
        'physical_bytes': {'required': True},
    }

    _attribute_map = {
        'logical_bytes': {'key': 'logicalBytes', 'type': 'long'},
        'ingested_bytes': {'key': 'ingestedBytes', 'type': 'long'},
        'physical_bytes': {'key': 'physicalBytes', 'type': 'long'},
    }

    def __init__(self, logical_bytes, ingested_bytes, physical_bytes):
        self.logical_bytes = logical_bytes
        self.ingested_bytes = ingested_bytes
        self.physical_bytes = physical_bytes
