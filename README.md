\#\# Project Title
------------------
Recipe-app

\#\# Project Description
---------------------------------
Recipe application that fetches recipes built in Flask framework and performs operations like view,create recipes, update recipes and delete recipe.
Please read test_request file for testing the Application and understanding more. 
Backend embedded database used - SQLite

\#\# Software Prerequisites
---------------------------------------
-   Python Version 3.9 
-   Python Packages required for installation are mentioned in requirements.txt file of project.
-   IDE - Pycharm Community Edition 2020.3.1

\#\# Database Prerequisites
------------------------ 
-   SQLite3

\#\# Operating System
------------------------------
- Windows Operating System

\#\# Front-End
-------------------------------
HTML, CSS 
Built using Flask render_template() and Jinja template engine

\#\# Installation
------------------------------------
- Install Python Version 3.9 [python.org](https://www.python.org/)
- Install IDE of choice

\#\# How to run
------------------------------------
- Perform all installations mentioned above and clone this repository
- Install all libraries as mentioned in requirements.txt
- Run following to setup the Database  : python db/init_sqlite.py
- Set environment variables via terminal:
    - set FLASK_APP=appsql
- Start up the flask application on your local machine: flask run
- The application will be up and running on http://127.0.0.1:5000/
- Application supports following APIs:
    - View all recipes
    - Create new recipe
    - Update existing recipe
    - Delete recipe

\#\#Application Purpose
-----------------------
The purpose of application is to perform CRUD operations on  recipe application.

\#\# Framework Choosen
-----------------------
- Flask is a Micro-framework  these are normally framework with little to no dependencies to external libraries. 
- Pros would be that the framework is light, there are little dependency to update and watch for security bugs
- Cons is that some time you will have to do more work by yourself or increase yourself the list of dependencies by adding plugins.
- Such frameworks could be used for basic CRUD operations for small set of users where records are less.

\#\# Technical Choices
-----------------------
- Flask 
- SQLite
- HTML,CSS,Jinja templates

\#\# Testing Methodologies
-----------------------
- Test cases are available in test.py file and can be checked by executing command python -m unittest in pycharm terminal.

\#\# Support
------------

For any queries and issues the user can contact Author Support Email id
- misbahmkhan996@gmail.com

\#\# Authors and Acknowledgements.
----------------------------------

Author's mail id - misbahmkhan996@gmail.com

\#\# License
------------------------------------
-Windows license Microsoft Windows License within the End-User License
Agreement (EULA) or [License
Terms](https://www.microsoft.com/en-in/useterms) that accompany the
content or are provided in the following guidelines. - Python license
[Python License Copyright](https://www.python.org/doc/copyright/)
1991-1995 by Stichting Mathematisch Centrum, Amsterdam, The Netherlands.

