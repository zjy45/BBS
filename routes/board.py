from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.board import Board


main = Blueprint('board', __name__)


def current_user():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后 User.find_by 来用 id 找用户
    # 找不到就返回 None
    uid = session.get('user_id', -1)
    u = User.find_by(id=uid)
    return u


def validate_admin():
    u = current_user()
    return u.role == 1


@main.route("/admin")
def index():
    if validate_admin():
        return render_template('board/admin_index.html')
    else:
        abort(404)


@main.route("/add", methods=["POST"])
def add():
    if validate_admin():
        form = request.form
        u = current_user()
        m = Board.new(form)
        return redirect(url_for('topic.index'))
    else:
        abort(404)


@main.route("/delete", methods=["POST"])
def delete():
    if validate_admin():
        form = request.form
        b_title = form.get('title', None)
        b = Board.find_by(title=b_title)
        b.delete()
        return redirect(url_for('topic.index'))
    else:
        abort(404)
