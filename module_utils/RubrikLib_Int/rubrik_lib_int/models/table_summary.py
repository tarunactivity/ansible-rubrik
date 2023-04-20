# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TableSummary(Model):
    """TableSummary.

    :param columns: Columns for the table.
    :type columns: list of str
    """

    _validation = {
        'columns': {'required': True},
    }

    _attribute_map = {
        'columns': {'key': 'columns', 'type': '[str]'},
    }

    def __init__(self, columns):
        self.columns = columns
