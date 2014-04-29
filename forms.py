# Our main form
from flask_wtf import Form
from wtforms import TextField, FieldList, FormField
from wtforms.validators import DataRequired

class StepField(Form):
    title = TextField('Title', validators=[])
    body = TextField('Body', validators=[])

class AssetField(Form):
    title = TextField('Title', validators=[])
    url = TextField('URL', validators=[])

class ResourceField(Form):
    title = TextField('Title', validators=[])
    url = TextField('URL', validators=[])

class LessonForm(Form):
    title = TextField('Title', validators=[])
    time = TextField('Time', validators=[])
    audience = TextField('Audience', validators=[])
    goals = TextField('Goals', validators=[])
    summary = TextField('Summary', validators=[])
    steps = FieldList(FormField(StepField), min_entries=5)
    assets = FieldList(FormField(AssetField), min_entries=1)
    resources = FieldList(FormField(ResourceField), min_entries=1)

    author_name = TextField('Author Name', validators=[])
    author_image = TextField('Author Image URL', validators=[])
    author_bio = TextField('Author Bio', validators=[])