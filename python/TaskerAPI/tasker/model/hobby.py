from marshmallow import post_load

from .task import Task, TaskSchema
from .task_type import TaskType


class Hobby(Task):
    def __init__(self, id, title, body, status):
        super(Hobby, self).__init__(id, title, body, status, TaskType.HOBBY)

    def __repr__(self):
        return '<Hobby(name={self.description!r})>'.format(self=self)


class HobbySchema(TaskSchema):
    @post_load
    def hobby(self, data, **kwargs):
        return Hobby(**data)
