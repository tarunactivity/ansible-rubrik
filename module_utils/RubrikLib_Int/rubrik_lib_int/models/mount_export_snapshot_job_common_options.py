# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MountExportSnapshotJobCommonOptions(Model):
    """MountExportSnapshotJobCommonOptions.

    :param vm_name: Name of the new VM created by mount or export
    :type vm_name: str
    :param disable_network: Sets the state of the network interfaces when the
     virtual machine is mounted or exported. Use 'false' to enable the network
     interfaces. Use 'true' to disable the network interfaces. Disabling the
     interfaces can prevent IP conflicts.
    :type disable_network: bool
    :param remove_network_devices: Determines whether to remove the network
     interfaces from the mounted or exported virtual machine. Set to 'true' to
     remove all network interfaces. The default value is 'false'.
    :type remove_network_devices: bool
    :param power_on: Determines whether the virtual machine should be powered
     on after mount or export. Set to 'true' to power on the virtual machine.
     Set to 'false' to mount or export the virtual machine but not power it on.
     The default is 'true'.
    :type power_on: bool
    :param keep_mac_addresses: Determines whether the MAC addresses of the
     network interfaces on the source virtual machine are assigned to the new
     virtual machine. Set to 'true' to assign the original MAC addresses to the
     new virtual machine. Set to 'false' to assign new MAC addresses. The
     default is 'false'. When removeNetworkDevices is set to true, this
     property is ignored.
    :type keep_mac_addresses: bool
    """

    _attribute_map = {
        'vm_name': {'key': 'vmName', 'type': 'str'},
        'disable_network': {'key': 'disableNetwork', 'type': 'bool'},
        'remove_network_devices': {'key': 'removeNetworkDevices', 'type': 'bool'},
        'power_on': {'key': 'powerOn', 'type': 'bool'},
        'keep_mac_addresses': {'key': 'keepMacAddresses', 'type': 'bool'},
    }

    def __init__(self, vm_name=None, disable_network=None, remove_network_devices=None, power_on=None, keep_mac_addresses=None):
        self.vm_name = vm_name
        self.disable_network = disable_network
        self.remove_network_devices = remove_network_devices
        self.power_on = power_on
        self.keep_mac_addresses = keep_mac_addresses