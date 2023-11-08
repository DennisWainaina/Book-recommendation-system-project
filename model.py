# Libraries to be used
import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Loaded model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# CSV files
ratings = pd.read_csv('ratings.csv')
books = pd.read_csv('books.csv')
tags = pd.read_csv('tags.csv')
combined_df = books.merge(ratings, on='book_id').merge(tags, left_on='book_id', right_on='tag_id')

# Function to get movie recommendations based on a given movie title
def get_book_recommendations(book_title, model, top_n=5):

    """
    Gives top n book recommendations based on book read.

    Parameters:
    book_title : The title of the book which the user has read.
    model : To be able to fit different models to the function to prevent repeating the function when fine tuning or fitting different models
    top_n : No of recommendations to return default value is 5.

    Returns:
    The top n recommendations based on the input of the user.
    
    """
    # This is to prevent an index error if the movie is not in the dataframe
    try:
        # First we get the Movie_Id for the given movie title
        movie_id = combined_df[combined_df['title'] == book_title]['book_id'].iloc[0]

        # We then get a list of user IDs who have rated the given movie
        users_who_watched = combined_df[combined_df['book_id'] == movie_id]['user_id'].unique()

        # This is a list to store recommendations to give to the user based on what he/she has entered as the movie_title
        recommendations = []

        # Generating recommendations for each user who watched the given movie
        for user_id in users_who_watched:
            
            # Get a list of movie IDs that the user has not rated yet
            unrated_movies = combined_df[(combined_df['user_id'] == user_id) & (combined_df['book_id'] != movie_id)]['book_id'].unique()

            # Predicting ratings for unrated movies
            for unrated_movie_id in unrated_movies:
                predicted_rating = model.predict(user_id, unrated_movie_id).est
                recommendations.append((unrated_movie_id, predicted_rating))

        # Sorting the recommendations by predicted rating in descending order
        recommendations.sort(key=lambda x: x[1], reverse=True)

        # Getting the top N movie recommendations
        top_recommendations = recommendations[:top_n]

        # Printing the top recommendations
        st.write(f"Top {top_n} book recommendations based on '{book_title}':")
        for movie_id, predicted_rating in top_recommendations:
            book_title = combined_df[combined_df['book_id'] == movie_id]['title'].iloc[0]
            st.write(f'Book: {book_title}, Predicted Rating: {predicted_rating}')
    
    # If the movie is not in the dataframe
    except IndexError:
        return "Book not in dataframe"


get_book_recommendations(combined_df['title'].unique()[0], loaded_model)

def main():

    # Title of homepage
    st.title('Book Recommendation System')

    # Getting input data from user
    book = st.text_input('Which book have you read before?')

    # Code for prediction
    movies = ''

    # Button for prediction
    if st.button('Book Recommendations'):
        movies = get_book_recommendations(book, loaded_model)

    # If successfull
    st.success(movies)


if __name__ == '__main__':
    main()

