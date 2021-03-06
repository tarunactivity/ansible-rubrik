# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class X509Certificate(Model):
    """X509Certificate.

    :param cert: X.509 certificate in Base64 encoded DER format. The
     certificate should start with -----BEGIN CERTIFICATE-----
    :type cert: str
    """

    _validation = {
        'cert': {'required': True},
    }

    _attribute_map = {
        'cert': {'key': 'cert', 'type': 'str'},
    }

    def __init__(self, cert):
        self.cert = cert
