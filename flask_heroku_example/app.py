import os
import psycopg2
from flask import Flask, render_template, g
import test
from flask import Flask, render_template, jsonify, request, session, redirect
import warnings, csv


app = Flask(__name__, template_folder="htmltemplates")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))


@app.before_request
def before_request():
    g.db_conn = connect_db()


@app.route('/')
def index():
    cur = g.db_conn.cursor()
    cur.execute("SELECT * FROM country;")

    return render_template('index.html')

@app.route("/about")
def about():
    return "<h1>About page</h1>"

@app.route("/update",methods= ['GET'])
def update():

    final_string = str(main())
    return jsonify(keke=final_string)

@app.route("/login", methods= ['POST'])
def login():
    username= request.form['username']
    password= request.form['password']
    if username=="username" and password=="password":
        session['username'] = 'admin'
        return redirect('/dashboard')
    else:
        return render_template('index.html', message="Wrong username/password!")



@app.route("/dashboard", methods= ['GET'])
def dshboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')



@app.route("/logout", methods= ['GET'])
def logout():
    session.pop('username', None)
    return redirect('/')




#if __name__ == '__main__':

    #app.run(debug=True)
