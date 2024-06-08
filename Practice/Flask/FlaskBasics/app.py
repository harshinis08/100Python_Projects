from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/coffee')
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/coffee-machine/')
def query_strings(name='iced-latte'):
    coffe = request.args.get('name', name)
    return f"Hi you ordered {coffe} coffee"


@app.route('/user/')
@app.route('/user/<name>')
def new_query_strings(name='betty'):
    return "Hi you ordered {} coffee".format(name)



@app.route('/list')
def displayCoffee():
    coffee_list = {'iced-mocha': 3.65,
                   'iced-vanilla-mocha': 2.90,
                   'mocha-moon': 7.80,
                   'vanilla-mocha-moon': 5.65,
                   'vanilla-lavender-mocha': 8.50,
                   'iced-mocha-latte': 9.80}
    return render_template('basic.html', name=None, coffee_list=coffee_list)


if __name__ == '__main__':
    app.run(debug=True)
