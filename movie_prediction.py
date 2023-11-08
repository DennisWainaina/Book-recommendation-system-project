# Libraries to be used
import numpy
import pandas as pd
import pickle
import streamlit

# Loaded model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Creating function
def movie_recommender(input_data):
    