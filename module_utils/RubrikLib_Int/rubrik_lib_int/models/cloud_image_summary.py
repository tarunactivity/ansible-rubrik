# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloudImageSummary(Model):
    """CloudImageSummary.

    :param id: The ID of the image
    :type id: str
    :param snapshot_id: The ID of the snapshot the image was generated from
    :type snapshot_id: str
    :param snappable_id: The ID of the snappable the snapshot was taken of.
     This can be used to get context about the image if the snapshot has since
     been expired. Will be empty if the snappable is not available.
    :type snappable_id: str
    :param snappable_name: The name of the source snappable. Will be empty if
     the snappable is not available.
    :type snappable_name: str
    :param snapshot_creation_date: The creation date of the snapshot this
     image is based on. This can be used to get context about the image if the
     snapshot has since been expired.
    :type snapshot_creation_date: datetime
    :param location_id: The ID of the location the image is on
    :type location_id: str
    :param location_name: The name of the location the image is on
    :type location_name: str
    :param image_id: The image the cloud instance was generated from
    :type image_id: str
    :param creation_date: The date the image was created
    :type creation_date: datetime
    :param expiration_date: The date the iamge is scheduled for expiration
    :type expiration_date: datetime
    :param links:
    :type links: :class:`CloudImageSummaryLinks
     <rubriklib_int.models.CloudImageSummaryLinks>`
    """

    _validation = {
        'id': {'required': True},
        'snapshot_id': {'required': True},
        'snapshot_creation_date': {'required': True},
        'location_id': {'required': True},
        'location_name': {'required': True},
        'image_id': {'required': True},
        'creation_date': {'required': True},
        'links': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'snapshot_id': {'key': 'snapshotId', 'type': 'str'},
        'snappable_id': {'key': 'snappableId', 'type': 'str'},
        'snappable_name': {'key': 'snappableName', 'type': 'str'},
        'snapshot_creation_date': {'key': 'snapshotCreationDate', 'type': 'iso-8601'},
        'location_id': {'key': 'locationId', 'type': 'str'},
        'location_name': {'key': 'locationName', 'type': 'str'},
        'image_id': {'key': 'imageId', 'type': 'str'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'expiration_date': {'key': 'expirationDate', 'type': 'iso-8601'},
        'links': {'key': 'links', 'type': 'CloudImageSummaryLinks'},
    }

    def __init__(self, id, snapshot_id, snapshot_creation_date, location_id, location_name, image_id, creation_date, links, snappable_id=None, snappable_name=None, expiration_date=None):
        self.id = id
        self.snapshot_id = snapshot_id
        self.snappable_id = snappable_id
        self.snappable_name = snappable_name
        self.snapshot_creation_date = snapshot_creation_date
        self.location_id = location_id
        self.location_name = location_name
        self.image_id = image_id
        self.creation_date = creation_date
        self.expiration_date = expiration_date
        self.links = links
