from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Airport(db.Model):
    __tablename__ = 'airport'
    name = db.Column(db.String(255))
    iata = db.Column(db.String(3))
    icao = db.Column(db.String(4),primary_key=True)
    continent = db.Column(db.String(255)) 
    country = db.Column(db.String(255))
    longitude = db.Column(db.Float())
    latitude = db.Column(db.Float())

    def __init__(self, name, iata, icao,country,continent,latitude,longitude):
        self.name = name
        self.iata = iata
        self.icao = icao 
        self.longitude = longitude 
        self.latitude = latitude 
        self.country = country 
        self.continent = continent
    def __repr__(self):
        return "<%s,%s,%s,%s,%s,%s>" %(self.name, self.iata,self.icao, self.longitude,self.latitude, self.country,self.continent)

