from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://euviacqgmlflof:2364b9b4ccf7d5b38397f69f66e1b640422c36e31816c4f20cd54ce8f1a91642@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d8lt7jnnfdvg1r'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bzfeospvnoyndy:0cefb46f528415a94f99a32fccf3a2285f42d3903c786a8c308b472da637bf7c@ec2-3-229-161-70.compute-1.amazonaws.com:5432/dempo515nlcd7f'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flights-users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

##CONFIGURE TABLES

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    fly_from = db.Column(db.String(50),nullable=False)
    max_price = db.Column(db.Integer, nullable=False)

db.create_all()

class EmailForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    fly_from = StringField("Your city", validators=[DataRequired()])
    max_price = StringField("Maximum price", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/", methods = ["POST", "GET"])
def home():
    form = EmailForm()
    if request.method == "POST":
        new_user = User(
            name = request.form["name"],
            email = request.form['email'],
            fly_from = request.form["fly_from"],
            max_price = int(request.form["max_price"])
        )
        db.session.add(new_user)
        db.session.commit()
        flash("You have been successfully added!")
        return redirect(url_for('home'))
    return render_template("index.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)