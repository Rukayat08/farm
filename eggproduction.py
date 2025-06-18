import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as pt 
import numpy as np 
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score 

#read csv file
#create a dataframe 

st.title("Egg Production Record")
df = pd.read_csv("egg_production_system.csv")
st.markdown("# First Five Observation")
st.write(df.head())

st.markdown("# Last Five Observation")
st.write(df.tail())
