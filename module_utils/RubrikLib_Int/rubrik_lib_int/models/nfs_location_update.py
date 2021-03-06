# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NfsLocationUpdate(Model):
    """NfsLocationUpdate.

    :param host:
    :type host: str
    :param export_dir:
    :type export_dir: str
    :param nfs_version:
    :type nfs_version: int
    :param auth_type:
    :type auth_type: str
    :param file_lock_period_in_seconds:
    :type file_lock_period_in_seconds: long
    :param name:
    :type name: str
    """

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'export_dir': {'key': 'exportDir', 'type': 'str'},
        'nfs_version': {'key': 'nfsVersion', 'type': 'int'},
        'auth_type': {'key': 'authType', 'type': 'str'},
        'file_lock_period_in_seconds': {'key': 'fileLockPeriodInSeconds', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, host=None, export_dir=None, nfs_version=None, auth_type=None, file_lock_period_in_seconds=None, name=None):
        self.host = host
        self.export_dir = export_dir
        self.nfs_version = nfs_version
        self.auth_type = auth_type
        self.file_lock_period_in_seconds = file_lock_period_in_seconds
        self.name = name
