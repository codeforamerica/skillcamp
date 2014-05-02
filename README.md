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
