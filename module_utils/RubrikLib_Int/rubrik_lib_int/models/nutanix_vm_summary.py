# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .snappable import Snappable


class NutanixVmSummary(Snappable):
    """NutanixVmSummary.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param configured_sla_domain_id: ID of the configured SLA domain
    :type configured_sla_domain_id: str
    :param configured_sla_domain_name: name of the configured SLA domain
    :type configured_sla_domain_name: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    :param sla_assignment: SLA assignment type. Possible values include:
     'Derived', 'Direct', 'Unassigned'
    :type sla_assignment: str or :class:`enum <rubriklib_int.models.enum>`
    :param effective_sla_domain_id: ID of the effective SLA domain
    :type effective_sla_domain_id: str
    :param effective_sla_domain_name: name of the effective SLA domain
    :type effective_sla_domain_name: str
    :param effective_sla_source_object_id: ID of the object from which the
     effective SLA domain is inherited
    :type effective_sla_source_object_id: str
    :param effective_sla_source_object_name: Name of the object from which the
     effective SLA domain is inherited
    :type effective_sla_source_object_name: str
    :param nutanix_cluster_id: The ID of the Nutanix cluster to which this VM
     belongs
    :type nutanix_cluster_id: str
    :param nutanix_cluster_name: The name of the Nutanix cluster to which this
     VM belongs
    :type nutanix_cluster_name: str
    :param is_relic: Whether this Nutanix VM is currently present on the
     Nutanix cluster
    :type is_relic: bool
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'configured_sla_domain_id': {'required': True},
        'configured_sla_domain_name': {'required': True},
        'primary_cluster_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'configured_sla_domain_id': {'key': 'configuredSlaDomainId', 'type': 'str'},
        'configured_sla_domain_name': {'key': 'configuredSlaDomainName', 'type': 'str'},
        'primary_cluster_id': {'key': 'primaryClusterId', 'type': 'str'},
        'sla_assignment': {'key': 'slaAssignment', 'type': 'str'},
        'effective_sla_domain_id': {'key': 'effectiveSlaDomainId', 'type': 'str'},
        'effective_sla_domain_name': {'key': 'effectiveSlaDomainName', 'type': 'str'},
        'effective_sla_source_object_id': {'key': 'effectiveSlaSourceObjectId', 'type': 'str'},
        'effective_sla_source_object_name': {'key': 'effectiveSlaSourceObjectName', 'type': 'str'},
        'nutanix_cluster_id': {'key': 'nutanixClusterId', 'type': 'str'},
        'nutanix_cluster_name': {'key': 'nutanixClusterName', 'type': 'str'},
        'is_relic': {'key': 'isRelic', 'type': 'bool'},
    }

    def __init__(self, id, name, configured_sla_domain_id, configured_sla_domain_name, primary_cluster_id, sla_assignment=None, effective_sla_domain_id=None, effective_sla_domain_name=None, effective_sla_source_object_id=None, effective_sla_source_object_name=None, nutanix_cluster_id=None, nutanix_cluster_name=None, is_relic=None):
        super(NutanixVmSummary, self).__init__(id=id, name=name, configured_sla_domain_id=configured_sla_domain_id, configured_sla_domain_name=configured_sla_domain_name, primary_cluster_id=primary_cluster_id, sla_assignment=sla_assignment, effective_sla_domain_id=effective_sla_domain_id, effective_sla_domain_name=effective_sla_domain_name, effective_sla_source_object_id=effective_sla_source_object_id, effective_sla_source_object_name=effective_sla_source_object_name)
        self.nutanix_cluster_id = nutanix_cluster_id
        self.nutanix_cluster_name = nutanix_cluster_name
        self.is_relic = is_relic
