# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RestorePathPair(Model):
    """RestorePathPair.

    :param path: Original file path to be restored
    :type path: str
    :param restore_path: Directory of the folder to copy files into. If this
     is empty, file will be restored back into original directory.
    :type restore_path: str
    """

    _validation = {
        'path': {'required': True},
    }

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'restore_path': {'key': 'restorePath', 'type': 'str'},
    }

    def __init__(self, path, restore_path=None):
        self.path = path
        self.restore_path = restore_path