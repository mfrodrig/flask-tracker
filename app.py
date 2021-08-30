from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIOINS'] = False
db = SQLAlchemy(app)

class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():
    #show all items
    tracker_list = Tracker.query.all()
    return render_template('base.html', tracker_list=tracker_list)

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)