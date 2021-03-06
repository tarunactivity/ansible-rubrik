# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BootstappedResult(Model):
    """BootstappedResult.

    :param is_bootstrapped:
    :type is_bootstrapped: bool
    """

    _validation = {
        'is_bootstrapped': {'required': True},
    }

    _attribute_map = {
        'is_bootstrapped': {'key': 'isBootstrapped', 'type': 'bool'},
    }

    def __init__(self, is_bootstrapped):
        self.is_bootstrapped = is_bootstrapped
