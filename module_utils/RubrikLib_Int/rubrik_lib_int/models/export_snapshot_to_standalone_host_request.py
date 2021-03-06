# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .mount_export_snapshot_job_common_options import MountExportSnapshotJobCommonOptions


class ExportSnapshotToStandaloneHostRequest(MountExportSnapshotJobCommonOptions):
    """ExportSnapshotToStandaloneHostRequest.

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
    :param host_ip_address: The IP address of the standalone ESXi host
    :type host_ip_address: str
    :param datastore_name: Name of the datastore to assign to the exported
     virtual machine.
    :type datastore_name: str
    :param host_username: The admin username of standalone ESXi host
    :type host_username: str
    :param host_password: The admin password of standalone ESXi host
    :type host_password: str
    """

    _attribute_map = {
        'vm_name': {'key': 'vmName', 'type': 'str'},
        'disable_network': {'key': 'disableNetwork', 'type': 'bool'},
        'remove_network_devices': {'key': 'removeNetworkDevices', 'type': 'bool'},
        'power_on': {'key': 'powerOn', 'type': 'bool'},
        'keep_mac_addresses': {'key': 'keepMacAddresses', 'type': 'bool'},
        'host_ip_address': {'key': 'hostIpAddress', 'type': 'str'},
        'datastore_name': {'key': 'datastoreName', 'type': 'str'},
        'host_username': {'key': 'hostUsername', 'type': 'str'},
        'host_password': {'key': 'hostPassword', 'type': 'str'},
    }

    def __init__(self, vm_name=None, disable_network=None, remove_network_devices=None, power_on=None, keep_mac_addresses=None, host_ip_address=None, datastore_name=None, host_username=None, host_password=None):
        super(ExportSnapshotToStandaloneHostRequest, self).__init__(vm_name=vm_name, disable_network=disable_network, remove_network_devices=remove_network_devices, power_on=power_on, keep_mac_addresses=keep_mac_addresses)
        self.host_ip_address = host_ip_address
        self.datastore_name = datastore_name
        self.host_username = host_username
        self.host_password = host_password
