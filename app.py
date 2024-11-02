import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    ind=movies[movies['title']==movie].index[0]
    distances=similarity[ind]#distance index
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster for the movie id to fetch poster
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

st.title("Movie Recommender System")
movies_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_list)
selected_movie = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values
)
if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)



