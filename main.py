from fastapi import FastAPI
import requests

app = FastAPI()

id = []
original_titles = []
overview = []
popularity = []
release_date = []
original_titles = []


# GET request #1 to get the longitudes and latitudes of a specific point from google maps
@app.get("/")
async def root():
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=256da2d742d5a5979790e6833447e4b4")
    data = response.json()
    for i in data['results']:
        id.append(i['id'])
        original_titles.append(i['original_title'])
        overview.append(i['overview'])
        popularity.append(i['popularity'])
        release_date.append(i['release_date'])
    movie_description = {
    "id": id,
    "original_titles": original_titles,
    "overview": overview,
    "popularity": popularity,
    "release_date": release_date
    }
    return movie_description


# GET request #2 to get the longitudes and latitudes of a specific point from google maps
@app.get("/titles")
async def show_original_title():
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=256da2d742d5a5979790e6833447e4b4")
    data = response.json()
    for i in data['results']:
        original_titles.append(i['original_title'])
    return original_titles



# GET request #3 to get the longitudes and latitudes of a specific point from google maps
URL = "https://api.bigdatacloud.net/data/reverse-geocode-client"

latitude1 = -1.2994786596965737
longitude2 = 36.79427519625748
PARAMS = {'latitude': latitude1, 'longitude': longitude2}

@app.get("/location")
def get_location():
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

    if data:
        location1 = {
            "continent": data['continent'],
            "countryName": data['countryName'],
            "city": data['city']
        }
        return location1
    else:
        print("error:Location not found")   
  
# GET request # 4 Using query and path parameters on the location api
@app.get("/location/{latitude},{longitude}")
def get_location_by_coordinates(latitude: float, longitude: float):
    r = requests.get(url = URL, params = {'latitude': latitude , 'longitude': longitude})
    data = r.json()

    location2 = {
        "continent": data['continent'],
        "countryName": data['countryName'],
        "city": data['city'],
        "locality": data['locality'],
        "administrative": data['localityInfo']['administrative']
        
    }
    return location2
    
# POST request #2 to get the longitudes and latitudes of a specific point from google maps

