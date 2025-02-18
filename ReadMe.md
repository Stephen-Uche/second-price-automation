# price_quote(Automation) module

## How to run on a local machine

- Run `cd user` to navigate to working directory
- Run the virtual environment [steps](#create-and-activate-virtual-environment)
- Run `pip install -r requirements.txt` to install the required packages within your activated environment
- Copy env.example to .env file on a bash terminal `cp env.example .env`
- Run `python -c 'import secrets; print(secrets.token_urlsafe(16))'` in the terminal to generate secret key and replace with **SECRET_KEY** value in the .env
- Run MySQL Setup [steps](#setup-mysql-database)
- Run the flask migration [steps](#migration)
- Run the app from the terminal `python run.py`

## Create and activate virtual environment

### Windows

- run `python3 -m venv venv` in the terminal to generate virtual environment
- (Bash Terminal) activate the virtual environment `source venv/Script/activate`
- (Command Prompt) activate the virtual environment `.\venv\Scripts\activate`

### Linux

- run `python3 -m venv venv` in the terminal to generate virtual environment
- (Bash Terminal) activate the virtual environment `source venv/bin/activate`

- run the command in the terminal to export Flask app name

```
export FLASK_APP=main.py
```

## Setup MySQL database

```
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE desired_database_name;
GRANT ALL PRIVILEGES ON desired_database_name.* TO 'username'@'localhost';
```

## Migration

- After creating the database `desired_database_name` as instructed above
- modify the **DB_USERNAME** and **DB_PASSWORD** to match your database user and user's password
- run the command to migrate table to existing database

```
flask db init
flask db migrate -m '<message>'
flask db upgrade
```
