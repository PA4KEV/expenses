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

## SQL

```
CREATE TABLE expenses (
  id INT PRIMARY KEY AUTO_INCREMENT,
  description VARCHAR(64) NOT NULL,
  source VARCHAR(32) NOT NULL,
  date DATETIME NOT NULL,
  amount FLOAT NOT NULL,
);
```

```
INSERT INTO expenses (description, source, date, amount)
VALUES
('Boodschappen', 'Albert Heijn', '2023-01-14 12:00:00', 45.99),
('Clone Troopers', 'Lego store', '2023-01-12 14:30:00', 19.99);
```

## External links

* [Flask request data](https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request)
* [avoid CORS errors on localhost](https://medium.com/swlh/avoiding-cors-errors-on-localhost-in-2020-5a656ed8cefa)