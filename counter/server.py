from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'davids_assignment'  

@app.route('/')
def index():
    if 'variable' not in session:
        session['variable'] = 1
    elif session['variable'] == 2:
        session['variable'] = 2

    if 'views_counter' not in session:
        session['views_counter'] = 1
    else:
        session['views_counter'] += session['variable'] 
    return render_template("index.html", counter=session['views_counter'])

@app.route('/button')
def button():
    session['variable'] = 2
    return redirect ('/')

@app.route('/reset')
def reset():
    session['views_counter'] = 0
    session['variable'] = 1
    return redirect ('/')
    

app.run(debug=True)