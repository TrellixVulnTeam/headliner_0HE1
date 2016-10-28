from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired

class HeadlineForm(Form):
	headline = TextField('Headline:', validators=[DataRequired()])
