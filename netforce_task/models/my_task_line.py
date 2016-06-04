from netforce.model import Model, fields

class TaskLine(Model):
    _name="my.task.line"
    _fields={
        'task_id': fields.Many2One("my.task","Task", required=True,on_delete="cascade"),
        "description": fields.Text("Description"),
        "time_start": fields.DateTime("Start"),
        "time_end": fields.DateTime("End"),
    }

TaskLine.register()
