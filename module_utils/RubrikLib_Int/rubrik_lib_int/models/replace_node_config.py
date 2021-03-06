# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReplaceNodeConfig(Model):
    """ReplaceNodeConfig.

    :param new_node_id:
    :type new_node_id: str
    :param old_node_id:
    :type old_node_id: str
    :param preserve_hdds:
    :type preserve_hdds: bool
    """

    _validation = {
        'new_node_id': {'required': True},
        'old_node_id': {'required': True},
        'preserve_hdds': {'required': True},
    }

    _attribute_map = {
        'new_node_id': {'key': 'newNodeId', 'type': 'str'},
        'old_node_id': {'key': 'oldNodeId', 'type': 'str'},
        'preserve_hdds': {'key': 'preserveHdds', 'type': 'bool'},
    }

    def __init__(self, new_node_id, old_node_id, preserve_hdds):
        self.new_node_id = new_node_id
        self.old_node_id = old_node_id
        self.preserve_hdds = preserve_hdds
