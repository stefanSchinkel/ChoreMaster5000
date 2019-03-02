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
        msg = "registerd chored {}".format(_id)
        return(msg)

