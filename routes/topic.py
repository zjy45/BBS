from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.topic import Topic
from models.board import Board
from models.reply import Reply


main = Blueprint('topic', __name__)


@main.route("/")
def index():
    # board_id = 2
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.find_all(deleted=False)
    else:
        ms = Topic.find_all(board_id=board_id, deleted=False)
    u = current_user()
    bs = Board.find_all(deleted=False)
    us = User.find_all(deleted=False)
    ts = Topic.find_all(deleted=False)
    rs = Reply.find_all(deleted=False)
    print("username", u.username)
    return render_template("topic/index2.html", ms=ms, bs=bs, us=us, ts=ts, rs=rs)


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)
    print("t.board()", m.board())
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Topic.new(form, user_id=u.id)
    return redirect(url_for('.detail', id=m.id))


@main.route("/delete")
def delete():
    id = int(request.args.get('id'))
    u = current_user()
    t = Topic.find(id)
    if u.id == t.user().id:
        if u is not None:
            print('删除 topic 用户是', u, id)
            t.delete()
            return redirect(url_for('.index'))
        else:
            abort(404)
    else:
        abort(403)


@main.route("/new")
def new():
    bs = Board.find_all(deleted=False)
    return render_template("topic/new.html", bs=bs)


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('index.index'))
    else:
        return render_template('profile.html', user=u)


@main.route('/user<int:id>')
def user(id):
    u = User.find(id)
    if u is None:
        return abort(404)
    else:
        return render_template('user.html', user=u)


@main.context_processor
def include_user_class():
    u = current_user()
    return {'u': u}