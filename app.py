from flask import Flask ,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy as SQLAlchemyBase
from sqlalchemy.pool import NullPool

from route.airline import Blueprint_Airline
from route.airport import Blueprint_Airport
from route.prices import Blueprint_Price
import json 


app = Flask(__name__)
CORS(app)
app.register_blueprint(Blueprint_Airline)
app.register_blueprint(Blueprint_Airport)
app.register_blueprint(Blueprint_Price)
db_config = open('config.json','r') 
db = json.loads(db_config.read())

DB_URL = "mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8".format(user=db['user'],password=db['password'],host=db['host'],port=3306,database=db['database'])
app.config['SECRET_KEY'] = '1qckllwreinou2ru0'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Pooling 500 Issue
# https://github.com/pallets/flask-sqlalchemy/pull/215
# Override Config , https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy.apply_driver_hacks
class SQLAlchemy(SQLAlchemyBase):
    def apply_driver_hacks(self,app,info,options):
        super(SQLAlchemy,self).apply_driver_hacks(app,info,options)
        options['poolclass'] = NullPool
        options.pop('pool_size',None)


db_Connect = SQLAlchemy(app)
db_Connect.create_all()


@app.route('/api')
def Welcome():
    return 'Hi' 


if __name__ == '__main__':
    app.run(port='6060',host='0.0.0.0',debug=True)


