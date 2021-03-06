# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .fileset_template_create import FilesetTemplateCreate


class FilesetTemplateDetail(FilesetTemplateCreate):
    """FilesetTemplateDetail.

    :param allow_backup_network_mounts: Include or exclude locally-mounted
     remote file systems from backups.
    :type allow_backup_network_mounts: bool
    :param allow_backup_hidden_folders_in_network_mounts: Include or exclude
     hidden folders inside locally-mounted remote file systems from backups.
    :type allow_backup_hidden_folders_in_network_mounts: bool
    :param use_windows_vss: Use VSS during Windows backups.
    :type use_windows_vss: bool
    :param name:
    :type name: str
    :param includes:
    :type includes: list of str
    :param excludes:
    :type excludes: list of str
    :param exceptions:
    :type exceptions: list of str
    :param operating_system_type: Operating system type of filesets created by
     template. Possible values include: 'Linux', 'Windows'
    :type operating_system_type: str or :class:`enum <rubriklib.models.enum>`
    :param share_type: Possible values include: 'NFS', 'SMB'
    :type share_type: str or :class:`enum <rubriklib.models.enum>`
    :param pre_backup_script: Script to run before backup of this fileset
     starts
    :type pre_backup_script: str
    :param post_backup_script: Script to run after backup of this fileset ends
    :type post_backup_script: str
    :param backup_script_timeout: Number of seconds after which the script is
     killed if it has not completed execution
    :type backup_script_timeout: long
    :param backup_script_error_handling: Action taken if script fails. Options
     are "abort", "continue"
    :type backup_script_error_handling: str
    :param id:
    :type id: str
    :param primary_cluster_id:
    :type primary_cluster_id: str
    :param is_archived:
    :type is_archived: bool
    :param host_count: Number of hosts where this template has been applied
    :type host_count: int
    :param share_count: Number of shares where this template has been applied
    :type share_count: int
    """

    _attribute_map = {
        'allow_backup_network_mounts': {'key': 'allowBackupNetworkMounts', 'type': 'bool'},
        'allow_backup_hidden_folders_in_network_mounts': {'key': 'allowBackupHiddenFoldersInNetworkMounts', 'type': 'bool'},
        'use_windows_vss': {'key': 'useWindowsVss', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'includes': {'key': 'includes', 'type': '[str]'},
        'excludes': {'key': 'excludes', 'type': '[str]'},
        'exceptions': {'key': 'exceptions', 'type': '[str]'},
        'operating_system_type': {'key': 'operatingSystemType', 'type': 'str'},
        'share_type': {'key': 'shareType', 'type': 'str'},
        'pre_backup_script': {'key': 'preBackupScript', 'type': 'str'},
        'post_backup_script': {'key': 'postBackupScript', 'type': 'str'},
        'backup_script_timeout': {'key': 'backupScriptTimeout', 'type': 'long'},
        'backup_script_error_handling': {'key': 'backupScriptErrorHandling', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'primary_cluster_id': {'key': 'primaryClusterId', 'type': 'str'},
        'is_archived': {'key': 'isArchived', 'type': 'bool'},
        'host_count': {'key': 'hostCount', 'type': 'int'},
        'share_count': {'key': 'shareCount', 'type': 'int'},
    }

    def __init__(self, allow_backup_network_mounts=None, allow_backup_hidden_folders_in_network_mounts=None, use_windows_vss=None, name=None, includes=None, excludes=None, exceptions=None, operating_system_type=None, share_type=None, pre_backup_script=None, post_backup_script=None, backup_script_timeout=None, backup_script_error_handling=None, id=None, primary_cluster_id=None, is_archived=None, host_count=None, share_count=None):
        super(FilesetTemplateDetail, self).__init__(allow_backup_network_mounts=allow_backup_network_mounts, allow_backup_hidden_folders_in_network_mounts=allow_backup_hidden_folders_in_network_mounts, use_windows_vss=use_windows_vss, name=name, includes=includes, excludes=excludes, exceptions=exceptions, operating_system_type=operating_system_type, share_type=share_type, pre_backup_script=pre_backup_script, post_backup_script=post_backup_script, backup_script_timeout=backup_script_timeout, backup_script_error_handling=backup_script_error_handling)
        self.id = id
        self.primary_cluster_id = primary_cluster_id
        self.is_archived = is_archived
        self.host_count = host_count
        self.share_count = share_count
