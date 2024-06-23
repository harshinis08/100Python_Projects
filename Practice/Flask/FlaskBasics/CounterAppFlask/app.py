from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
counter = 0


class IncrementForm(FlaskForm):
    increment = SubmitField("Increment")
    decrement = SubmitField("Decrement")
    reset = SubmitField("Reset")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = IncrementForm()
    if form.validate_on_submit():
        if form.increment.data:
            return redirect(url_for('increment'))
        elif form.decrement.data:
            return redirect(url_for('decrement'))
        else:
            return redirect(url_for('reset'))
    return render_template('index.html', form=form, counter=counter)


@app.route('/increment', methods=['GET', 'POST'])
def increment():
    global counter
    counter += 1
    return redirect(url_for('index'))


@app.route('/decrement', methods=['GET', 'POST'])
def decrement():
    global counter
    counter -= 1
    return redirect(url_for('index'))


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    global counter
    counter = 0
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
