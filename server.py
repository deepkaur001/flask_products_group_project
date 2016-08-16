from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "spoons"

mysql = MySQLConnector(app, 'group_project')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add')
def add():
    pass


@app.route('/create', methods=['POST'])
def create():
    pass


@app.route('/show')
def read():
    pass


@app.route('/edit/<id>')
def edit(id):
    pass


@app.route('/update/<id>', methods=['POST'])
def update():
    pass


@app.route('/delete/<id>')
def destroy(id):
    pass


app.run(debug=True)
