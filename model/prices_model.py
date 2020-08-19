from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Price(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer,primary_key =True)
    operator = db.Column(db.String(255))
    flight_number = db.Column(db.Integer)
    departure_airport_iata = db.Column(db.String(3))
    arrival_airport_iata = db.Column(db.String(3))
    currency = db.Column(db.String(3))
    price = db.Column(db.String(10))
    relativeflights = db.Column(db.Integer)
    departure_time = db.Column(db.Date)    
    arrival_time = db.Column(db.Date)
    bookinglink = db.Column(db.String(255))   
    search_data = db.Column(db.String(255))
    
    def __init__(self, 
    id,
    operator,
    flight_number, 
    departure_airport_iata,
    arrival_airport_iata,
    currency,
    price,
    relativeflights,
    departure_time,
    arrival_time,
    bookinglink,
    search_data):
        self.id=id 
        self.operator =operator
        self.flight_number = flight_number 
        self.departure_airport_iata = departure_airport_iata 
        self.arrival_airport_iata = arrival_airport_iata 
        self.currency = currency
        self.price = price
        self.relativeflights = relativeflights
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.bookinglink = bookinglink 
        self.search_data = search_data 

    def __repr__(self):
        return "<%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s>" %(self.id ,
        self.operator,
        self.flight_number,
        self.departure_airport_iata,
        self.arrival_airport_iata,
        self.currency,
        self.price,
        self.relativeflights,
        self.departure_time,
        self.arrival_time,
        self.bookinglink,
        self.search_data)

