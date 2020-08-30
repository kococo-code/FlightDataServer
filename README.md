# FlightDataServer
## Build with Flask and SQLAlchemy connect to MySQL
- Follow MVC Pattern
- Data Resource from [Kayak.com](https://github.com/kococo-code/FlightDataCrwaler)
## Model 
- Airport
  <table>
    <tr>
      <td>Column</td>
      <td>Data Type</td>
      <td>Options</td>
    </tr>
    <tr>
      <td>name</td>
      <td>String(255)</td>
      <td></td>
    </tr>
    <tr>
      <td>iata</td>
      <td>String(2)</td>
      <td></td>
    </tr>
    <tr>
      <td>icao</td>
      <td>String(3)</td>
      <td>PK</td>
    </tr>
    <tr>
      <td>Continent</td>
      <td>String(255)</td>
      <td></td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Float</td>
      <td></td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>Float)</td>
      <td></td>
    </tr>
  </table>
  
Model => [Airport Model](https://github.com/kococo-code/FlightDataServer/blob/master/model/airport_model.py)

- Airline
  <table>
    <tr>
      <td>Column</td>
      <td>Data Type</td>
      <td>Options</td>
    </tr>
    <tr>
      <td>iata</td>
      <td>String(2)</td>
      <td></td>
    </tr>
    <tr>
      <td>icao</td>
      <td>String(3)</td>
      <td></td>
    </tr>
    <tr>
      <td>Callsign</td>
      <td>String(90)</td>
      <td></td>
    </tr>
    <tr>
      <td>Country</td>
      <td>String(255)</td>
      <td></td>
    </tr>
    <tr>
      <td>logo</td>
      <td>String(255)</td>
      <td></td>
    </tr>
  </table>
Model => [Airline Model](https://github.com/kococo-code/FlightDataServer/blob/master/model/airline_model.py)

- Price

  <table>
      <tr>
        <td>Column</td>
        <td>Data Type</td>
        <td>Options</td>
      </tr>
      <tr>
        <td>id</td>
        <td>Integer</td>
        <td>PK</td>
      </tr>
      <tr>
        <td>operator</td>
        <td>String(255)</td>
        <td></td>
      </tr>
      <tr>
        <td>flight_number</td>
        <td>Integer</td>
        <td></td>
      </tr>
       <tr>
        <td>departure_airport_iata</td>
        <td>String(3)</td>
        <td></td>
      </tr>
      <tr>
        <td>arrival_airport_iata</td>
        <td>String(3)</td>
        <td></td>
      </tr>
      <tr>
        <td>departure_time</td>
        <td>Date</td>
        <td></td>
      </tr>
      <tr>
        <td>arrival_time</td>
        <td>Date</td>
        <td></td>
      </tr>
       <tr>
        <td>currency</td>
        <td>String(3)</td>
        <td></td>
      </tr>
      <tr>
        <td>price</td>
        <td>String(10)</td>
        <td></td>
      </tr>
      <tr>
        <td>relativeflights</td>
        <td>Integer</td>
        <td></td>
      </tr>
      <tr>
        <td>booking_link</td>
        <td>String(255)</td>
        <td></td>
      </tr>
      <tr>
        <td>search_data</td>
        <td>String(255)</td>
        <td></td>
      </tr>
      </tr>

    </table>

Model => [Price Model](https://github.com/kococo-code/FlightDataServer/blob/master/model/prices_model.py)
