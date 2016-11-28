# Overview
NCAA Football Teams (Item Catalog) application built with Flask

# How to run the application:
- Run `pip install -r requirements.txt` to install the dependency libraries (Flask, sqlalchemy, requests and oauth2client, included in the requirements.txt file)
- Run `python db_seed.py` to populate the database
- Run `python app.py` to fire up the server at port 8000
- Go to url localhost:8000 at the browser to check the web app

# Application breakdowns
- Routing and Templating implemented with Flask
- Google+ Login used to authenticate users for creating, editing and deleting teams
- SQLAlchemy used as the ORM to communicate with the database
- RESTful API endpoints that return json files
- Front-end UI built with twitter Bootstrap


