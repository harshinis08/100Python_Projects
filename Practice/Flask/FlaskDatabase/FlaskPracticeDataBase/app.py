from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import MySQLdb
import yaml

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'mysecretkey'


# configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="FlaskPractice123!!",
            db="flask_database"
        )

cursor = mysql.cursor()
# mysql = MySQL(app)


@app.route('/')
def dbData():

    cursor = mysql.cursor()
    if cursor.execute("""INSERT INTO user(name) VALUES('Bijli')"""):
        mysql.commit()
        return 'success', 201
    else:
        cursor.execute("""SELECT * FROM user'""")
        rv = cursor.fetchall()
        return str(rv)


@app.route('/datab')
def index():

    fruits = ['mango', 'banana', 'apple', 'grapes', 'avacado', 'pineapple']
    return render_template('index.html', fruits=fruits)


@app.route('/about')
def about():
    return redirect(url_for('index'))


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return f"Here is what you entered:{request.form['password']}"
    return render_template('submit.html')


@app.route('/css')
def css():
    return render_template('css.html')


@app.errorhandler(404)
def error_handle(e):
    return '<h1>404! This page is not found</h1>'


if __name__ == '__main__':
    app.run(debug=True)