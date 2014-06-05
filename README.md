skillcamp
=========

A #crosshack project that makes it easy for fellows to share the things they teach others.

Idea:
A framework for instructors to share their workshop curricula, assets, slides, handouts, etc. Makes it easier for groups to reproduce presentations.


Initial use case:
Code for America fellows undergo intense training in January before they head to their host cities in February. While in their cities in Feb, Code for America fellows have an opportunity to give presentations. Skill Camp is a tool to allow fellows to more easily give presentations by providing documentation from the original presenter.

## Running the code locally

Skillcamp is a Python Flask application.

1.  Get started by [preparing your Python environment](https://github.com/codeforamerica/howto/blob/master/Python-Virtualenv.md) and installing [dependencies from `requirements.txt`](https://github.com/codeforamerica/howto/blob/master/Python-Virtualenv.md#install-packages).
2.  Next, prepare a [local PostgreSQL database](https://github.com/codeforamerica/howto/blob/master/PostgreSQL.md).
3.  Skillcamp uses the environment variable `DATABASE_URL` to connect to PostgreSQL; it will look something like this:
    
        postgres://username:password@hostname:5432/databasename

### Run app

When testing, run the application like this:

    $ DATABASE_URL=postgres://username:password@hostname:5432/databasename python app.py

=========
1. setup python/pip/virtualenv
2. setup postgres

export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.3/bin
ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future pip install -r requirements.txt

maya=# CREATE USER skillcamp PASSWORD 'skillcamp';
CREATE ROLE
maya=# CREATE DATABASE skillcamp OWNER=skillcamp;


## to run:
1. source virtualenv
2. DATABASE_URL
3. python app.py

## After all setup, do this to run it:
1. source ENV/bin/activate
2. export DATABASE_URL=postgres://skillcamp:skillcamp@localhost/skillcamp
3. python app.py
