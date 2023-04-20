# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class StartTimeAttributes(Model):
    """StartTimeAttributes.

    :param minutes:
    :type minutes: int
    :param hour:
    :type hour: int
    :param day_of_week:
    :type day_of_week: int
    :param day_of_month:
    :type day_of_month: int
    :param week_of_month:
    :type week_of_month: int
    :param month:
    :type month: int
    :param year:
    :type year: int
    """

    _validation = {
        'minutes': {'required': True},
        'hour': {'required': True},
    }

    _attribute_map = {
        'minutes': {'key': 'minutes', 'type': 'int'},
        'hour': {'key': 'hour', 'type': 'int'},
        'day_of_week': {'key': 'dayOfWeek', 'type': 'int'},
        'day_of_month': {'key': 'dayOfMonth', 'type': 'int'},
        'week_of_month': {'key': 'weekOfMonth', 'type': 'int'},
        'month': {'key': 'month', 'type': 'int'},
        'year': {'key': 'year', 'type': 'int'},
    }

    def __init__(self, minutes, hour, day_of_week=None, day_of_month=None, week_of_month=None, month=None, year=None):
        self.minutes = minutes
        self.hour = hour
        self.day_of_week = day_of_week
        self.day_of_month = day_of_month
        self.week_of_month = week_of_month
        self.month = month
        self.year = year
