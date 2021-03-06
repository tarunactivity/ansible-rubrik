# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EffectiveAuthorizationsQuery(Model):
    """EffectiveAuthorizationsQuery.

    :param principal:
    :type principal: str
    :param resources:
    :type resources: list of str
    """

    _validation = {
        'resources': {'required': True},
    }

    _attribute_map = {
        'principal': {'key': 'principal', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[str]'},
    }

    def __init__(self, resources, principal=None):
        self.principal = principal
        self.resources = resources
