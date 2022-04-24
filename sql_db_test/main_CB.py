from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import date

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Cerulean-Bee.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
# class Art_Location_Info(db.Model):
#     art_location_id = db.Column(db.Integer, primary_key=True)
#     art_location = db.Column(db.String(250), nullable=True)
#     description = db.Column(db.String(250), nullable=True)
#     cost = db.Column(db.Float, nullable=False)
#     employee = db.Column(db.String(250), nullable=True)
#     date_complete = db.Column(db.Date, nullable=False)
#     colors = db.Column(db.String(250), nullable=True)
#     def __repr__(self):
#         return "%s"%(self.art_location)

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

    # Art_Location_Info = db.Column(db.ForeignKey("Art_Location_Info.art_location_id"), nullable=True, primary_key=True)

    # art_location_info = Art_Location_Info
    def __repr__(self):
        return "%s, %s, "%(self.id, self.customer)

# class Employee_Work_Log(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     employee = db.Column(db.String(250), nullable=False)
#     phone = db.Column(db.String(250), nullable=False)
#     full_time_part_time = db.Column(db.String(250), nullable=False)
    
db.create_all()


#CREATE RECORD
# new_AO_info = Art_Location_Info(art_location_id=0, art_location="art location", description="description", cost=1.00, employee="employee", date_complete=date(day=4,month=5,year=2022))
new_AO = Artwork_Order(id=1, customer="customer?", contact="contact?", phone="1234567890", discount="discount?", total_price=1.50,
                        order_date=date(day=1,month=2,year=2022), date_approved=date(day=2,month=3,year=2022), scheduled_print_date=date(day=3,month=4,year=2022),
                        apparel_item="shirt", base_color="yellow", maximum_colors=5,
                        event="event", theme="theme",)
                        #art_location_info=new_AO_info)
db.session.add(new_AO)
db.session.commit()