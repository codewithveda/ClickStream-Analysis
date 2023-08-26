# import main Flask class and request object
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from urllib.request import urlopen
from flask_mysqldb import MySQL
import json
from urllib.request import urlopen
from datetime import date
import time

# create the Flask app
asakthi@33
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vedasakthi@33'
app.config['MYSQL_DB'] = 'backend'

mysql = MySQL(app)

html=urlopen('file:C:/Users/Veda Prakash K/PycharmProjects/clickstream/templates/index.html')

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/move_forward')
def move_forward():
    ip = request.remote_addr
    soup = BeautifulSoup(html, 'html.parser')
    soup2 = soup.find('h1')
    product = soup2.text
    location="Chennai"
    if product is not None:
        product_text = product
    else:
      "handle the case where the h1 element was not found"
    today = date.today()
    timestamp = time.time()
    formatted_time = time.strftime('%H:%M:%S', time.localtime(timestamp))
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO veda1(ip, product, date, time, location) VALUES (%s, %s, %s, %s, %s)", (ip, product, today, formatted_time, location))
    mysql.connection.commit()
    cur.close()

    return render_template('cart.html')


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)