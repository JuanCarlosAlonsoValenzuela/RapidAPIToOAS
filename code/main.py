import functions
import json

url_map = {
    'ChickenCoop' : 'https://rapidapi.com/valkiki/api/chicken-coop?endpoint=apiendpoint_550d9371-2ad0-445c-af7c-624c52c9c66f',
    'Api-basketball' : 'https://rapidapi.com/api-sports/api/api-basketball',
    'Api-football' : 'https://rapidapi.com/api-sports/api/api-football-beta'
}

apiname = 'Api-football'

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