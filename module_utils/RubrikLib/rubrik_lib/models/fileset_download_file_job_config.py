# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FilesetDownloadFileJobConfig(Model):
    """FilesetDownloadFileJobConfig.

    :param source_dir: Source directory to download from
    :type source_dir: str
    """

    _validation = {
        'source_dir': {'required': True},
    }

    _attribute_map = {
        'source_dir': {'key': 'sourceDir', 'type': 'str'},
    }

    def __init__(self, source_dir):
        self.source_dir = source_dir
