import sqlite3
import os
from datetime import datetime

conn = sqlite3.connect('database.db')

with open('db/schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO recipes (title, suitable_for,is_vegetarian,ingredients,cooking_instructions,created_date) VALUES (?, ?, ?,?,?,?)",
            ('Red sauce pasta',4,'Yes','basil,onion,garlic,tomato','A great introduction to pasta for kids – loads of fun to eat, and a brilliant base for adding all kinds of other fresh ingredients. ',datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M'))
            )

cur.execute("INSERT INTO recipes (title, suitable_for,is_vegetarian,ingredients,cooking_instructions,created_date) VALUES (?, ?, ?,?,?,?)",
            ('Chicken Chilly',6,'No','chicken,capsicum,garlic,chillies,tomato','A great recipe for all those non-veg lovers. ',datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M'))
            )

conn.commit()
conn.close()