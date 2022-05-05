from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

'''CREATE DATABASE'''
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Cerulean_Bee.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''CREATE TABLE'''
class Artwork_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(250), nullable=True)
    contact = db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(250), nullable=True)
    discount = db.Column(db.String(250), nullable=True)
    total_price = db.Column(db.String(250), nullable=True)

    order_date = db.Column(db.String(250), nullable=True)
    date_approved = db.Column(db.String(250), nullable=True)
    scheduled_print_date = db.Column(db.String(250), nullable=True)

    apparel_item = db.Column(db.String(250), nullable=True)
    base_color = db.Column(db.String(250), nullable=True)
    maximum_colors = db.Column(db.Integer, nullable=True)

    event = db.Column(db.String(250), nullable=True)
    theme = db.Column(db.String(250), nullable=True)

class Employee_Work_Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(250), nullable=True)
    full_part_time = db.Column(db.String(250), nullable=True)

    date = db.Column(db.String(250), nullable=True)
    start_time = db.Column(db.String(250), nullable=True)
    project = db.Column(db.String(250), nullable=True)
    art_item = db.Column(db.String(250), nullable=True)
    task = db.Column(db.String(250), nullable=True)
    end_time = db.Column(db.String(250), nullable=True)

class Print_Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(250), nullable=True)
    contact = db.Column(db.String(250), nullable=True)
    phone = db.Column(db.String(250), nullable=True)
    email = db.Column(db.String(250), nullable=True)

    setup_charge = db.Column(db.String(250), nullable=True)
    deposit = db.Column(db.String(250), nullable=True)
    discount = db.Column(db.String(250), nullable=True)
    total_cost = db.Column(db.String(250), nullable=True)

    order_date = db.Column(db.String(250), nullable=True)
    art_slide_date = db.Column(db.String(250), nullable=True)
    due_date = db.Column(db.String(250), nullable=True)

    apparel_date = db.Column(db.String(250), nullable=True)
    art_film_date = db.Column(db.String(250), nullable=True)
    print_date = db.Column(db.String(250), nullable=True)
    date_delivered = db.Column(db.String(250), nullable=True)

    base_color = db.Column(db.String(250), nullable=True)
    vendor = db.Column(db.String(250), nullable=True)

    x_small_number = db.Column(db.Integer, nullable=True)
    x_small_add_charge = db.Column(db.String(250), nullable=True)
    small_number = db.Column(db.Integer, nullable=True)
    small_add_charge = db.Column(db.String(250), nullable=True)
    medium_number = db.Column(db.Integer, nullable=True)
    medium_add_charge = db.Column(db.String(250), nullable=True)
    large_number = db.Column(db.Integer, nullable=True)
    large_add_charge = db.Column(db.String(250), nullable=True)
    x_large_number = db.Column(db.Integer, nullable=True)
    x_large_add_charge = db.Column(db.String(250), nullable=True)
    xx_large_number = db.Column(db.Integer, nullable=True)
    xx_large_add_charge = db.Column(db.String(250), nullable=True)

    per_unit_base_price = db.Column(db.String(250), nullable=False)
    color_charge = db.Column(db.String(250), nullable=False)
    total_blank_price = db.Column(db.String(250), nullable=False)

    location_size = db.Column(db.String(250), nullable=False)
    num_colors_charge = db.Column(db.String(250), nullable=False)
    color_list = db.Column(db.String(250), nullable=False)
    total = db.Column(db.String(250), nullable=False)

db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/artwork_home')
def artwork_home():
    all_artwork_orders = db.session.query(Artwork_Order).all()
    return render_template('artwork_home.html', all_artwork_orders=all_artwork_orders)

@app.route("/add_artwork_order", methods=["GET", "POST"])
def add_artwork_order():
    if request.method == "POST":
        new_artwork_order = Artwork_Order(
            customer = request.form["customer"],
            contact = request.form["contact"],
            phone = request.form["phone"],
            discount = request.form["discount"],
            total_price = request.form["total_price"],
            order_date = request.form["order_date"],
            date_approved = request.form["date_approved"],
            scheduled_print_date = request.form["scheduled_print_date"],
            apparel_item = request.form["apparel_item"],
            base_color = request.form["base_color"],
            maximum_colors = request.form["maximum_colors"],
            event = request.form["event"],
            theme = request.form["theme"],
        )

        print(new_artwork_order.order_date)

        db.session.add(new_artwork_order)
        db.session.commit()
        return redirect(url_for('artwork_home'))
    return render_template('add_artwork_order.html')

@app.route("/edit_artwork_order", methods=["GET", "POST"])
def edit_artwork_order():
    if request.method == "POST":
        #UPDATE RECORD
        artwork_order_id = request.form["id"]
        artwork_order_to_update = Artwork_Order.query.get(artwork_order_id)
        artwork_order_to_update.customer = request.form["customer"]
        artwork_order_to_update.contact = request.form["contact"]
        artwork_order_to_update.phone = request.form["phone"]
        artwork_order_to_update.discount = request.form["discount"]
        artwork_order_to_update.total_price = request.form["total_price"]
        artwork_order_to_update.order_date = request.form["order_date"]
        artwork_order_to_update.date_approved = request.form["date_approved"]
        artwork_order_to_update.scheduled_print_date = request.form["scheduled_print_date"]
        artwork_order_to_update.apparel_item = request.form["apparel_item"]
        artwork_order_to_update.base_color = request.form["base_color"]
        artwork_order_to_update.maximum_colors = request.form["maximum_colors"]
        artwork_order_to_update.event = request.form["event"]
        artwork_order_to_update.theme = request.form["theme"]

        db.session.commit()
        return redirect(url_for('artwork_home'))
    artwork_order_id = request.args.get('id')
    artwork_order_selected = Artwork_Order.query.get(artwork_order_id)
    return render_template("edit_artwork_order.html", artwork_order=artwork_order_selected)

@app.route("/delete_artwork_order")
def delete_artwork_order():
    artwork_order_id = request.args.get('id')

    # DELETE A RECORD BY ID
    artwork_order_to_delete = Artwork_Order.query.get(artwork_order_id)
    db.session.delete(artwork_order_to_delete)
    db.session.commit()
    return redirect(url_for('artwork_home'))

@app.route('/employee_work_log_home')
def employee_work_log_home():
    all_employee_work_logs = db.session.query(Employee_Work_Log).all()
    return render_template('employee_work_log_home.html', all_employee_work_logs=all_employee_work_logs)

@app.route("/add_employee_work_log", methods=["GET", "POST"])
def add_employee_work_log():
    if request.method == "POST":
        new_employee_work_log = Employee_Work_Log(
            employee = request.form["employee"],
            phone = request.form["phone"],
            full_part_time = request.form["full_part_time"],
            date = request.form["date"],
            start_time = request.form["start_time"],
            project = request.form["project"],
            art_item = request.form["art_item"],
            task = request.form["task"],
            end_time = request.form["end_time"],
        )

        db.session.add(new_employee_work_log)
        db.session.commit()
        return redirect(url_for('employee_work_log_home'))
    return render_template('add_employee_work_log.html')

@app.route("/edit_employee_work_log", methods=["GET", "POST"])
def edit_employee_work_log():
    if request.method == "POST":
        #UPDATE RECORD
        employee_work_log_id = request.form["id"]
        employee_work_log_to_update = Employee_Work_Log.query.get(employee_work_log_id)
        employee_work_log_to_update.employee = request.form["employee"]
        employee_work_log_to_update.phone = request.form["phone"]
        employee_work_log_to_update.full_part_time = request.form["full_part_time"]
        employee_work_log_to_update.date = request.form["date"]
        employee_work_log_to_update.start_time = request.form["start_time"]
        employee_work_log_to_update.project = request.form["project"]
        employee_work_log_to_update.art_item = request.form["art_item"]
        employee_work_log_to_update.task = request.form["task"]
        employee_work_log_to_update.end_time = request.form["end_time"]

        db.session.commit()
        return redirect(url_for('employee_work_log_home'))
    employee_work_log_id = request.args.get('id')
    employee_work_log_selected = Employee_Work_Log.query.get(employee_work_log_id)
    return render_template("edit_employee_work_log.html", employee_work_log=employee_work_log_selected)

@app.route("/delete_employee_work_log")
def delete_employee_work_log():
    employee_work_log_id = request.args.get('id')

    # DELETE A RECORD BY ID
    employee_work_log_to_delete = Employee_Work_Log.query.get(employee_work_log_id)
    db.session.delete(employee_work_log_to_delete)
    db.session.commit()
    return redirect(url_for('employee_work_log_home'))

@app.route('/print_order_home')
def print_order_home():
    all_print_orders = db.session.query(Print_Order).all()
    return render_template('print_order_home.html', all_print_orders=all_print_orders)

@app.route("/add_print_order", methods=["GET", "POST"])
def add_print_order():
    if request.method == "POST":
        new_print_order = Print_Order(
            customer = request.form["customer"],
            contact = request.form["contact"],
            phone = request.form["phone"],
            email = request.form["email"],
            setup_charge = request.form["setup_charge"],
            deposit = request.form["deposit"],
            discount = request.form["discount"],
            total_cost = request.form["total_cost"],
            order_date = request.form["order_date"],
            art_slide_date = request.form["art_slide_date"],
            due_date = request.form["due_date"],
            apparel_date = request.form["apparel_date"],
            art_film_date = request.form["art_film_date"],
            print_date = request.form["print_date"],
            date_delivered = request.form["date_delivered"],
            base_color = request.form["base_color"],
            vendor = request.form["vendor"],

            x_small_number = request.form["x_small_number"],
            x_small_add_charge = request.form["x_small_add_charge"],
            small_number = request.form["small_number"],
            small_add_charge = request.form["small_add_charge"],
            medium_number = request.form["medium_number"],
            medium_add_charge = request.form["medium_add_charge"],
            large_number = request.form["large_number"],
            large_add_charge = request.form["large_add_charge"],
            x_large_number = request.form["x_large_number"],
            x_large_add_charge = request.form["x_large_add_charge"],
            xx_large_number = request.form["xx_large_number"],
            xx_large_add_charge = request.form["xx_large_add_charge"],

            per_unit_base_price = request.form["per_unit_base_price"],
            color_charge = request.form["color_charge"],
            total_blank_price = request.form["total_blank_price"],
            location_size = request.form["location_size"],
            num_colors_charge = request.form["num_colors_charge"],
            color_list = request.form["color_list"],
            total = request.form["total"],
        )

        db.session.add(new_print_order)
        db.session.commit()
        return redirect(url_for('print_order_home'))
    return render_template('add_print_order.html')

@app.route("/edit_print_order", methods=["GET", "POST"])
def edit_print_order():
    if request.method == "POST":
        #UPDATE RECORD
        print_order_id = request.form["id"]
        print_order_to_update = Print_Order.query.get(print_order_id)
        print_order_to_update.customer = request.form["customer"]
        print_order_to_update.contact = request.form["contact"]
        print_order_to_update.phone = request.form["phone"]
        print_order_to_update.email = request.form["email"]
        print_order_to_update.setup_charge = request.form["setup_charge"]
        print_order_to_update.deposit = request.form["deposit"]
        print_order_to_update.discount = request.form["discount"]
        print_order_to_update.total_cost = request.form["total_cost"]
        print_order_to_update.order_date = request.form["order_date"]
        print_order_to_update.art_slide_date = request.form["art_slide_date"]
        print_order_to_update.due_date = request.form["due_date"]
        print_order_to_update.apparel_date = request.form["apparel_date"]
        print_order_to_update.art_film_date = request.form["art_film_date"]
        print_order_to_update.print_date = request.form["print_date"]
        print_order_to_update.date_delivered = request.form["date_delivered"]
        print_order_to_update.base_color = request.form["base_color"]
        print_order_to_update.vendor = request.form["vendor"]

        print_order_to_update.x_small_number = request.form["x_small_number"]
        print_order_to_update.x_small_add_charge = request.form["x_small_add_charge"]
        print_order_to_update.small_number = request.form["small_number"]
        print_order_to_update.small_add_charge = request.form["small_add_charge"]
        print_order_to_update.medium_number = request.form["medium_number"]
        print_order_to_update.medium_add_charge = request.form["medium_add_charge"]
        print_order_to_update.large_number = request.form["large_number"]
        print_order_to_update.large_add_charge = request.form["large_add_charge"]
        print_order_to_update.x_large_number = request.form["x_large_number"]
        print_order_to_update.x_large_add_charge = request.form["x_large_add_charge"]
        print_order_to_update.xx_large_number = request.form["xx_large_number"]
        print_order_to_update.xx_large_add_charge = request.form["xx_large_add_charge"]

        print_order_to_update.per_unit_base_price = request.form["per_unit_base_price"]
        print_order_to_update.color_charge = request.form["color_charge"]
        print_order_to_update.total_blank_price = request.form["total_blank_price"]
        print_order_to_update.location_size = request.form["location_size"]
        print_order_to_update.num_colors_charge = request.form["num_colors_charge"]
        print_order_to_update.color_list = request.form["color_list"]
        print_order_to_update.total = request.form["total"]

        db.session.commit()
        return redirect(url_for('print_order_home'))
    print_order_id = request.args.get('id')
    print_order_selected = Print_Order.query.get(print_order_id)
    return render_template("edit_print_order.html", print_order=print_order_selected)

@app.route("/delete_print_order")
def delete_print_order():
    print_order_id = request.args.get('id')

    # DELETE A RECORD BY ID
    print_order_to_delete = Print_Order.query.get(print_order_id)
    db.session.delete(print_order_to_delete)
    db.session.commit()
    return redirect(url_for('print_order_home'))

if __name__ == "__main__":
    app.run(debug=True)

