# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .host_summary import HostSummary


class HostDetail(HostSummary):
    """HostDetail.

    :param id:
    :type id: str
    :param hostname:
    :type hostname: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    :param operating_system:
    :type operating_system: str
    :param operating_system_type:
    :type operating_system_type: str
    :param status:
    :type status: str
    :param agent_id:
    :type agent_id: str
    :param compression_enabled:
    :type compression_enabled: bool
    """

    _validation = {
        'id': {'required': True},
        'hostname': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'hostname': {'key': 'hostname', 'type': 'str'},
        'primary_cluster_id': {'key': 'primaryClusterId', 'type': 'str'},
        'operating_system': {'key': 'operatingSystem', 'type': 'str'},
        'operating_system_type': {'key': 'operatingSystemType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'agent_id': {'key': 'agentId', 'type': 'str'},
        'compression_enabled': {'key': 'compressionEnabled', 'type': 'bool'},
    }

    def __init__(self, id, hostname, primary_cluster_id=None, operating_system=None, operating_system_type=None, status=None, agent_id=None, compression_enabled=None):
        super(HostDetail, self).__init__(id=id, hostname=hostname, primary_cluster_id=primary_cluster_id, operating_system=operating_system, operating_system_type=operating_system_type, status=status)
        self.agent_id = agent_id
        self.compression_enabled = compression_enabled
