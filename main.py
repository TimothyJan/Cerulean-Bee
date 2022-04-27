from flask import Flask, render_template
import requests

app = Flask(__name__)
print(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/artwork_order")
def artwork_order():
    return render_template("artwork.html")

@app.route("/employee_order")
def employee_order():
    return render_template("employee.html")

@app.route("/print_order")
def print_order():
    return render_template("print.html")

if __name__ == "__main__":
    app.run(debug=True)