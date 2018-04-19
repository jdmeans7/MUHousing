from flask import Flask, render_template
from pymysql import *
import pymysql.cursors
#import models
#import query


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretSecret'

#connection = pymysql.connect(host='db4free.net',
#                             user='jasondmeans7',
#                             password='Shadow10',
#                             db='muhousing',
#                             charset='utf8mb4',
#                             cursorclass=pymysql.cursors.DictCursor)
connection = pymysql.connect(host='sql9.freesqldatabase.com',
                             user='sql9233446',
                             password='crjxGGauSm',
                             db='sql9233446',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `FirstName`, `LastName` FROM `Advisor` WHERE `email`=%s"
        cursor.execute(sql, ('puc@marshall.edu',))
        result = cursor.fetchone()
finally:
    connection.close()

@app.route('/')
def index():
    return render_template('Index.html', result=result)

if __name__ == '__main__':
    app.run()
