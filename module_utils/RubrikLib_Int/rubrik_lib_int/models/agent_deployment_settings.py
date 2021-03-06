# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AgentDeploymentSettings(Model):
    """AgentDeploymentSettings.

    :param is_automatic: Determines whether the Rubrik cluster automatically
     deploys the Rubrik Backup Service to the guest OS at the first backup. Set
     to true to permit automatic deployment. Set to false to prevent automatic
     deployment.
    :type is_automatic: bool
    """

    _validation = {
        'is_automatic': {'required': True},
    }

    _attribute_map = {
        'is_automatic': {'key': 'isAutomatic', 'type': 'bool'},
    }

    def __init__(self, is_automatic):
        self.is_automatic = is_automatic
