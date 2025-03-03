import requests
import random


API_KEY = "Your_API_KEY"
BASE_URL = "https://api.themoviedb.org/3"


def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Error fetching genres:", response.text)
        return {}


def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie"
    params = {"api_key": API_KEY, "with_genres": genre_id, "language": "en-US", "page": 1}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        movies = response.json()["results"]
        return movies
    else:
        print("Error fetching movies:", response.text)
        return []


def recommend_movie():
    genres = get_genres()
    
    if not genres:
        print("Could not load genres. Try again later.")
        return

    print("Available genres:", ", ".join(genres.keys()))
    user_genre = input("Enter a movie genre: ").strip().lower()

    if user_genre not in genres:
        print("Invalid genre. Please choose from the list.")
        return

    movies = get_movies_by_genre(genres[user_genre])

    if movies:
        movie = random.choice(movies)
        print("\nRecommended Movie:")
        print(f"Title: {movie['title']}")
        print(f"Overview: {movie['overview']}")
        print(f"Rating: {movie['vote_average']}⭐")
    else:
        print("No movies found for this genre.")


recommend_movie()
