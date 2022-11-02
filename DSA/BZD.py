import sqlite3
# import random
# from coin import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect('mentor.sqlite3')
    cursor = db.cursor()
    if db:
        print('База данных подключена!')

    # noinspection SqlNoDataSourceInspection
    db.execute('CREATE TABLE IF NOT EXISTS anketa '
               '(id INTEGER PRIMARY KEY, name TEXT, '
               'direction TEXT, age INTEGER, '
               'Groupp TEXT )')

    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()



