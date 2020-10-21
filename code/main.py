import functions
import json

url_map = {
    'CarbonFootprint' : 'https://rapidapi.com/carbonandmore-carbonandmore-default/api/carbonfootprint1',
    'USRestaurantMenus' : 'https://rapidapi.com/restaurantmenus/api/us-restaurant-menus',
    'GreatCircleMapper' : 'https://rapidapi.com/marcusgoede/api/great-circle-mapper',
    'FlightData' : 'https://rapidapi.com/Travelpayouts/api/flight-data',
    'Skyscanner Flight Search' : 'https://rapidapi.com/skyscanner/api/skyscanner-flight-search',
    'AirportInfo' : 'https://rapidapi.com/Active-api/api/airport-info',
    'OpenWeatherMap' : 'https://rapidapi.com/community/api/open-weather-map',
    'UsWeatherByZipCode': 'https://rapidapi.com/interzoid/api/us-weather-by-zip-code',
    'ClimaCell' : 'https://rapidapi.com/ClimaCell/api/climacell',
    'CountriesCities' : 'https://rapidapi.com/natkapral/api/countries-cities',
    'UsWeatherByCity' : 'https://rapidapi.com/interzoid/api/us-weather-by-city',
    'WeatherForecast14Days' : 'https://rapidapi.com/weatheronline/api/weather-forecast-14-days',
    'ChickenCoop' : 'https://rapidapi.com/valkiki/api/chicken-coop?endpoint=apiendpoint_550d9371-2ad0-445c-af7c-624c52c9c66f',
    'TrueWayGeocoding' : 'https://rapidapi.com/trueway/api/trueway-geocoding',
    'Asos' : 'https://rapidapi.com/apidojo/api/asos2/',
    'SalesTaxCalculator' : 'https://rapidapi.com/etmdigital/api/sales-tax-calculator/',
    'MovieDatabase' : 'https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative',
    'PublicHoliday' : 'https://rapidapi.com/theapiguy/api/public-holiday',
    'QuestionAnswering' : 'https://rapidapi.com/webknox/api/question-answering/',
    'CoronavirusMap' : 'https://rapidapi.com/Yatko/api/coronavirus-map',
    'SimilarWeb' : 'https://rapidapi.com/apifactory/api/similarweb2',
    'Api-basketball' : 'https://rapidapi.com/api-sports/api/api-basketball',
    'Api-football' : 'https://rapidapi.com/api-sports/api/api-football-beta'
}

apiname = 'ChickenCoop'

api_spec_url = url_map[apiname]

html, data = functions.obtain_html(api_spec_url)

json_data = json.loads(data)

props = json_data['props']
initialReduxState = props['initialReduxState']
api = initialReduxState['api']
cache = api['cache']
api_ed84 = cache[list(cache.keys())[0]]
version = api_ed84['version']
endpoints = version['endpoints']

functions.print_oas(version, endpoints)
functions.write_oas(version, endpoints, apiname)