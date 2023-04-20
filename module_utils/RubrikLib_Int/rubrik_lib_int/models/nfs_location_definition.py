# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NfsLocationDefinition(Model):
    """NfsLocationDefinition.

    :param host:
    :type host: str
    :param export_dir:
    :type export_dir: str
    :param nfs_version:
    :type nfs_version: int
    :param auth_type:
    :type auth_type: str
    :param other_nfs_options:
    :type other_nfs_options: str
    :param file_lock_period_in_seconds:
    :type file_lock_period_in_seconds: long
    :param bucket: Bucket name cannot contain whitespace or _\\\\/*?%.:|<>
    :type bucket: str
    :param name:
    :type name: str
    """

    _validation = {
        'host': {'required': True},
        'export_dir': {'required': True},
        'file_lock_period_in_seconds': {'required': True},
        'bucket': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'export_dir': {'key': 'exportDir', 'type': 'str'},
        'nfs_version': {'key': 'nfsVersion', 'type': 'int'},
        'auth_type': {'key': 'authType', 'type': 'str'},
        'other_nfs_options': {'key': 'otherNfsOptions', 'type': 'str'},
        'file_lock_period_in_seconds': {'key': 'fileLockPeriodInSeconds', 'type': 'long'},
        'bucket': {'key': 'bucket', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, host, export_dir, file_lock_period_in_seconds, bucket, name, nfs_version=None, auth_type=None, other_nfs_options=None):
        self.host = host
        self.export_dir = export_dir
        self.nfs_version = nfs_version
        self.auth_type = auth_type
        self.other_nfs_options = other_nfs_options
        self.file_lock_period_in_seconds = file_lock_period_in_seconds
        self.bucket = bucket
        self.name = name
