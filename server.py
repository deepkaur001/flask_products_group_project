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

@app.route('/show/<id>')
def read(id):
    query = "SELECT * FROM products WHERE id=:id"
    data = {'id':id}
    mysql.query_db(query, data)
    return render_template('show.html')


@app.route('/edit/<id>')
def edit(id):
    query = '''UPDATE products SET name=:name, price=:price, stock=:stock, SKU=:SKU
                WHERE id=:id'''
    data = {
        'id': id,
        'name': request.form['name'],
        'price': request.form['price'],
        'stock': request.form['stock'],
        'SKU': request.form['SKU']
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/update/<id>', methods=['POST'])
def update(id):
    query = "UPDATE products\
             SET name = :name, price = :price,\
             stock = :stock, sku = :sku \
             WHERE id = :id"
    data = {
             'name': request.form['name'],
             'price':  request.form['price'],
             'stock': request.form['stock'],
             'sku': request.form['sku'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete/<id>')
def destroyConfirm():
    return render_template('delete.html', id=id)

@app.route('/delete/<id>', methods=['POST'])
def destroy(id):
    query = "DELETE FROM products WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
