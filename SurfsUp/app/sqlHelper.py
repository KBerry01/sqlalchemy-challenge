import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd
import numpy as np

# Seperate out Database logic using a class
class SQLHelper():
    #Database setup
    #Define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///hawaii.sqlite")
        self.base = None
    
        #automap Base classes
        self.init_base()

    def init_base(self):
        # Reflect existing database in new model
        self.base = automap_base()
        # Reflect tables
        self.base.prepare(autoload_with=self.engine)

    # Database queries
    def precipitation(self):
        query = """
                SELECT 
                    PRCP AS PERCIPITATION, 
                    DATE, 
                    STATION
                FROM 
                    MEASUREMENT 
                WHERE 
                    DATE >= '2016-08-23' 
                ORDER BY 
                    DATE ASC
                ;
                    """
        df = pd.read_sql(text(query), con = self.engine)
        data = df.to_dict(orient="records")
        return data
    
    def station(self):
        query = """
                SELECT
                    STATION
                FROM
                    STATION
                ;
                """
        df = pd.read_sql(text(query), con = self.engine)
        data = df.to_dict(orient="records")
        return data
    
    def tobs(self):
        query = """
                SELECT
                    DATE,
                    TOBS AS TEMPERATURE
                FROM
                    MEASUREMENT
                WHERE
                    STATION = 'USC00519281'
                    AND
                    DATE >= '2016-08-23'
                ;
                """
        df = pd.read_sql(text(query), con = self.engine)
        data = df.to_dict(orient="records")
        return data

    def start_end(self, start_date, end_date):
        query = """
                SELECT
                    MIN(tobs) as Min_Temp,
                    MAX(tobs) as Max_Temp,
                    AVG(tobs) as Avg_Temp
                FROM
                    MEASUREMENT
                WHERE
                    date >= '{start_date}'
                    AND
                    date <= '{end_date}'
                ;
                """
        df = pd.read_sql(text(query), con = self.engine)
        data = df.to_dict(orient="records")
        return data