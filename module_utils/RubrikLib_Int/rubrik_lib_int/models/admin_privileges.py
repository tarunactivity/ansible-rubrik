# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdminPrivileges(Model):
    """AdminPrivileges.

    :param full_admin:
    :type full_admin: list of str
    """

    _attribute_map = {
        'full_admin': {'key': 'fullAdmin', 'type': '[str]'},
    }

    def __init__(self, full_admin=None):
        self.full_admin = full_admin
