# Flask Command Line

Flask Sample project that extends the classic Flask CLI with new commands. The code includes a few commands from a simple `hello` to something more useful like `loading` new information in the database. For newcomers, FLASK CLI gives access to the `application` context, database and helpers.  

> STATUS: WIP (work in progress)

<br />

> Features

- Custom Commands
    - Simple `Hello World` 
    - Parse input File and load the information into the database
- DB Tools: `SQLAlchemy` ORM, `Flask-Migrate` (schema migrations)
- Permissive MIT License - allows unlimited copies for hobby and commercial products
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Implementation Summary

- Code `Hello World` command
- Define a new table `Stats` (will be used to save loaded data)
- Code `Data Loader` command
    - parse the information (csv format)
    - load the information into `Stats` table 
- Show the loaded information in charts

<br />

> Links

- [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black) - Free Starter with more features:
    - Authentication, Blueprints, Dual Config (dev & production), Deploy scripts.
- [Flask Dashboard Black - Demo](https://flask-black-dashboard.appseed-srv1.com) - LIVE App deployment

<br />

## Want more? Go PRO!

PRO versions include **Premium UI Kits**, Lifetime updates and **24/7 LIVE Support** (via [Discord](https://discord.gg/fZC6hup))

| [Flask Datta PRO](https://appseed.us/admin-dashboards/flask-dashboard-dattaable-pro) | [Flask Material PRO](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [Flask Volt PRO](https://appseed.us/admin-dashboards/flask-dashboard-volt-pro) |
| --- | --- | --- |
| [![Flask Datta PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-dattaable-pro/master/media/flask-dashboard-dattaable-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-dattaable-pro) | [![Flask Material PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-material-pro/master/media/flask-dashboard-material-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-material-pro) | [![Flask Volt PRO](https://raw.githubusercontent.com/app-generator/flask-dashboard-volt-pro/master/media/flask-dashboard-volt-pro-screen.png)](https://appseed.us/admin-dashboards/flask-dashboard-volt-pro)

<br />

![Flask Dashboard - Black Design, dashboard screen.](https://raw.githubusercontent.com/app-generator/flask-command-line/master/media/flask-command-line-screen.png)

<br />

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/flask-command-line.git
$ cd flask-command-line
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install modules - SQLite Database
$ pip3 install -r requirements.txt
$
$ # OR with PostgreSQL connector
$ # pip install -r requirements-pgsql.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Start the application (development mode)
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the dashboard in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## Codebase structure

The project is coded using blueprints, app factory pattern, dual configuration profile (development and production) and an intuitive structure presented bellow:

> Simplified version

```bash
< PROJECT ROOT >
   |
   |-- app/                      # Implements app logic
   |    |-- base/                # Base Blueprint - handles the authentication
   |    |-- home/                # Home Blueprint - serve UI Kit pages
   |    |
   |   __init__.py               # Initialize the app
   |
   |-- requirements.txt          # Development modules - SQLite storage
   |-- requirements-mysql.txt    # Production modules  - Mysql DMBS
   |-- requirements-pqsql.txt    # Production modules  - PostgreSql DMBS
   |
   |-- .env                      # Inject Configuration via Environment
   |-- config.py                 # Set up the app
   |-- run.py                    # Start the app - WSGI gateway
   |
   |-- ************************************************************************
```

<br />

> The bootstrap flow

- `run.py` loads the `.env` file
- Initialize the app using the specified profile: *Debug* or *Production*
  - If env.DEBUG is set to *True* the SQLite storage is used
  - If env.DEBUG is set to *False* the specified DB driver is used (MySql, PostgreSQL)
- Call the app factory method `create_app` defined in app/__init__.py
- Redirect the guest users to Login page
- Unlock the pages served by *home* blueprint for authenticated users

<br />

## Implementation details

**@ToDo**

<br />

---
Flask Command Line - Open-source sample provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
