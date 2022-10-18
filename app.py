from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from flight_search import FlightSearch
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = config('APP_CONFIG')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://euviacqgmlflof:2364b9b4ccf7d5b38397f69f66e1b640422c36e31816c4f20cd54ce8f1a91642@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d8lt7jnnfdvg1r'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

db = SQLAlchemy(app)

##CONFIGURE TABLES

class User(db.Model):
    __tablename__ = "flights-users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    max_price = db.Column(db.Integer, nullable=False)
    fly_from = db.Column(db.String(50),nullable=False)

# db.create_all()

class EmailForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    fly_from = StringField("Your city", validators=[DataRequired()])
    max_price = StringField("Maximum price", validators=[DataRequired()])
    submit = SubmitField("Submit")

class FlightsForm(FlaskForm):
    fly_from = StringField("Your city", validators=[DataRequired()])
    max_price = StringField("Maximum price (£)", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods = ["POST", "GET"])
def home():
    form = FlightsForm()
    return render_template("index.html", form = form)

@app.route("/flights", methods = ['POST'])
def flights():
    fly_from = request.form["fly_from"]
    max_price = int(request.form["max_price"])
    flight_search = FlightSearch()
    iata_code = flight_search.get_iata_code(fly_from)
    flight_inspiration = flight_search.flight_inspiration(iata_code,max_price)
    all_flights = []
    for i in range(0,11):
        if flight_inspiration != None and i < len(flight_inspiration):
            one_flight = {}
            one_flight["Destination"] = flight_search.get_city_name(flight_inspiration[i]["Destination"])
            one_flight["Departure Date"] = flight_inspiration[i]["Departure Date"]
            one_flight["Return Date"] = flight_inspiration[i]["Return Date"]
            one_flight["Price"] = flight_inspiration[i]["Price"]
            all_flights.append(one_flight)
        else:
            break

    return render_template("flights.html", origin = fly_from, price = max_price, flights = all_flights)

if __name__ == "__main__":
    app.run(debug=True)
