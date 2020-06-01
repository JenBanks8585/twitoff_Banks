# twitoff_Banks
Twitoff project

## Installation

TODO: instruction for git clone

## Setup

TODO: instruction for virtual environment

setup for database:
FLASK_APP=web_app flask db init #> generates app/migrations dir (one time)

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #>

## Usage

```sh
#Mac
FLASK_APP=hello.py flask run

#Windows

export FLASK_APP=hello.py # one-time thing, to set the env var flask run
```
