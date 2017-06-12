# Telegram Bot for Pizzeria

This bot prints the pizzeria's menu from db to  telegram chat.

## Installation

- Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)
- Put your token, login and password for admin site into dev.env
```
$ pip install -r requirements.txt
$ . dev.env
$ python db_create.py
$ python load_initial_menu_in_db.py
```

## Usage

##### Run bot:
```
$ python bot.py
```
##### Run admin site
```
$ python server.py
```
go to [/admin](http://127.0.0.1:5000/admin/)

## Requirements

- Python >= 3.5

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
