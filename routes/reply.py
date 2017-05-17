from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort,
)

from routes import *

from models.reply import Reply


main = Blueprint('reply', __name__)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    print('DEBUG', form)
    m = Reply.new(form, user_id=u.id)
    return redirect(url_for('topic.detail', id=m.topic_id))


@main.route("/delete")
def delete():
    r_id = int(request.args.get('id'))
    u = current_user()
    r = Reply.find_by(id=r_id)
    print("r.user()", r.user())
    if r.user().id == u.id:
        if u is not None:
            print('删除 topic 用户是', u, id)
            r.delete()
            return redirect(url_for('topic.detail', id=r.topic_id))
        else:
            abort(404)
    else:
        abort(403)