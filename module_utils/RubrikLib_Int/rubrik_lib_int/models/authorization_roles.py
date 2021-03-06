# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuthorizationRoles(Model):
    """AuthorizationRoles.

    :param principal:
    :type principal: str
    :param admin:
    :type admin: :class:`AdminRole <rubriklib_int.models.AdminRole>`
    :param end_user:
    :type end_user: :class:`EndUserRole <rubriklib_int.models.EndUserRole>`
    """

    _validation = {
        'principal': {'required': True},
        'admin': {'required': True},
        'end_user': {'required': True},
    }

    _attribute_map = {
        'principal': {'key': 'principal', 'type': 'str'},
        'admin': {'key': 'admin', 'type': 'AdminRole'},
        'end_user': {'key': 'endUser', 'type': 'EndUserRole'},
    }

    def __init__(self, principal, admin, end_user):
        self.principal = principal
        self.admin = admin
        self.end_user = end_user
