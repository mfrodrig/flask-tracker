from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/add", methods = ["POST"])
def add():
    #add new item
    title = request.form.get("title")
    new_item = Tracker(title=title, complete = False)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:item_id>")
def update(item_id):
    item = Tracker.query.filter_by(id=item_id).first()
    item.complete = not item.complete
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:item_id>")
def delete(item_id):
    item = Tracker.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)