# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper



#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all avaliable api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/Precipitation<br/>"
        f"/api/Station<br/>"
        f"/api/Tobs<br/>"
        f"/api/Start_End/2012-05-30/2017-05-30<br/>"
    )

# Link SQLHelper queries to route
@app.route("/api/Precipitation")
def Precipitation():
    data = sql.precipitation()
    return(jsonify(data))

@app.route("/api/Station")
def Station():
    data = sql.station()
    return(jsonify(data))

@app.route("/api/Tobs")
def Tobs():
    data = sql.tobs()
    return(jsonify(data))

@app.route("/api/Start_End/<start_date>/<end_date>")
def Start_End(start_date, end_date):
    data = sql.start_end(start_date, end_date)
    return(jsonify(data))

# Run app
if __name__ == '__main__':
    app.run(debug=True)