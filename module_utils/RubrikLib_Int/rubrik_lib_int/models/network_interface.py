# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .node_ip import NodeIp


class NetworkInterface(NodeIp):
    """NetworkInterface.

    :param node: Node this interface is configured on
    :type node: str
    :param ip: IP of the node
    :type ip: str
    :param netmask: Netmask of the IP.
    :type netmask: str
    :param vlan: VLAN this interface is on
    :type vlan: int
    """

    _validation = {
        'node': {'required': True},
        'ip': {'required': True},
    }

    _attribute_map = {
        'node': {'key': 'node', 'type': 'str'},
        'ip': {'key': 'ip', 'type': 'str'},
        'netmask': {'key': 'netmask', 'type': 'str'},
        'vlan': {'key': 'vlan', 'type': 'int'},
    }

    def __init__(self, node, ip, netmask=None, vlan=None):
        super(NetworkInterface, self).__init__(node=node, ip=ip)
        self.netmask = netmask
        self.vlan = vlan
