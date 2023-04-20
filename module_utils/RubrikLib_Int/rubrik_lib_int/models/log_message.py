# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LogMessage(Model):
    """LogMessage.

    :param log_level: One of FATAL, ERROR, WARNING, INFO, TRACE
    :type log_level: str
    :param component: Component generating the log
    :type component: str
    :param message: Message to be logged
    :type message: str
    """

    _validation = {
        'log_level': {'required': True},
        'component': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'log_level': {'key': 'logLevel', 'type': 'str'},
        'component': {'key': 'component', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, log_level, component, message):
        self.log_level = log_level
        self.component = component
        self.message = message