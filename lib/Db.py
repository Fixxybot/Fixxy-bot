import datetime

from peewee import *

db = SqliteDatabase('db/bot.db')


class User(Model):
    """"User model"""

    id = IntegerField(unique=True)
    description = TextField(unique=False)
    afk = BooleanField(unique=False)
    group_admin = BooleanField(default=False)
    sudo_admin = BooleanField(default=False)

    class Meta:
        """"Import db."""
        database = db


class Group(Model):
    """"Group model"""

    group_id = IntegerField(unique=True)
    lang = CharField(default="en")

    class Meta:
        """"Import db"""
        database = db


class warns(Model):
    user = CharField()
    id = IntegerField()
    group = IntegerField()
    last = CharField

    class Meta:
        """"import db"""
        database = db


class commands(Model):
    """"Command model db"""
    id_group = IntegerField(unique=False)
    command = TextField()
    text = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        """"import db"""
        database = db


def main():
    db.connect()
    db.create_tables([User, Group, warns, commands], safe=True)
