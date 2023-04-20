# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeNetworkInterface(Model):
    """NodeNetworkInterface.

    :param netmask: Node this interface is configured on
    :type netmask: str
    :param ip: IP of the node
    :type ip: str
    :param vlan: VLAN tag of the interface
    :type vlan: int
    """

    _validation = {
        'netmask': {'required': True},
        'ip': {'required': True},
        'vlan': {'required': True},
    }

    _attribute_map = {
        'netmask': {'key': 'netmask', 'type': 'str'},
        'ip': {'key': 'ip', 'type': 'str'},
        'vlan': {'key': 'vlan', 'type': 'int'},
    }

    def __init__(self, netmask, ip, vlan):
        self.netmask = netmask
        self.ip = ip
        self.vlan = vlan
