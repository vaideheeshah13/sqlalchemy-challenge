
# Import dependencies
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from flask import Flask, jsonify

# Set up Flask
app = Flask(__name__)

# create engine to hawaii.sqlite
engine = create_engine("sqlite:////Users/Vaidehee/Desktop/10-Advanced-Data-Storage-and-Retrieval/Instructions/Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

query_results = session.query(Measurement.date,Measurement.prcp).\
    filter(Measurement.date > '2016-08-23').all()


#return JSON representation of your dictionary
precip_dic ={}
for i in query_results:
    precip_dic[(i.date)]=i.prcp

    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    
    stations = session.query(Station.station).all()
    
    
#return JSON list of stations from dataset
stationlist = list(np.ravel(results))

return jsonify(stationlist)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs = session.query(Measurement.date, Measurement.tobs)\
            .filter(Measurement.date >= '2016-08-23')\
            .order_by(Measurement.date).all()

return jsonify(tobs)

@app.route("/api/v1.0/<start>")
@app.route("/apiv1.0/<start>/<end>")
#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

#When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


#define main behavior
if __name__ == "__main__":
    app.run(debug=True)

