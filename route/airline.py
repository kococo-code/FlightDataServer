from flask import Blueprint, request
from model.airline_model import Airline
import json 

config = open('config.json','r') 
config = json.loads(config.read())

Blueprint_Airline = Blueprint('airline',__name__,url_prefix='/api/airline') 

@Blueprint_Airline.route('/',methods=['GET'])
def Search():
    query_string = str(request.query_string).replace('b','').replace("'",'').split('=')
    target_name = query_string[0]
    target = query_string[1]
    if(query_string[0] == 'iata'):
        results = Airline.query.filter_by(iata=target).all()
    elif(query_string[0] == 'icao'):
        results = Airline.query.filter_by(icao=target).all()
    
    if(len(results)> 0):
        exportResults = {}
        for result in results:
            icao = result.icao
            iata = result.iata 
            name = result.name 
            callsign = result.callsign 
            logo = result.logo
            country = result.country 
            exportResults[icao] = {
                'icao' : icao,
                'iata' : iata,
                'name' : name,
                'callsign' : callsign,
                'country' : country,
                'logo' : logo 
            }

        exportjson = json.dumps(exportResults)
        return exportjson
    else:
        return 'Not Found'    
