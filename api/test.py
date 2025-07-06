import time
import bd.createDb
import pprint
from flask import Flask, request
app = Flask(__name__)
import psycopg2
def connect_db():
    global conn
    if conn is None:
        conn = psycopg2.connect("dbname=meubanco user=meuusuario password=senha host=localhost")
    return conn

@app.route('/')
def get_current_time():
    sla =  connect_db()
    test =  bd.createDb.connect_db(sla)
    return test

@app.route('/api/login', methods=['GET', 'POST'])
def get_login():
    user =  request.get_json(silent=True)
    print(user)
    return user



@app.route('/api/create', methods=['GET', 'POST'])
def register_account():
    user =  request.get_json(silent=True)
    print(user)
    return user