from flask import Flask, render_template
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

app = Flask(__name__)
app.debug = True


# Our Routes

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/create")
def create():
    return render_template('create.html')

@app.route("/<int:uid>/view")
def view(uid):
    return render_template('view.html', uid=uid)

@app.route("/<int:uid>/edit")
def edit(uid):
    return render_template('edit.html', uid=uid)

if __name__ == "__main__":
    app.run()


# Our Models
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Text, String, Integer

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image = Column(String(255))  # Representing URL
    bio = Column(String(255))

class Lesson(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    time = Column(String(60))
    audience = Column(String(255))
    goals = Column(Text)
    summary = Column(Text)

    author = relationship('User')

class Asset(Base):
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    name = Column(String(255))

    lesson = relationship("Lesson", backref=backref("assets"))

class Resource(Base):
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    name = Column(String(255))

    lesson = relationship("Lesson", backref=backref("resources"))

class Step(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    order = Column(Integer)

    lesson = relationship("Lesson", backref=backref("step", order_by=order))