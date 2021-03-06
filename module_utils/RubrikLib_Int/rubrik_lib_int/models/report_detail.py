# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportDetail(Model):
    """ReportDetail.

    :param name: The name of the report.
    :type name: str
    :param filters: Filter properties to update.
    :type filters: :class:`FilterSummary <rubriklib_int.models.FilterSummary>`
    :param chart0: Chart0 properties to update.
    :type chart0: :class:`ChartSummary <rubriklib_int.models.ChartSummary>`
    :param chart1: Chart1 properties to update.
    :type chart1: :class:`ChartSummary <rubriklib_int.models.ChartSummary>`
    :param table: Table properties to update.
    :type table: :class:`TableSummary <rubriklib_int.models.TableSummary>`
    :param id: ID of the report.
    :type id: str
    :param report_type: Type of the report. Possible values include: 'Canned',
     'Custom'
    :type report_type: str or :class:`enum <rubriklib_int.models.enum>`
    :param update_status: The most recent update status of this report. NOTE:
     This field is likely to change
    :type update_status: str
    """

    _validation = {
        'name': {'required': True},
        'filters': {'required': True},
        'chart0': {'required': True},
        'chart1': {'required': True},
        'table': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'filters': {'key': 'filters', 'type': 'FilterSummary'},
        'chart0': {'key': 'chart0', 'type': 'ChartSummary'},
        'chart1': {'key': 'chart1', 'type': 'ChartSummary'},
        'table': {'key': 'table', 'type': 'TableSummary'},
        'id': {'key': 'id', 'type': 'str'},
        'report_type': {'key': 'reportType', 'type': 'str'},
        'update_status': {'key': 'updateStatus', 'type': 'str'},
    }

    def __init__(self, name, filters, chart0, chart1, table, id=None, report_type=None, update_status=None):
        self.name = name
        self.filters = filters
        self.chart0 = chart0
        self.chart1 = chart1
        self.table = table
        self.id = id
        self.report_type = report_type
        self.update_status = update_status
