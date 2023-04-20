# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PrincipalSort(Model):
    """PrincipalSort.

    :param attr: Attribute by which to sort:
     name|principalType|firstName|lastName|emailAddress|description (default is
     "name")
    :type attr: str
    :param order: Sort order: asc|desc (default is "asc")
    :type order: str
    """

    _validation = {
        'attr': {'required': True},
    }

    _attribute_map = {
        'attr': {'key': 'attr', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
    }

    def __init__(self, attr, order=None):
        self.attr = attr
        self.order = order
