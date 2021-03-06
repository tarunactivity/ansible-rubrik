# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SendEmailParams(Model):
    """SendEmailParams.

    :param ids:
    :type ids: list of str
    """

    _validation = {
        'ids': {'required': True},
    }

    _attribute_map = {
        'ids': {'key': 'ids', 'type': '[str]'},
    }

    def __init__(self, ids):
        self.ids = ids
