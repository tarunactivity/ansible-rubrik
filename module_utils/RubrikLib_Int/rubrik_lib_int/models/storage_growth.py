# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StorageGrowth(Model):
    """StorageGrowth.

    :param bytes:
    :type bytes: long
    """

    _validation = {
        'bytes': {'required': True},
    }

    _attribute_map = {
        'bytes': {'key': 'bytes', 'type': 'long'},
    }

    def __init__(self, bytes):
        self.bytes = bytes
