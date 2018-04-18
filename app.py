from flask import Flask, render_template
from pymysql import *
import pymysql.cursors
import models
import query


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretSecret'

connection = pymysql.connect(host='7fce33ca-0ef5-4c15-a0a7-a8c5002d2c0b.mysql.sequelizer.com',
                             user='wwfrditfmmpgodzk',
                             password='cuUx4AEBhgFsD85TrxzRX7AQLmiMhLCw2FnzNviyvSHbVAQDHY6kRmGe3eUQrZtD',
                             db='db7fce33ca0ef54c15a0a7a8c5002d2c0b',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

db = query.query()

@app.route('/')
def index():
    return render_template('Index.html', s=db.getStudent(2))

if __name__ == '__main__':
    app.run()
