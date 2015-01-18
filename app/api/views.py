# -*- coding: utf-8 -*-

from flask import jsonify, request, current_app, url_for

from . import api
from ..models import User, TodoList


@api.route('/user/')
def get_users():
    users = User.query.all()
    return jsonify({
        'users' : [user.to_json() for user in users]
    })


@api.route('/user/<int:id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/user/<int:id>/todolists')
def get_user_todolists(id):
    user = User.query.get_or_404(id)
    todolists = user.todolists
    return jsonify({
        'todolists': [todolist.to_json() for todolist in todolists]
    })


@api.route('/user/<int:user_id>/todolist/<int:todolist_id>')
def get_todolist_todos(todolist_id, user_id=None):
    todolist = TodoList.query.get_or_404(todolist_id)
    todos = todolist.todos
    return jsonify({
        'todos': [todo.to_json() for todo in todos]
    })
