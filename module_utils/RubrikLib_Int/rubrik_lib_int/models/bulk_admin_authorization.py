# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkAdminAuthorization(Model):
    """BulkAdminAuthorization.

    :param principals:
    :type principals: list of str
    :param privileges:
    :type privileges: :class:`AdminPrivileges
     <rubriklib_int.models.AdminPrivileges>`
    """

    _validation = {
        'principals': {'required': True},
        'privileges': {'required': True},
    }

    _attribute_map = {
        'principals': {'key': 'principals', 'type': '[str]'},
        'privileges': {'key': 'privileges', 'type': 'AdminPrivileges'},
    }

    def __init__(self, principals, privileges):
        self.principals = principals
        self.privileges = privileges
