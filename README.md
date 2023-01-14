# Expenses
expenditure tracking application.

# PMA
## Progressive Web Application

Basically a website that can be installable, work in offline mode, send notifications and behave like a native application.

# API
## REST application programming interface

Python API to interact, manipulate and sanitize data with.
Flask-API is used.

---

## Docker


### API

`docker build -t exp_api:latest api/`

`docker run -p 80:5000 -d --name exp_api exp_api`

### Database

`docker build -t exp_db:latest config/database/`

`docker run -d --name exp_db exp_db`