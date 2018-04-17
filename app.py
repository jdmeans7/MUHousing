from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import query

app = Flask(__name__)

querydb = query.query()


@app.route('/')
def index():
    return render_template('Index.html', s=querydb.getStudent(2))

if __name__ == '__main__':
    app.run()
