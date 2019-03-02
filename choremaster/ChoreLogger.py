from flask import  render_template
from flask.views import MethodView

class LoggerAPI(MethodView):

    def get(self):
        chores = [ {"id": 1, "name": "pushups", "multiplier": 10}]
        return render_template('main.html', chores=chores)


    def post(self, chore_id):
        msg = "registerd chored {}".format(chore_id)
        return(msg)

