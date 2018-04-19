from flask import Flask, render_template
from pymysql import *
import pymysql.cursors
#import models
import query


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretSecret'

#connection = pymysql.connect(host='db4free.net',
#                             user='jasondmeans7',
#                             password='Shadow10',
#                             db='muhousing',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)

querydb = query.query()

@app.route('/')
def index():
    return render_template('Index.html', result=querydb.getLeases("Summer"))


if __name__ == '__main__':
    app.run()
