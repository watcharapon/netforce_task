import time

from netforce.model import Model, fields

class MyTask(Model):
    _name="my.task"
    _field_name="number"

    _fields={
        'number': fields.Char("Number",required=True),
        'date': fields.Date("Date"),
        'description': fields.Text("Description",required=True),
        "state": fields.Selection([['draft','Draft'],['wait_approve','Wait Approval'],['in_progress','In Progress'],['done','Completed']],'State'),
        'lines': fields.One2Many("my.task.line","task_id","Lines"),
    }

    _defaults={
        'date': lambda *a: time.strftime("%Y-%m-%d"),
        'state': 'draft',
    }

MyTask.register()
