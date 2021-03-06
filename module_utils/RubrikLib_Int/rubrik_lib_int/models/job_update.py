# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobUpdate(Model):
    """JobUpdate.

    :param affinity: Affinity of the job
    :type affinity: str
    :param cron_expression: Cron expression if it is a one time job
    :type cron_expression: str
    :param interval: Interval that define the frequency of a scheduled job
    :type interval: str
    :param retries:
    :type retries: int
    :param enabled: Flag to enable/disable a job
    :type enabled: bool
    """

    _attribute_map = {
        'affinity': {'key': 'affinity', 'type': 'str'},
        'cron_expression': {'key': 'cronExpression', 'type': 'str'},
        'interval': {'key': 'interval', 'type': 'str'},
        'retries': {'key': 'retries', 'type': 'int'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, affinity=None, cron_expression=None, interval=None, retries=None, enabled=None):
        self.affinity = affinity
        self.cron_expression = cron_expression
        self.interval = interval
        self.retries = retries
        self.enabled = enabled
