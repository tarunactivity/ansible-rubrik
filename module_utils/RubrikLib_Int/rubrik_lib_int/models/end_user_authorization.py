# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EndUserAuthorization(Model):
    """EndUserAuthorization.

    :param principal:
    :type principal: str
    :param privileges:
    :type privileges: :class:`EndUserPrivileges
     <rubriklib_int.models.EndUserPrivileges>`
    """

    _validation = {
        'principal': {'required': True},
        'privileges': {'required': True},
    }

    _attribute_map = {
        'principal': {'key': 'principal', 'type': 'str'},
        'privileges': {'key': 'privileges', 'type': 'EndUserPrivileges'},
    }

    def __init__(self, principal, privileges):
        self.principal = principal
        self.privileges = privileges
