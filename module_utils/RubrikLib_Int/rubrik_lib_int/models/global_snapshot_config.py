# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GlobalSnapshotConfig(Model):
    """GlobalSnapshotConfig.

    :param similarity_threshold: Similarity threshold to pick a sim disk
    :type similarity_threshold: float
    """

    _attribute_map = {
        'similarity_threshold': {'key': 'similarity_threshold', 'type': 'float'},
    }

    def __init__(self, similarity_threshold=None):
        self.similarity_threshold = similarity_threshold
