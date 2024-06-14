from flask import Flask, render_template, redirect, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, RadioField,
                    BooleanField, SelectField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please chose your mood? ", choices=[('mood_one', 'happy'),
                                                           ('mood_two', 'excited')])
    food_choice = SelectField(u'Pick your favorite food: ', choices=[('chi', 'Chicken'),
                                                                     ('fi', 'fish'),
                                                                     ('to', 'tofu')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")


class SimpleForm(FlaskForm):
    breed = StringField("What breed are you?", validators=[DataRequired()])
    submit = SubmitField("Click Me.")


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/breed', methods=['GET', 'POST'])
def breedName():

    form = SimpleForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to {session['breed']}")

        return redirect(url_for('breedName'))

    return render_template('breed.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)