# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DiskStatus(Model):
    """DiskStatus.

    :param id:
    :type id: str
    :param status:
    :type status: str
    :param is_encrypted:
    :type is_encrypted: bool
    :param disk_type:
    :type disk_type: str
    :param node_id:
    :type node_id: str
    """

    _validation = {
        'id': {'required': True},
        'status': {'required': True},
        'is_encrypted': {'required': True},
        'disk_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'is_encrypted': {'key': 'isEncrypted', 'type': 'bool'},
        'disk_type': {'key': 'diskType', 'type': 'str'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
    }

    def __init__(self, id, status, is_encrypted, disk_type, node_id=None):
        self.id = id
        self.status = status
        self.is_encrypted = is_encrypted
        self.disk_type = disk_type
        self.node_id = node_id