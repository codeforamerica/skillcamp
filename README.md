skillcamp
=========

A #crosshack project that makes it easy for fellows to share the things they teach others.

Idea:
A framework for instructors to share their workshop curricula, assets, slides, handouts, etc. Makes it easier for groups to reproduce presentations.


Initial use case:
Code for America fellows undergo intense training in January before they head to their host cities in February. While in their cities in Feb, Code for America fellows have an opportunity to give presentations. Skill Camp is a tool to allow fellows to more easily give presentations by providing documentation from the original presenter.

## Running the code locally
### Step 1: Install dependencies
``` bash
sudo pip install -r requirements.txt
```

### Step 2: Set up local database
You'll need to set up a local postgres database.

Then define an environmental variable with your database string.

```
 export DATABASE_URL=postgres://username:password @hostname:5432/databasename
```

### Step 3: Run app

``` bash
python app.py
```

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
