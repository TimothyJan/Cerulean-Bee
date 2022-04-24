from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Artwork_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(250), nullable=False)
    contact = db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(250), nullable=False)
    discount = db.Column(db.String(250), nullable=True)
    total_price = db.Column(db.Float, nullable=False)

    order_date = db.Column(db.Date, nullable=False)
    date_approved = db.Column(db.Date, nullable=False)
    scheduled_print_date = db.Column(db.Date, nullable=False)

    apparel_item = db.Column(db.String(250), nullable=False)
    base_color = db.Column(db.String(250), nullable=False)
    maximum_colors = db.Column(db.Integer, nullable=True)

    event = db.Column(db.String(250), nullable=True)
    theme = db.Column(db.String(250), nullable=True)

db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/artwork_order')
def artwork_order():
    return render_template("artwork_order.html")

@app.route('/employee_order')
def employee_order():
    return render_template("employee_order.html")

@app.route('/print_order')
def print_order():
    return render_template("print_order.html")

if __name__ == "__main__":
    app.run(debug=True)