import mongoengine as me

class Booking(me.EmbeddedDocument):
    guest_owner_id = me.ObjectField()
    guest_snake_id = me.ObjectField()


    booked_date = me.DateTimeField()
    check_in_date = me.DateTimeField(required=True)
    check_out_date = me.DateTimeField(required=True)

    review = me.StringField()
    rating = me.IntField(default=0)
