from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Airline(db.Model):
    __tablename__ = 'airline'
    name = db.Column(db.String(255), primary_key=True)
    iata = db.Column(db.String(2))
    icao = db.Column(db.String(3))
    callsign = db.Column(db.String(90))
    country = db.Column(db.String(255))
    logo = db.Column(db.String(255))

    def __init__(self, name, iata, icao,callsign,country,logo):
        self.name = name
        self.iata = iata
        self.icao = icao 
        self.callsign = callsign 
        self.country = country 
        self.logo = logo 

    def __repr__(self):
        return "<%s,%s,%s,%s,%s,%s>" %(self.name, self.iata,self.icao, self.callsign,self.country, self.logo)

