# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataStoreDetail(Model):
    """DataStoreDetail.

    :param id:
    :type id: str
    :param moid:
    :type moid: str
    :param name:
    :type name: str
    :param data_store_type:
    :type data_store_type: str
    :param capacity:
    :type capacity: long
    :param path:
    :type path: str
    :param data_center:
    :type data_center: :class:`DataCenterSummary
     <rubriklib_int.models.DataCenterSummary>`
    :param virtual_disks:
    :type virtual_disks: list of :class:`VirtualDiskSummary
     <rubriklib_int.models.VirtualDiskSummary>`
    :param is_local:
    :type is_local: bool
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'moid': {'key': 'moid', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'data_store_type': {'key': 'dataStoreType', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'long'},
        'path': {'key': 'path', 'type': 'str'},
        'data_center': {'key': 'dataCenter', 'type': 'DataCenterSummary'},
        'virtual_disks': {'key': 'virtualDisks', 'type': '[VirtualDiskSummary]'},
        'is_local': {'key': 'isLocal', 'type': 'bool'},
    }

    def __init__(self, id, moid=None, name=None, data_store_type=None, capacity=None, path=None, data_center=None, virtual_disks=None, is_local=None):
        self.id = id
        self.moid = moid
        self.name = name
        self.data_store_type = data_store_type
        self.capacity = capacity
        self.path = path
        self.data_center = data_center
        self.virtual_disks = virtual_disks
        self.is_local = is_local
