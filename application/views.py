from flask import render_template, request, redirect, url_for
from application import app
from .forms import *
from . import controllers as controller



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = FilterForm()
	return render_template('index.html', form=form)


@app.route('/tester', methods=['GET', 'POST'])
def tester():
	return render_template('test.html')

@app.route('/display', methods=['GET', 'POST'])
def display():
	form = FilterForm()
	headline = request.form['headline']
	data = (controller.get_articles(headline))
	return render_template('news_display.html', form=form, headline=headline, data=data)