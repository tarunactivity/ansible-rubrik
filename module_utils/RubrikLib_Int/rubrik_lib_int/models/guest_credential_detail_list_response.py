# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GuestCredentialDetailListResponse(Model):
    """GuestCredentialDetailListResponse.

    :param has_more: If there is more
    :type has_more: bool
    :param data: List of matching objects
    :type data: list of :class:`GuestCredentialDetail
     <rubriklib_int.models.GuestCredentialDetail>`
    :param total: Total list responses
    :type total: int
    """

    _attribute_map = {
        'has_more': {'key': 'hasMore', 'type': 'bool'},
        'data': {'key': 'data', 'type': '[GuestCredentialDetail]'},
        'total': {'key': 'total', 'type': 'int'},
    }

    def __init__(self, has_more=None, data=None, total=None):
        self.has_more = has_more
        self.data = data
        self.total = total
