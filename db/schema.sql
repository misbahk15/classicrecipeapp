DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    suitable_for INTEGER ,
    is_vegetarian TEXT,
    ingredients TEXT,
    created_date TEXT  ,
    cooking_instructions TEXT
);