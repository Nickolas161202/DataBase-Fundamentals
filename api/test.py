import time
import bd.createDb
from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_current_time():
    test =  bd.createDb.connect_db()
    return test