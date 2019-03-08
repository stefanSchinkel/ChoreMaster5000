from flask import  render_template, jsonify
from flask.views import MethodView

from . import db as _db

QS_DAY = "SELECT * FROM log WHERE day = date('now') and chore_id = ?"
QS_INSERT = "INSERT INTO log (day, chore_id, counter) VALUES (date('now'),  ?, ?)"
# not sure why safe query construction fails
QS_UPDATE = "UPDATE log SET counter=%d WHERE day=date('now')  AND  chore_id = %s"


class LoggerAPI(MethodView):

    def get(self, _id=None):

        # for ajax only
        db = _db.get_db()
        if _id:
            res = db.execute(QS_DAY, (_id,)).fetchone()
            return jsonify({"count": res['counter']})

        # render actual page
        chores = []
        res = db.execute('SELECT * FROM chores').fetchall()
        for item in res:
            chores.append({
                "id": item['chore_id'],
                "name": item["description"],
                "multiplier": item["multiplier"]
            })
        return render_template('main.html', chores=chores)


    def post(self, _id):
        db = _db.get_db()
        res = db.execute(QS_DAY, (_id,)).fetchone()
        if not res:
            suc = db.execute(QS_INSERT, (_id, 1))
        else:
            cnt = res['counter']
            suc = db.execute( QS_UPDATE % (cnt+1, _id))
        db.commit()

        msg = "registered chored {}".format(_id)
        return msg, 201

