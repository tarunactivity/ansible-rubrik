# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IoStat(Model):
    """IoStat.

    :param iops:
    :type iops: :class:`Iops <rubriklib_int.models.Iops>`
    :param io_throughput:
    :type io_throughput: :class:`IoThroughput
     <rubriklib_int.models.IoThroughput>`
    """

    _validation = {
        'iops': {'required': True},
        'io_throughput': {'required': True},
    }

    _attribute_map = {
        'iops': {'key': 'iops', 'type': 'Iops'},
        'io_throughput': {'key': 'ioThroughput', 'type': 'IoThroughput'},
    }

    def __init__(self, iops, io_throughput):
        self.iops = iops
        self.io_throughput = io_throughput
