from peewee import *


class Admin(Model):
    """Admin model."""

    # username = CharField(max_length=255, unique=True)
    id = IntegerField(unique=True)

    class Meta:
        """Import db."""

        database = SqliteDatabase('bot.db')
