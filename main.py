from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sql_return

app = Flask(__name__)
SQL = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    __tablename__ = 'cafe'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean(), nullable=False)
    has_toilet = db.Column(db.Boolean(), nullable=False)
    has_wifi = db.Column(db.Boolean(), nullable=False)
    can_take_calls = db.Column(db.Boolean(), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


@app.route('/')
def home():
    locations = sql_return.SQLReturn().all_locations()
    return render_template("index.html", locations=locations)


if __name__ == '__main__':
    app.run(debug=True)
