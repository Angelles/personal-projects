from marshmallow import post_load

from .task import Task, TaskSchema
from .task_type import TaskType


class School(Task):
    def __init__(self, id, title, body, status):
        super(School, self).__init__(id, title, body, status, TaskType.SCHOOL)

    def __repr__(self):
        return '<School(name={self.description!r})>'.format(self=self)


class SchoolSchema(TaskSchema):
    @post_load
    def school(self, data, **kwargs):
        return School(**data)
