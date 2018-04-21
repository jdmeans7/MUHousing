from flask import Flask, render_template, redirect, url_for, request
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

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Index.html')

@app.route('/func', methods=['POST'])
def function1():
    print("Hello")
    return redirect(url_for('query1'))

@app.route('/query1', methods=['GET', 'POST'])
def query1():
    choice = request.form['query']
    if choice == "query1":
        result = querydb.getManagers("Hall")
    elif choice == "query2":
        result = querydb.getStudentsLeases()
    elif choice == "query3":
        result = querydb.getLeases("Summer")
    elif choice == "query4":
        result = querydb.getTotalRent(2)
    return render_template('query1.html', result=result)

#@app.route('/query2', methods=['GET','POST'])
#def query2():
#    result = querydb.getLeases('Summer')
#    return redirect(url_for('query1'))


if __name__ == '__main__':
    app.run()
