from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
import os

db_connection = os.environ['DATABASE_URL']

#engine = create_engine('sqlite:///foo.db', echo=True)
engine = create_engine(db_connection)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
app.debug = True
app.secret_key = 'M\x97\xca\x83{\xcf\xf7Z: JF\x96\x19\xc6\x86\xe0|\x97\x94\xa9\xac\x90 '

# TODO
# - Correct validators
# - Add/remove fields
# - Database make it go

from forms import LessonForm
from models import Base, Lesson, Step

Base.metadata.create_all(engine)
# Our Routes

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create", methods=["GET", "POST"])
def create():
    form = LessonForm()

    if form.validate_on_submit():
        print request.form
        #4/0
        lesson = Lesson()
        lesson.title = request.form.get('title')
        lesson.time = request.form.get('time')
        lesson.audience = request.form.get('audience')
        lesson.goals = request.form.get('goals')
        lesson.summary = request.form.get('summary')
        session.add(lesson)
        session.flush()

        for index,step_entry in enumerate(form.steps.entries):
            step = Step()
            step.title = step_entry.title.data
            step.body = step_entry.body.data
            step.order = index
            step.lesson = lesson
            session.add(step)
            session.flush()

        session.commit()
        return redirect(url_for('view', uid=lesson.id))

    return render_template('create.html', form=form)

@app.route("/<int:uid>/view")
def view(uid):
    lesson = session.query(Lesson).get(uid)
    if lesson:
        return render_template('view.html', lesson=lesson)
    else:
        return "Not found", 404

@app.route("/<int:uid>/edit")
def edit(uid):
    return render_template('edit.html', uid=uid)

if __name__ == "__main__":
    app.run()
