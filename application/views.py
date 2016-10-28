from flask import render_template, request, redirect, url_for
from application import app
from .forms import *
from . import controllers as controller



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
  form = FilterForm()
  return render_template('index.html', form=form)

@app.route('/display', methods=['GET', 'POST'])
def display():
  form = FilterForm()
  if len(request.form['headline']) == 0:
    return redirect(url_for('/'))
  else:
    headline = request.form['headline']



  return render_template('result.html', form=form, headline=headline)
