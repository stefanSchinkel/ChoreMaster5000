import datetime
import calendar

from flask import render_template
from flask.views import MethodView

from . import db as _db

QS_MONTH = '''
SELECT * FROM log WHERE strftime('%Y', day) = ?
    AND  strftime('%m', day) = ?
    AND chore_id = ?
    '''
QS_CHORE = "SELECT * FROM chores WHERE chore_id = ?"


class StatsAPI(MethodView):

    def get(self, _id, year=None,):
        s_year = str(year)

        db = _db.get_db()
        chore = db.execute(QS_CHORE, (_id,)).fetchone()
        factor = int(chore["multiplier"])

        payload = []
        for month in range(1, 13):
            s_month = "%02d" % month
            res = db.execute(QS_MONTH, (s_year, s_month, _id)).fetchall()
            payload.append(self._test_render(res, year, month, factor))

        data = {
            "year" : year,
            "chore": chore["description"],
            "logs": payload
        }
        return render_template("stats.html", data=data)

    def _test_render(self, data, year, month, factor):
        dd = {}
        for row in data:
            dd.update({row["day"]: row["counter"]})

        payload = []
        # limit only to actual days
        n_days = calendar.monthrange(year, month)[1] + 1
        days = [datetime.date(year, month, day) for day in range(1, n_days)]

        for day in days:
            val = dd.get(day, 0) * factor
            if val < 50:
                payload.append("red")
            elif val < 100:
                payload.append("yellow")
            elif val >= 100:
                payload.append("green")

        return payload
