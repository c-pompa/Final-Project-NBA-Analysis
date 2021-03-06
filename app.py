# import necessary libraries
import os
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import update_data
from collections import namedtuple
from json import JSONEncoder

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# db_all = create_classes(db)
##############################################

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)
# Check db table names
# Base.classes.keys()
data_from_db = Base.classes.top2020Yil5

#################################################

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")



@app.route("/api/predict")
def predict2020YIL5():

    prediction = update_data.top2020_yil_5()
    return jsonify(prediction)


@app.route("/test")
def test():
    return render_template("test.html")





@app.route("/jane")
def jane():
    return render_template("jane.html")



@app.route("/naz")
def naz():
    return render_template("naz.html")



@app.route("/fabiola")
def fabiola():
    return render_template("fabiola.html")










































# NOT USING YET
# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():

    return render_template("")


@app.route("/api/pals")
def pals():

    return jsonify()







if __name__ == "__main__":
    app.run()
