from fastapi import FastAPI
import requests

app = FastAPI()

id = []
original_titles = []
overview = []
popularity = []
release_date = []
original_titles = []

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


@app.get("/titles")
async def show_original_title():
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=256da2d742d5a5979790e6833447e4b4")
    data = response.json()
    for i in data['results']:
        original_titles.append(i['original_title'])
    return original_titles


# Get request #2 to get the longitudes and latitudes of a specific point from google maps


