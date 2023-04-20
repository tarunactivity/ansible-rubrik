# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OrganizationPrincipalDef(Model):
    """OrganizationPrincipalDef.

    :param id: The id of the Principal
    :type id: str
    :param access_level: The level of access this principal has on the
     Organization. NOTE 1) An empty array specifies no access 2) The ManageSla
     and ManageUser access levels require OrgAdmin access
    :type access_level: list of str
    """

    _validation = {
        'id': {'required': True},
        'access_level': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'access_level': {'key': 'accessLevel', 'type': '[str]'},
    }

    def __init__(self, id, access_level):
        self.id = id
        self.access_level = access_level
