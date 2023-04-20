# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserDetail(Model):
    """UserDetail.

    :param id:
    :type id: str
    :param auth_domain_id:
    :type auth_domain_id: str
    :param username:
    :type username: str
    :param first_name:
    :type first_name: str
    :param last_name:
    :type last_name: str
    :param email_address:
    :type email_address: str
    :param contact_number:
    :type contact_number: str
    :param created_by_id:
    :type created_by_id: str
    :param create_time:
    :type create_time: str
    """

    _validation = {
        'id': {'required': True},
        'auth_domain_id': {'required': True},
        'username': {'required': True},
        'created_by_id': {'required': True},
        'create_time': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'auth_domain_id': {'key': 'authDomainId', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'contact_number': {'key': 'contactNumber', 'type': 'str'},
        'created_by_id': {'key': 'createdById', 'type': 'str'},
        'create_time': {'key': 'createTime', 'type': 'str'},
    }

    def __init__(self, id, auth_domain_id, username, created_by_id, create_time, first_name=None, last_name=None, email_address=None, contact_number=None):
        self.id = id
        self.auth_domain_id = auth_domain_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.contact_number = contact_number
        self.created_by_id = created_by_id
        self.create_time = create_time
