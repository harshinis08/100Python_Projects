from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    SECRET_KEY='mysecretkey',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:local@localhost/local_flaskDb',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)

    def __init__(self, public_id, name):
        self.id = public_id
        self.name = name

    def __repr__(self):
        return "The id is {}, name is {}".format(self.id, self.name)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/session')
def session_data():
    if 'name' not in session:
        session['name'] = 'Tom'
    return render_template('session.html', session=session, name=session['name'])


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
