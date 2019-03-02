from flask import  render_template
from flask.views import MethodView

from . import db as _db
class LoggerAPI(MethodView):

    def get(self):
        chores = []
        db = _db.get_db()
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
        res = db.execute("SELECT * FROM log WHERE day = date('now') and chore_id = ?", (_id,)).fetchone()
        if not res:
            suc = db.execute(
                "INSERT INTO log (day, chore_id, counter) VALUES (date('now'),  ?, ?)",(_id, 1)
            )
        else:
            cnt = res['counter']
            # not sure why safe query construction fails
            q = "UPDATE log SET counter=%d WHERE day=date('now')  AND  chore_id = %s" % (cnt+1, _id)
            suc = db.execute(q)
        db.commit()

        msg = "registerd chored {}".format(_id)
        return(msg)

