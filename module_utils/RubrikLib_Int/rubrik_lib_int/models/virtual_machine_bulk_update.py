# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineBulkUpdate(Model):
    """VirtualMachineBulkUpdate.

    :param vm_ids:
    :type vm_ids: list of str
    :param update_property:
    :type update_property: :class:`VirtualMachineUpdateWithSecret
     <rubriklib_int.models.VirtualMachineUpdateWithSecret>`
    """

    _validation = {
        'vm_ids': {'required': True},
        'update_property': {'required': True},
    }

    _attribute_map = {
        'vm_ids': {'key': 'vmIds', 'type': '[str]'},
        'update_property': {'key': 'updateProperty', 'type': 'VirtualMachineUpdateWithSecret'},
    }

    def __init__(self, vm_ids, update_property):
        self.vm_ids = vm_ids
        self.update_property = update_property
