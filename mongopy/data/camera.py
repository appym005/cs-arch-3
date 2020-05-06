import mongoengine


class Camera(mongoengine.Document):
    cam_id = mongoengine.IntField(required=True, default=0)
    latitude = mongoengine.StringField(required=True)
    longitude = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'camera'
    }
