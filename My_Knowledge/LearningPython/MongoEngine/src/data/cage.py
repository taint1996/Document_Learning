import mongoengine as me
import datetime as dt

class Cage(me.Document):
    registered_date = me.DateTimeField(default=dt.datetime.now)

    name = me.StringField(required=True)
    price = me.FloatField(required=True)
    square_meters = me.FloatField(required=True)
    is_carpeted = me.BooleanField(required=True)
    has_toys = me.BooleanField(required=True)
    allow_dangerous_snakes = me.BooleanField(default=False)

    bookings = me.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }
