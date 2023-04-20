# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestFailedException(Model):
    """RequestFailedException.

    :param error_type:
    :type error_type: str
    :param message:
    :type message: str
    :param code:
    :type code: str
    :param param:
    :type param: str
    """

    _validation = {
        'error_type': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'error_type': {'key': 'errorType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'param': {'key': 'param', 'type': 'str'},
    }

    def __init__(self, error_type, message, code=None, param=None):
        self.error_type = error_type
        self.message = message
        self.code = code
        self.param = param
