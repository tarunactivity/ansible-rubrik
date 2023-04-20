# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EventStatusSummary(Model):
    """EventStatusSummary.

    :param id:
    :type id: str
    :param progress:
    :type progress: str
    :param is_cancelable:
    :type is_cancelable: bool
    :param is_cancel_requested:
    :type is_cancel_requested: bool
    :param attempt_number:
    :type attempt_number: int
    """

    _validation = {
        'id': {'required': True},
        'progress': {'required': True},
        'is_cancelable': {'required': True},
        'is_cancel_requested': {'required': True},
        'attempt_number': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'progress': {'key': 'progress', 'type': 'str'},
        'is_cancelable': {'key': 'isCancelable', 'type': 'bool'},
        'is_cancel_requested': {'key': 'isCancelRequested', 'type': 'bool'},
        'attempt_number': {'key': 'attemptNumber', 'type': 'int'},
    }

    def __init__(self, id, progress, is_cancelable, is_cancel_requested, attempt_number):
        self.id = id
        self.progress = progress
        self.is_cancelable = is_cancelable
        self.is_cancel_requested = is_cancel_requested
        self.attempt_number = attempt_number