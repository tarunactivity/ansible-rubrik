# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkUpdateDetail(Model):
    """BulkUpdateDetail.

    :param notification_ids:
    :type notification_ids: list of str
    :param state:
    :type state: str
    """

    _validation = {
        'notification_ids': {'required': True},
        'state': {'required': True},
    }

    _attribute_map = {
        'notification_ids': {'key': 'notificationIds', 'type': '[str]'},
        'state': {'key': 'state', 'type': 'str'},
    }

    def __init__(self, notification_ids, state):
        self.notification_ids = notification_ids
        self.state = state
