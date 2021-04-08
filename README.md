# Flask Command Line

Flask Sample project that extends the classic Flask CLI with new commands. The code includes a few commands from a simple `hello` to something more useful like `listing` the application configuration. For newcomers, FLASK CLI gives access to the `application` context, database and helpers.  

<br />

> Features

- Define a new Blueprint `commands`
- Define Custom Command `hello` that echos a simple `Hello World`
    - Usage: `flask commands hello`
- Define Custom Command `cfg` that prints all configuration variables and optionally filter the output.
    - Usage: `flask commands cfg` - print all variables used by the app
    - Usage: `flask commands cfg SQL` - filtered output
- Support via **Github** (issues tracker) and [Discord](https://discord.gg/fZC6hup).

<br />

> Implementation Summary

- Create the [commands](./app/commands.py) Blueprint
- Update the `app factory` to include and register the Blueprint
- Code `Hello World` command
- Code `Cfg` command

<br />

> Links

- [Flask Dashboard Black](https://appseed.us/admin-dashboards/flask-dashboard-black) - Free Starter with more features:
    - Authentication, Blueprints, Dual Config (dev & production), Deploy scripts.
- [Flask Dashboard Black - Demo](https://flask-black-dashboard.appseed-srv1.com) - LIVE App deployment

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
$ # List available commands 
$ flask commands # commands = the name of the Blueprint
$
$ # Call Hello Command
$ flask commands hello # this will print a dummy message
$
$ # Call CFG Command
$ flask commands cfg     # list all variables
$ flask commands cfg sql # filter the output that matches `SQL` 
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
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

## Sample Output

> Command `hello` - to customize the message, open the [commands](./app/commands.py) file and update `hello()`

```bash
$ flask commands hello
Custom command - Hello # <-- the output 
```

<br />

> Command `cfg` - Unfiltered output

```bash
$ flask commands cfg
Custom command - Cfg(None)
  |- ENV -> production
  |- DEBUG -> False
  |- TESTING -> False
  |- PROPAGATE_EXCEPTIONS -> None
  |- PRESERVE_CONTEXT_ON_EXCEPTION -> None
  |- SECRET_KEY -> S3cr3t_K#Key
  |- PERMANENT_SESSION_LIFETIME -> 31 days, 0:00:00
  |- USE_X_SENDFILE -> False
  |- SERVER_NAME -> None
  |- APPLICATION_ROOT -> /
  |- SESSION_COOKIE_NAME -> session
  |- SESSION_COOKIE_DOMAIN -> None
  |- SESSION_COOKIE_PATH -> None
  |- SESSION_COOKIE_HTTPONLY -> True
  |- SESSION_COOKIE_SECURE -> False
  |- SESSION_COOKIE_SAMESITE -> None
...
(truncated output)
```

<br />

> Command `cfg` - Filtered output (case insensitive)

```bash
$ # Filter ouput that matches `database`  
$ flask commands cfg database
Custom command - Cfg(Filter=database)
  |- SQLALCHEMY_DATABASE_URI -> sqlite:///...\flask-command-line-blueprints\db.sqlite3
$  
$ # Filter ouput that matches `JSON`
$ flask commands cfg JSON
Custom command - Cfg(Filter=JSON)
  |- JSON_AS_ASCII -> True
  |- JSON_SORT_KEYS -> True
  |- JSONIFY_PRETTYPRINT_REGULAR -> False
  |- JSONIFY_MIMETYPE -> application/json
```

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
   |   commands.py               # Defines the custom commands                 <-- NEW
   |   __init__.py               # Initialize the app                          <-- UPDATED
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

---
Flask Command Line - Open-source sample provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
