from flask import Blueprint, request , make_response
from model.prices_model import Price
from model.prices_model import db
from model.airport_model import Airport
from KayakCrwaler.Collector import Collector

from collections import defaultdict
import datetime
import json

Blueprint_Price = Blueprint('Price_api',__name__,url_prefix='/api/price') 
def InsertCrwaledData(params,target):
    search_data = '{departure}_{arrival}_{datetime}'.format(departure=params['departure'],arrival=params['arrival'],datetime=params['departure-datetime'])
    getLastID = Price.query.count() + 1 
    queries = []
    for values in target.values():
        for value in values:
            queries.append(Price(
                id=getLastID,
                operator= value['operator'],
                flight_number = value['flight_number'],
                departure_airport_iata= value['departure'],
                arrival_airport_iata= value['arrival'],
                currency = value['currency'],
                price = value['price'],
                relativeflights = value['relativeFlights'],
                departure_time= value['departure_date'] + ' ' + value['departure_time'],
                arrival_time = value['arrival_date'] + ' ' + value['arrival_time'],
                bookinglink = value['bookinglink'],
                search_data= search_data
                ))
            getLastID +=1 
    session = db.session()
    session.add_all(queries)
    session.commit()
    session.close()
def sortingRelativeTicket(params,results):
    departure = params['departure']
    arrival = params['arrival']
    flights = defaultdict(list)
    for flight in results.values():
        isFin = False
        iteridx = 0
        nextDeparture = departure
        while isFin != True:
            for flight_ in flight:
                if(flight_[0]['departure']) == nextDeparture:
                    flights[flight_[0]['relativeFlights']].append(flight_[0])
                    nextDeparture = flight_[0]['arrival']
                    if nextDeparture == arrival:
                        isFin=True
                
            iteridx +=1
            if(iteridx >20):
                flights[flight_[0]['relativeFlights']].append(flight_[0])
                break 
    return flights
def bindingRelativeTicket(params,tickets):
        results = defaultdict(list)
        dict_idx = 0
        for price in tickets:
            results[price.relativeflights].append([{
                'operator' : price.operator,
                'flight_number' : price.flight_number,
                'price' : price.flight_number,
                'departure' : price.departure_airport_iata, 
                'departure_date' :str(price.departure_time.date()),
                'departure_time' :str(price.departure_time.time()),
                'arrival' : price.arrival_airport_iata,
                'arrival_date' : str(price.arrival_time.date()),
                'arrival_time' : str(price.arrival_time.time()),
                'price' : price.price,
                'currency' : price.currency,
                'bookinglink' : price.bookinglink,
                'relativeFlights' : price.relativeflights
            }])
                
        dict_idx +=1  
        results = sortingRelativeTicket(params,results)
       
        return results
def bindingRelativeTicketfromCrwaler(params,tickets):
    cashed = []
    results = defaultdict(list)
    tickets = [ticket for ticket in tickets.values()]
    session = db.session()
    for price in tickets:
        results[price['relativeflights']].append([{
            'operator' : price['operator'],
            'flight_number' : price['flightsnumber'],
            'price' : price['price'],
            'departure' : price['departure']['airport'], 
            'departure_date' :price['departure']['date'][0:10],
            'departure_time' :price['departure']['date'][11:],
            'arrival' : price['arrival']['airport'],
            'arrival_date' : price['arrival']['date'][0:10],
            'arrival_time' : price['arrival']['date'][11:],
            'price' : price['price'],
            'currency' : price['currency'],
            'bookinglink' : price['link'],
            'relativeFlights' : price['relativeflights']
        }])
    results = sortingRelativeTicket(params,results)    
    return results

@Blueprint_Price.route('/tickets',methods=['GET'])    
def price():
    # Restful API => URI , HTTP Method , Representaion 
    # Uniform , Stateless, Cacheable, Self-descriptiveness, Client-Server , Hierarchical Structure  
    session = db.session()
    referrer = request.referrer
    if(referrer != 'https://94rising.xyz/flights/'):
        req = request.args
        params = {
            'departure' : req['departure'],
            'arrival' : req['arrival'],
            'departure-datetime' : req['departure-date'].replace('-','_')
        }

        search_data = '{departure}_{arrival}_{datetime}'.format(departure=params['departure'],arrival=params['arrival'],datetime=params['departure-datetime'])
        try:
            querySearchedPrices = session.query(Price).filter_by(search_data=search_data).all()
            session.close()

        except:
            return make_response("Invalid Args",404)

        if(len(querySearchedPrices) > 0):
            results = bindingRelativeTicket(params,querySearchedPrices)
            return results

        else:
            ## Using Crawler
            CrawledResults = Collector(src=params['departure'],dst=params['arrival'],datetime=params['departure-datetime'])
            # Test Codes
            #target = open('./route/ICN-DOM-2020_08_22.json','r')
            if(CrawledResults != 404):
                results = bindingRelativeTicketfromCrwaler(params,CrawledResults)
                
                search_data = params['departure-datetime']
                InsertCrwaledData(params,results)
                return make_response(results,200)
            else:
                msg = {"msg" : "Not Found"}
                return make_response(msg,404)
    else:
        msg = {"msg" : "Invalid referrer"}
        return make_response(msg,403)
