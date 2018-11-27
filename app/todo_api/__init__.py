from flask import Blueprint

todo_api = Blueprint('todo_api', __name__)

from . import views
