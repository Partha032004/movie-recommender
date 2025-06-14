import streamlit as st
import joblib
import requests
import os

def movies_poster(movie_id):
    
    TMDB_API_KEY = os.environ.get("TMDB_API_KEY")
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US')

    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

# takes movie name and returns the 5 recommended movies name
def recommender(movie):
  movie_index=movies[movies['title']==movie].index[0]
  distance=similarity[movie_index]
  movies_list=sorted(list(enumerate(distance)),key=lambda x:x[1],reverse=True)[1:6]
  recommended_movies=[]
  recommended_movies_posters=[]
  for i in movies_list:
    movie_id=movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    #fetch poster from api
    recommended_movies_posters.append(movies_poster(movie_id))
  return recommended_movies,recommended_movies_posters

similarity=joblib.load('models/similarity.pkl')
movies = joblib.load('models/movies.pkl')

st.title('Movie Recommander System')
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button("Recommend"):
    names,posters=recommender(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
