from flask import Flask, render_template
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

app = Flask(__name__)
app.debug = True
app.secret_key = 'M\x97\xca\x83{\xcf\xf7Z: JF\x96\x19\xc6\x86\xe0|\x97\x94\xa9\xac\x90 '

# TODO
# - Correct validators
# - Add/remove fields
# - Database make it go

from forms import LessonForm

# Our Routes

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create", methods=["GET", "POST"])
def create():
    form = LessonForm()
    return render_template('create.html', form=form)

@app.route("/<int:uid>/view")
def view(uid):
    return render_template('view.html', uid=uid)

@app.route("/<int:uid>/edit")
def edit(uid):
    return render_template('edit.html', uid=uid)

if __name__ == "__main__":
    app.run()