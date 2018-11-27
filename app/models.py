from app import db, ma


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120))

    def __init__(self, text):
        self.text = text


class TodoSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'text')
