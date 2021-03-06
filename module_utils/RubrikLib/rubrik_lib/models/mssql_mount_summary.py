# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MssqlMountSummary(Model):
    """MssqlMountSummary.

    :param id:
    :type id: str
    :param source_database_id:
    :type source_database_id: str
    :param source_database_name:
    :type source_database_name: str
    :param source_recovery_point:
    :type source_recovery_point: :class:`MssqlRecoveryPoint
     <rubriklib.models.MssqlRecoveryPoint>`
    :param target_instance_id:
    :type target_instance_id: str
    :param target_root_name: Name of the top-level object on which the target
     instance resides.
    :type target_root_name: str
    :param creation_date: The date this mount was created.
    :type creation_date: datetime
    :param owner_id: ID of the user who created this mount.
    :type owner_id: str
    :param owner_name: Name of the user who created this mount.
    :type owner_name: str
    :param status: The status of this mount. The status is **_Available_**
     when the database is successfully mounted and ready to use. Possible
     values include: 'Available', 'Unavailable', 'Mounting', 'Unmounting'
    :type status: str or :class:`enum <rubriklib.models.enum>`
    :param mounted_database_id: ID for the mounted SQL Server database, once
     it is available.
    :type mounted_database_id: str
    :param mounted_database_name: Name for the mounted SQL Server database.
    :type mounted_database_name: str
    """

    _validation = {
        'id': {'required': True},
        'source_database_id': {'required': True},
        'source_database_name': {'required': True},
        'source_recovery_point': {'required': True},
        'target_instance_id': {'required': True},
        'target_root_name': {'required': True},
        'creation_date': {'required': True},
        'status': {'required': True},
        'mounted_database_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'source_database_id': {'key': 'sourceDatabaseId', 'type': 'str'},
        'source_database_name': {'key': 'sourceDatabaseName', 'type': 'str'},
        'source_recovery_point': {'key': 'sourceRecoveryPoint', 'type': 'MssqlRecoveryPoint'},
        'target_instance_id': {'key': 'targetInstanceId', 'type': 'str'},
        'target_root_name': {'key': 'targetRootName', 'type': 'str'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'owner_name': {'key': 'ownerName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'mounted_database_id': {'key': 'mountedDatabaseId', 'type': 'str'},
        'mounted_database_name': {'key': 'mountedDatabaseName', 'type': 'str'},
    }

    def __init__(self, id, source_database_id, source_database_name, source_recovery_point, target_instance_id, target_root_name, creation_date, status, mounted_database_name, owner_id=None, owner_name=None, mounted_database_id=None):
        self.id = id
        self.source_database_id = source_database_id
        self.source_database_name = source_database_name
        self.source_recovery_point = source_recovery_point
        self.target_instance_id = target_instance_id
        self.target_root_name = target_root_name
        self.creation_date = creation_date
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.status = status
        self.mounted_database_id = mounted_database_id
        self.mounted_database_name = mounted_database_name
