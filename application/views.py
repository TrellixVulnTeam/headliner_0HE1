from flask import render_template, request, redirect, url_for
from application import app
from .forms import *
from . import controllers as controller


@app.route('/', methods=['GET', 'POST'])
def index():
	form = HeadlineForm(request.form, csrf_enabled=False)
	# headline = request.form['headline']
	if request.method == 'POST' and form.validate():
		headline=form.headline.data
		controller.get_headline(headline)
		return redirect('/display')
	return render_template('index.html', form=form)

@app.route('/display')
def display():
	return render_template('test.html')
