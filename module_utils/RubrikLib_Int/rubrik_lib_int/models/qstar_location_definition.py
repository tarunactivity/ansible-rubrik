# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class QstarLocationDefinition(Model):
    """QstarLocationDefinition.

    :param host: Hostname of the QStar server
    :type host: str
    :param integral_volume: QStar integral volume to mount
    :type integral_volume: str
    :param bucket: Bucket under the integral volume. The name cannot contain
     whitespace or _\\\\/*?%.:|<>
    :type bucket: str
    :param name: Name of this archival location
    :type name: str
    :param mount_protocol: Protocol to connect with the QStar server. Possible
     values include: 'NFS', 'CIFS'
    :type mount_protocol: str or :class:`enum <rubriklib_int.models.enum>`
    :param nfs_version: NFS protocol version to communicate with QStar server
     when using NFS mount protocol
    :type nfs_version: int
    :param other_nfs_options: Additional NFS options when using NFS protocol
    :type other_nfs_options: str
    :param other_cifs_options: Additional CIFS options when using CIFS
     protocol
    :type other_cifs_options: str
    """

    _validation = {
        'host': {'required': True},
        'integral_volume': {'required': True},
        'bucket': {'required': True},
        'name': {'required': True},
        'mount_protocol': {'required': True},
    }

    _attribute_map = {
        'host': {'key': 'host', 'type': 'str'},
        'integral_volume': {'key': 'integralVolume', 'type': 'str'},
        'bucket': {'key': 'bucket', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'mount_protocol': {'key': 'mountProtocol', 'type': 'str'},
        'nfs_version': {'key': 'nfsVersion', 'type': 'int'},
        'other_nfs_options': {'key': 'otherNfsOptions', 'type': 'str'},
        'other_cifs_options': {'key': 'otherCifsOptions', 'type': 'str'},
    }

    def __init__(self, host, integral_volume, bucket, name, mount_protocol, nfs_version=None, other_nfs_options=None, other_cifs_options=None):
        self.host = host
        self.integral_volume = integral_volume
        self.bucket = bucket
        self.name = name
        self.mount_protocol = mount_protocol
        self.nfs_version = nfs_version
        self.other_nfs_options = other_nfs_options
        self.other_cifs_options = other_cifs_options
