# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class HypervInstantRecoveryJobConfig(Model):
    """HypervInstantRecoveryJobConfig.

    :param vm_name: name of the new VM to instantly recover
    :type vm_name: str
    :param host_id: ID of the host to instantly recover to
    :type host_id: str
    """

    _attribute_map = {
        'vm_name': {'key': 'vmName', 'type': 'str'},
        'host_id': {'key': 'hostId', 'type': 'str'},
    }

    def __init__(self, vm_name=None, host_id=None):
        self.vm_name = vm_name
        self.host_id = host_id
