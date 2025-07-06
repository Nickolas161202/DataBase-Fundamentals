import time
import bd.createDb
import pprint
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def get_current_time():
    test =  bd.createDb.connect_db()
    return test

@app.route('/api/login', methods=['GET', 'POST'])
def get_login():
    
    user =  request.get_json(silent=True) 
    print(user)
    
    return user