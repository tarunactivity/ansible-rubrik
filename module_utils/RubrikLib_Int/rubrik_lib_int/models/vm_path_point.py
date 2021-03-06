# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VmPathPoint(Model):
    """VmPathPoint.

    :param id: ID of the object
    :type id: str
    :param managed_id: (Deprecated) - See **id**
    :type managed_id: str
    :param name: Name of the object
    :type name: str
    """

    _validation = {
        'id': {'required': True},
        'managed_id': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'managed_id': {'key': 'managedId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, id, managed_id, name):
        self.id = id
        self.managed_id = managed_id
        self.name = name
