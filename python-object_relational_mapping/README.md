# python-object_relational_mapping

Connecting Python to a MySQL database, first with the raw `MySQLdb` module
and then with the SQLAlchemy ORM.

## Learning objectives

- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python class to a MySQL table

## Requirements

- Python 3.8.5, pycodestyle 2.7.*
- MySQLdb 2.0.x, SQLAlchemy 1.4.x
- Every script starts with `#!/usr/bin/python3` and is executable

## Tasks

- `0-select_states.py`: list all states from `hbtn_0e_0_usa` ordered by
  `id`, using `MySQLdb`.
