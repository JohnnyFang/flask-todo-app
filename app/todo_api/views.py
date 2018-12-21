from flask import request, jsonify, Response

from app import db
from app.models import Todo, TodoSchema
from . import todo_api

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)


# endpoint to create new todo
@todo_api.route("/todo", methods=["POST"])
def add_todo():
    text = request.json['text']
    new_todo = Todo(text)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({'id': new_todo.id, 'text': new_todo.text})


# endpoint to show all todos
@todo_api.route("/todo", methods=["GET"])
def get_todo():
    all_todos = Todo.query.all()
    result = todos_schema.dump(all_todos)
    return jsonify(result.data)


# endpoint to delete todo
@todo_api.route("/todo/delete", methods=["POST"])
def todo_delete():
    ids = request.json['ids']
    for todo_id in ids:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
    db.session.commit()
    return Response(status=204)
