from flask import Blueprint, request , make_response
from model.airport_model import Airport
from model.airport_model import db
import json 
import math
from sqlalchemy import or_
Blueprint_Airport = Blueprint('Airport_api',__name__,url_prefix='/api/airport') 
def getDistance(src_pos,dst_pos):
    R = 6373.0
    lat1 = math.radians(float(src_pos['latitude']))
    lat2 = math.radians(float(dst_pos['latitude']))
    lon1 = math.radians(float(src_pos['longitude']))
    lon2 = math.radians(float(dst_pos['longitude']))
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return math.ceil(distance)

def Parsed_airport_data(results) -> dict:
    exportResults = []
    for result in results:
        icao = result.icao
        iata = result.iata 
        name = result.name 
        country = result.country 
        continent = result.continent
        latitude = result.latitude 
        longitude = result.longitude 
        exportResults.append({
                'icao' : icao,
                'iata' : iata,
                'name' : name,
                'continent' : continent,
                'country' : country,
                'latitude' : latitude,
                'longitude' : longitude  
            })
    return exportResults


@Blueprint_Airport.route('/search',methods=['GET'])
def Search():
    query_string = str(request.query_string).replace('b','').replace("'",'').split('=')
    target_name = query_string[0]
    target = query_string[1]
    result = ''
    if(query_string[0] == 'iata'):
        results = Airport.query.filter_by(iata=target).all()
    elif(query_string[0] == 'icao'):
        results = Airport.query.filter_by(icao=target).all()
    
    if(len(results)> 0):
        exportResults = Parsed_airport_data(results)
        exportjson = json.dumps(exportResults)
        return exportjson
    else:
        return 'Not Found'    

@Blueprint_Airport.route('/flightsairport',methods=['GET'])
def flightsairport():

    # if have transfer need multiple times gatering
    query_string = str(request.query_string).replace('b','').replace("'",'').split('&')
    targets = {} 
    for sub_query in query_string:
        q = sub_query.split('=')
        targets[q[0]] = q[1]

    exportResults = {}
    for key,value in targets.items():
        if key.lower() == 'departure' or key.lower()=='arrival':
            results = Airport.query.filter_by(iata=value).all()
            if(len(results) > 0):
                exportResults[key] = Parsed_airport_data(results) 


    exportjson = json.dumps(exportResults)
    return exportjson

@Blueprint_Airport.route('/airportname',methods=['GET'])
def isValidAirport():
    session = db.session() 
    target = request.args['target']
    if(target[0] == ' '):
        target = target[1:]
    results = session.query(Airport).filter(or_(Airport.iata.like(target+'%'),Airport.name.like(target+'%'))).all()
    session.close()
    if(len(results) > 0):
        data = json.dumps(Parsed_airport_data(results))
        return make_response(data,200)

    msg = {'data' : 'Not Found'}
    return make_response(msg,404)