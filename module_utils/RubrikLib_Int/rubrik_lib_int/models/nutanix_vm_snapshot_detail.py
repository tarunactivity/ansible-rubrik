# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .nutanix_vm_snapshot_summary import NutanixVmSnapshotSummary


class NutanixVmSnapshotDetail(NutanixVmSnapshotSummary):
    """NutanixVmSnapshotDetail.

    :param id:
    :type id: str
    :param date_property:
    :type date_property: datetime
    :param expiration_date:
    :type expiration_date: datetime
    :param source_object_type:
    :type source_object_type: str
    :param is_on_demand_snapshot:
    :type is_on_demand_snapshot: bool
    :param cloud_state:
    :type cloud_state: long
    :param consistency_level:
    :type consistency_level: str
    :param index_state:
    :type index_state: long
    :param replication_location_ids:
    :type replication_location_ids: list of str
    :param archival_location_ids:
    :type archival_location_ids: list of str
    :param sla_id:
    :type sla_id: str
    :param sla_name:
    :type sla_name: str
    :param vm_name:
    :type vm_name: str
    """

    _validation = {
        'id': {'required': True},
        'date_property': {'required': True},
        'is_on_demand_snapshot': {'required': True},
        'replication_location_ids': {'required': True},
        'sla_id': {'required': True},
        'sla_name': {'required': True},
    }

    def __init__(self, id, date_property, is_on_demand_snapshot, replication_location_ids, sla_id, sla_name, expiration_date=None, source_object_type=None, cloud_state=None, consistency_level=None, index_state=None, archival_location_ids=None, vm_name=None):
        super(NutanixVmSnapshotDetail, self).__init__(id=id, date_property=date_property, expiration_date=expiration_date, source_object_type=source_object_type, is_on_demand_snapshot=is_on_demand_snapshot, cloud_state=cloud_state, consistency_level=consistency_level, index_state=index_state, replication_location_ids=replication_location_ids, archival_location_ids=archival_location_ids, sla_id=sla_id, sla_name=sla_name, vm_name=vm_name)
