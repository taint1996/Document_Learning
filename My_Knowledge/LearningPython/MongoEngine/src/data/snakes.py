import mongoengine as me
import datetime as dt

class Snake(me.Document):
    registered_date = me.DateTimeField(default=dt.datetime.now)
    species = me.StringField(required=True)

    length = me.FloatField(required=True)
    name = me.StringField(required=True)
    is_venomous = me.BooleanField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'snakes'
    }
