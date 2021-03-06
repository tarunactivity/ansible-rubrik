# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MssqlDbSlaConflictInfo(Model):
    """MssqlDbSlaConflictInfo.

    :param groups:
    :type groups: list of :class:`MssqlDbSlaConflictGroup
     <rubriklib_int.models.MssqlDbSlaConflictGroup>`
    """

    _validation = {
        'groups': {'required': True},
    }

    _attribute_map = {
        'groups': {'key': 'groups', 'type': '[MssqlDbSlaConflictGroup]'},
    }

    def __init__(self, groups):
        self.groups = groups
