# Our main form
from flask_wtf import Form
from wtforms import TextField, FieldList, FormField
from wtforms.validators import DataRequired

class StepField(Form):
    title = TextField('Title', validators=[DataRequired()])
    body = TextField('Body', validators=[DataRequired()])

class AssetField(Form):
    title = TextField('Title', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])

class ResourceField(Form):
    title = TextField('Title', validators=[DataRequired()])
    url = TextField('URL', validators=[DataRequired()])

class LessonForm(Form):
    title = TextField('Title', validators=[DataRequired()])
    time = TextField('Time', validators=[DataRequired()])
    audience = TextField('Audience', validators=[DataRequired()])
    goals = TextField('Goals', validators=[DataRequired()])
    summary = TextField('Summary', validators=[DataRequired()])
    steps = FieldList(FormField(StepField), min_entries=2)
    assets = FieldList(FormField(AssetField), min_entries=1)
    resources = FieldList(FormField(ResourceField), min_entries=1)

    author_name = TextField('Author Name', validators=[DataRequired()])
    author_image = TextField('Author Image URL', validators=[DataRequired()])
    author_bio = TextField('Author Bio', validators=[DataRequired()])