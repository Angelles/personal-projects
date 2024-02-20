import datetime as dt

from marshmallow import Schema, fields


class Task(object):
    def __init__(self, id, title, body, status, type):
        self.id = id
        self.title = title
        self.body = body
        self.create_date = dt.datetime.now()
        self.status = status
        self.type = type

    def __repr__(self):
        return '<Task(name={self.title!r})>'.format(self=self)


class TaskSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    body = fields.Str()
    created_at = fields.Date()
    status = fields.Str()
    type = fields.Str()
