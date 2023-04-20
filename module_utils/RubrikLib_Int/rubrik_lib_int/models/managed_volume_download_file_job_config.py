# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedVolumeDownloadFileJobConfig(Model):
    """ManagedVolumeDownloadFileJobConfig.

    :param path: Absolute file path
    :type path: str
    """

    _validation = {
        'path': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, path):
        self.path = path
