import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up the database engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)
#references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link
session = Session(engine)

app = Flask(__name__)

@app.route('/')
def welcome():
    return (
            '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year.dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >=prev_year).all()
    return 