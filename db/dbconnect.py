#Function to perform db operations
import sqlite3

from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_recipe(recipe_id):
        conn = get_db_connection()
        recipe = conn.execute('SELECT * FROM recipes WHERE recipe_id = ?',
                        (recipe_id,)).fetchone()
        conn.close()
        if recipe is None:
            abort(404)
        return recipe
        