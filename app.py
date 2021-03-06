
# Here we are importing the relevent files
# from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask import *
from functools import wraps

# We are creating an object here called app
app = Flask(__name__)

app.secret_key = "secret key"

# Here we are creating the welcome method that will take us to the first page
@app.route("/")
def welcome ():
    return render_template('welcome.html')

# Direct to home page
@app.route("/home")
def home():
    session['attempt'] = 1
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

# Here we loging in, We have hard coded the login information however once the CSV file is working we will use that
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'daniel' or request.form['password'] != '12345':
            attempt = int(session.get('attempt'))
            if attempt == 2:
                flash("This is your last chance")
            if attempt == 3:
                flash('You have been logged out.')
                return render_template("error.html")
            else:
                attempt += 1
                session['attempt'] = attempt
                error = 'Invalid Credentials. Please try again'
        else:
            session['logged_in'] = True
            flash("You are logged in")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



# Here we are creating a function to disable access if the user does not login. This restricts the user from accessing the page via the URL
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
                return test(*args, **kwargs)
        else:
                flash('You must be logged in')
                return redirect(url_for('login'))
    return wrap


# Direct to quiz page
@app.route("/quiz")
def quiz():
    return render_template('quiz.html')

# Direct to welcome
@app.route("/welcome")
def back():
    return render_template("welcome.html")

@app.route("/error")
def error_message():
    return render_template("error.html")

# Logs the user out
@app.route('/logout')
def logout ():
    session.pop('Logged_in', None) # We use the pop method to reset the key back to the default value
    flash("You were logged out")
    return redirect(url_for('login'))


# Syntax to run our app
if __name__ == "__main__":
    app.run(debug=True) # Good practice to add debug = true
