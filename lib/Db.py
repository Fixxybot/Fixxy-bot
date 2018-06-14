from peewee import *


db = SqliteDatabase('db/bot.db')


class Admin(Model):
    """Admin model."""

    # username = CharField(max_length=255, unique=True)
    id = IntegerField(unique=True)

    class Meta:
        """Import db."""

        database = db


class User(Model):
    """"User model"""

    id = IntegerField(unique=True)
    warn = IntegerField(unique=False)
    description = TextField(unique=False)
    afk = BooleanField(unique=False)

    class Meta:
        """"Import db."""
        database = db


def main():
    db = SqliteDatabase('db/bot.db')
    db.connect()
    db.create_tables([Admin, User], safe=True)
