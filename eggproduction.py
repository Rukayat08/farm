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
st.markdown("## First Five Observation")
st.write(df.head())

st.markdown("## Last Five Observation")
st.write(df.tail())


st.title("General Information About The Record")
st.markdown('## Preview')
Preview = df.describe()
st.write(Preview)

st.markdown("## OVERVIEW")
summary = df.shape
st.write(summary)

#Univariate Analysis
st.markdown("## Univariate Analysis")
st.markdown("### Organic Free Range Farms")
df = pd.read_csv("egg_production_system.csv")
Organic = df["Number of eggs from hens in organic, free range farms"].describe()
st.table(Organic)


st.markdown("### ")
df = pd.read_csv("egg_production_system.csv")
Non_organic = df["Number of eggs from hens in non-organic, free range farms"].describe()
st.write(df["Non_organic"].describe())

st.markdown("### Year of Production")
df = pd.read_csv("egg_production_system.csv")
Year = df["Year"].describe()
st.write(df["Year"].describe())


organic = px.histogram(df["Number of eggs from hens in organic, free range farms"], x = "BloodPressure", title = "Distribution of Blood Pressure")
st.plotly_chart(organic, use_container_width = True)

organic = px.bar(df["Number of eggs from hens in organic, free range farms"], y = "Number of eggs from hens in organic, free range farms", title = "Organic farms production")
st.plotly_chart(organic, use_container_width = True)

n_organic = px.bar(df["Number of eggs from hens in non-organic, free range farms"], y = "Number of eggs from hens in non-organic, free range farms", title = "Non-organic Farms production")
st.plotly_chart(n_organic, use_container_width = True)

st.markdown("Bivariate Analysis")
st.markdown("## Year vs Organic Farm prodcution")
df2 = pd.DataFrame(df["Year"], df["Number of eggs from hens in organic, free range farms"])
st.write(df2)

st.markdown("Bivariate Analysis")
st.markdown("## Year vs Organic Farm prodcution")
df3 = pd.DataFrame(df["Year"], df["Number of eggs from hens in non-organic, free range farms"])
st.write(df3)


