from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/create_recipe', methods=["POST"] )
def create_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.valid_recipe(request.form):
        return redirect('/create')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
        "time" : request.form['time'],
        "instruction" : request.form['instruction'],
        "date_made" : request.form['date_made'],
        "user_id" : request.form['user_id'],
    }
    Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/edit_recipe', methods=["POST"] )
def edit_recipe():
    if 'user_id' not in session:
        return redirect('/')
    if not Recipe.valid_recipe(request.form):
        return redirect('/edit')
    data = {
        "id" : request.form['id'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "time" : request.form['time'],
        "instruction" : request.form['instruction'],
        "date_made" : request.form['date_made'],
        "user_id" : request.form['user_id'],
    }
    Recipe.edit_recipe(data)
    return redirect('/dashboard')

@app.route('/create')
def create():
    data ={
        'id': session['user_id']
    }
    user=User.get_by_id(data)
    return render_template("new_recipe.html", user=user)