import math
import pandas as pd
import os
import openpyxl
import pymysql

pymysql.install_as_MySQLdb()
# import database_conn as dbc                                                #uncomment for debug
import configparser
from datetime import datetime, timedelta, timezone


APP_DIR = os.path.dirname(os.path.realpath(__file__))

def read(name):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    # # исполняем SQL-запрос
    # sql="""SELECT building_number FROM clients;"""
    sqlr = f"""SELECT * FROM {name};"""
    # sqlw = f"""INSERT test (id, firstname, lastname, building_number, address, phone ) VALUES (1, "NULL", "NULL", 99, "NULL", "NULL");"""

    cursor.execute(sqlr)
    DATA = cursor.fetchall()
    print(DATA)
    # применяем изменения к базе данных
    db.commit()
    db.close()


def create_user_table(name="clients"):
    config = configparser.ConfigParser()
    config.read("config.ini")  # читаем конфиг
    # создаём подключение с помощью метода Connect
    db = pymysql.connect(host=config["database"]["host"],  # your host, usually localhost
                         port=int(config["database"]["port"]),  # your port
                         user=config["database"]["user"],  # your username
                         passwd=config["database"]["passwd"],  # your password
                         db=config["database"]["db"])  # name of the data base
    cursor = db.cursor()
    sql = f"""create TABLE {name} (id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, PRIMARY KEY (id));"""
    # sql1 = """create TABLE clients (user_id INT UNSIGNED AUTO_INCREMENT NOT NULL, firstname VARCHAR(100), lastname VARCHAR(100),building_number INT UNSIGNED, address VARCHAR(100), phone VARCHAR(100), email VARCHAR(50), counter_model VARCHAR(100), counter_vendor_number INT UNSIGNED, counter_start_date DATE, counter_start_val INT UNSIGNED, counter_end_date DATE,counter_end_val INT UNSIGNED, contact_id INT UNSIGNED NOT NULL, PRIMARY KEY (entry_id, contact_id));"""
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        print(f"таблица {name} создана успешно")
    except:
        print("что то пошло не так...")
        db.close()

def light_index(a, b, H,):
    print('test')

def test():
    df = pd.DataFrame({'Name': ['Manchester City', 'Real Madrid', 'Liverpool',
                                'FC Bayern München', 'FC Barcelona', 'Juventus'],
                       'League': ['English Premier League (1)', 'Spain Primera Division (1)',
                                  'English Premier League (1)', 'German 1. Bundesliga (1)',
                                  'Spain Primera Division (1)', 'Italian Serie A (1)'],
                       'TransferBudget': [176000000, 188500000, 90000000,
                                          100000000, 180500000, 105000000]})
    df.to_excel('./teams.xlsx')

def test1():

    # Open the Workbook
    wookbook = openpyxl.load_workbook("tables/shehovtsov/light_index.xlsx")
    # Define variable to load the wookbook
    # Define variable to read the active sheet:
    worksheet = wookbook.active
    # Iterate the loop to read the cell values
    for i in range(1, 8):
        # print(i)
        # print(col[i].value, end="\t\t")
        for col in worksheet.iter_cols(3, 19):
            # print(col)
            print(col[i].value, end="\t\t")
        print('')

# test1()
read("test")