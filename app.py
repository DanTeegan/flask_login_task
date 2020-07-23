
# Here we are importing the relevent files
# from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask import *
from functools import wraps

app = Flask(__name__)

app.secret_key = "secret key"

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
                return test(*args, **kwargs)
        else:
                flash('You must be logged in')
                return redirect(url_for('login'))
    return wrap

@app.route("/welcome")
@login_required
def welcome ():
    return render_template('welcome.html')


@app.route('/logout')
def logout ():
    session.pop('Logged_in', None) # We use the pop method to reset the key back to the default value
    flash("You were logged out")
    return redirect(url_for('login'))


# Syntax to run our app
if __name__ == "__main__":
    app.run(debug=True) # Good practice to add debug = true