
# Our Models
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Text, String, Integer, ForeignKey

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    image = Column(String(255))  # Representing URL
    bio = Column(String(255))

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    time = Column(String(60))
    audience = Column(String(255))
    goals = Column(Text)
    summary = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User')

class Asset(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    name = Column(String(255))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))

    lesson = relationship("Lesson", backref=backref("assets"))

class Resource(Base):
    __tablename__ = 'resources'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    name = Column(String(255))
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    lesson = relationship("Lesson", backref=backref("resources"))

class Step(Base):
    __tablename__ = 'steps'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    order = Column(Integer)
    lesson_id = Column(Integer, ForeignKey('lessons.id'))
    lesson = relationship("Lesson", backref=backref("steps", order_by=order))