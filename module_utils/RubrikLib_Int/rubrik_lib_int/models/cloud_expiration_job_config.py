# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudExpirationJobConfig(Model):
    """CloudExpirationJobConfig.

    :param vm_id: ID of the VM for which we are expiring snapshots
    :type vm_id: str
    """

    _validation = {
        'vm_id': {'required': True},
    }

    _attribute_map = {
        'vm_id': {'key': 'vmId', 'type': 'str'},
    }

    def __init__(self, vm_id):
        self.vm_id = vm_id
