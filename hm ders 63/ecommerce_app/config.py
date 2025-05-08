import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://Nova02\HMSERVER/E_Commerce?driver=ODBC+Driver+17+for+SQL+Server?trusted_connection=yes"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)