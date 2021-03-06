# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommandResult(Model):
    """CommandResult.

    :param success:
    :type success: bool
    """

    _validation = {
        'success': {'required': True},
    }

    _attribute_map = {
        'success': {'key': 'success', 'type': 'bool'},
    }

    def __init__(self, success):
        self.success = success
