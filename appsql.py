from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from db import dbconnect as db
from datetime import datetime
from http_response_code import HTTPResponseCode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'recipeapp'

@app.route('/')
def index():
    conn = db.get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)

@app.route('/<int:recipe_id>')
def recipe(recipe_id):
    recipe = db.get_recipe(recipe_id)
    return render_template('recipe.html', recipe=recipe)

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        suitable_for = request.form['suitable_for']
        is_vegetarian = request.form['isveg']
        ingredients = request.form['ingredients']
        cooking_instructions = request.form['cookinginstructions']

        if not title:
            flash('Title is required!')
        else:
            conn = db.get_db_connection()
            conn.execute("INSERT INTO recipes (title, suitable_for, is_vegetarian,ingredients, cooking_instructions,created_date) VALUES (?, ?, ?,?,?,?)",
            (title, suitable_for,is_vegetarian,ingredients,cooking_instructions,datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M'))
            )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:recipe_id>/edit', methods=('GET', 'POST'))
def edit(recipe_id):
    recipe = db.get_recipe(recipe_id)

    if request.method == 'POST':
        title = request.form['title']
        suitable_for = request.form['suitable_for']
        is_vegetarian = request.form['isveg']
        ingredients = request.form['ingredients']
        cooking_instructions = request.form['cookinginstructions']

        if not title:
            flash('Title is required!')
        else:
            conn = db.get_db_connection()
            conn.execute('UPDATE recipes SET title = ?, suitable_for = ?,is_vegetarian = ?,ingredients = ?,cooking_instructions=?'
                         ' WHERE recipe_id = ?',
                         (title, suitable_for,is_vegetarian,ingredients,cooking_instructions,recipe_id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', recipe=recipe)

@app.route('/<int:recipe_id>/delete', methods=('POST',))
def delete(recipe_id):
    recipe = db.get_recipe(recipe_id)
    conn = db.get_db_connection()
    conn.execute('DELETE FROM recipes WHERE recipe_id = ?', (recipe_id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(recipe['title']))
    return redirect(url_for('index'))
