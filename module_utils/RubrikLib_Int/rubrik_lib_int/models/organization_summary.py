# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OrganizationSummary(Model):
    """OrganizationSummary.

    :param id: The unique id of the Organization
    :type id: str
    :param name: The name of the Organization
    :type name: str
    :param resource_count:
    :type resource_count: int
    :param user_count:
    :type user_count: int
    :param organization_admins: All of the Org Admins for this Organization
    :type organization_admins: list of :class:`OrganizationPrincipalSummary
     <rubriklib_int.models.OrganizationPrincipalSummary>`
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
        'resource_count': {'required': True},
        'user_count': {'required': True},
        'organization_admins': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'resource_count': {'key': 'resourceCount', 'type': 'int'},
        'user_count': {'key': 'userCount', 'type': 'int'},
        'organization_admins': {'key': 'organizationAdmins', 'type': '[OrganizationPrincipalSummary]'},
    }

    def __init__(self, id, name, resource_count, user_count, organization_admins):
        self.id = id
        self.name = name
        self.resource_count = resource_count
        self.user_count = user_count
        self.organization_admins = organization_admins
