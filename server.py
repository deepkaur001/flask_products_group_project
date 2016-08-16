from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "spoons"

mysql = MySQLConnector(app, 'group_project')


@app.route('/')
def index():
    query="SELECT * FROM products"
    return render_template("index.html", products=mysql.query_db(query))


@app.route('/add')
def add():
    return render_template("add.html")


@app.route('/create', methods=['POST'])
def create():
    query = "INSERT INTO products (name, price, stock, sku, created_at, updated_at)
             VALUES (:name, :price, :stock, :sku, NOW(), NOW())"
    data = {
             'name': request.form['name'],
             'price':  request.form['price'],
             'stock':  request.form['stock'],
             'sku': request.form['sku']
           }
    mysql.query_db(query, data)
    return redirect('/')

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
