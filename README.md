# Welcome

### In this repository I was required to create a login page using python and flask. It contains the following:
- Using python functions
- Using flask
- Integrating HTML with python
- Login in function
- Register page
- Python quiz
- Saving data into CSV files
- Error function after 3 unsucessfull attempts


#### importing flask modules:
```python
from flask import *
from functools import wraps
```

#### Directing to main page
```python
@app.route("/")
def welcome ():
    return render_template('welcome.html')
```

#### Creating login function
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'daniel' or request.form['password'] != '12345':
            error = 'Invalid Credentials. Please try again.'
            attempt = session.get('attempt')
            attempt -= 1
            session['attempt'] = attempt
            if attempt == 1:
                flash("Last chance")
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
```