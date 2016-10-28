# from flask_wtf import Form
# from wtforms import StringField, TextField
# from wtforms.validators import DataRequired

# class HeadlineForm(Form):
# 	headline = TextField('Headline:', validators=[DataRequired()])
from flask_wtf import Form
from wtforms import TextField, StringField, BooleanField
from wtforms.validators import DataRequired

class FilterForm(Form):
	headline = StringField('Headline', validators=[DataRequired()])
	