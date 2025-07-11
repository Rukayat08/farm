import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score 

#read csv file
#create a dataframe 
st.set_page_config(page_title="Multivariate Analysis", layout="wide")
st.title("Egg Production Record")
df = pd.read_csv("egg_production_system.csv")

#remove columns that has string in a dataframe
df = df.drop('Entity',axis=1)
df = df.drop('Code', axis=1)
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
st.table(summary)

#Univariate Analysis
st.markdown("## Univariate Analysis")
st.markdown("### Organic Free Range Farms")
df = pd.read_csv("egg_production_system.csv")
Organic = df["Number of eggs from hens in organic, free-range farms"].describe()
st.table(Organic)

st.markdown("### Non-Organic Free Range Farms")
df = pd.read_csv("egg_production_system.csv")
n_organic = df["Number of eggs from hens in non-organic, free-range farms"].describe()
st.table(n_organic) 

st.markdown("### Eggs Produced in Barns")
df = pd.read_csv("egg_production_system.csv")
barns = df["Number of eggs from hens in barns"].describe()
st.table(barns) 

st.markdown("### Eggs Produced in Cages")
df = pd.read_csv("egg_production_system.csv")
cage = df["Number of eggs from hens in (enriched) cages"].describe()
st.write(cage) 


st.markdown("### Year of Production")
df = pd.read_csv("egg_production_system.csv")
Year = df["Year"].describe()
st.table(Year)


st.title(" Graph Representation")
st.markdown("## Histogram")
Organic2 = px.histogram(df["Number of eggs from hens in organic, free-range farms"], x = "Number of eggs from hens in organic, free-range farms", title = "Eggs Produced in Organic farms")
st.plotly_chart(Organic2, use_container_width = True)

st.markdown("### Bar Chart")
n_organic = px.bar(df["Number of eggs from hens in non-organic, free-range farms"], y = "Number of eggs from hens in non-organic, free-range farms", title = "Organic farms production")
st.plotly_chart(n_organic, use_container_width = True)

organic = px.bar(df["Number of eggs from hens in organic, free-range farms"], y = "Number of eggs from hens in organic, free-range farms", title = "Non-organic Farms production")
st.plotly_chart(organic, use_container_width = True)

st.markdown("## Line Chart for Eggs Produced in Barns")
barns = px.line(df["Number of eggs from hens in barns"], y = "Number of eggs from hens in barns", title = "Barns production")
st.plotly_chart(barns, use_container_width = True)

st.markdown("## Line Chart for Eggs Produced in Cages")
cages = px.line(df["Number of eggs from hens in (enriched) cages"], y = "Number of eggs from hens in (enriched) cages", title = "Cages production")
st.plotly_chart(cages, use_container_width = True)


st.markdown("## Bivariate Analysis")
st.markdown("## Year vs Organic Farm prodcution")
df2 = pd.DataFrame(df["Year"], df["Number of eggs from hens in organic, free-range farms"])
st.write(df2)


st.markdown("## Year vs Non-organic Farm prodcution")
df3 = pd.DataFrame(df["Year"], df["Number of eggs from hens in non-organic, free-range farms"])
st.write(df3)

st.markdown("## Year vs Barns prodcution")
df3 = pd.DataFrame(df["Year"], df["Number of eggs from hens in barns"])
st.write(df3) 

st.markdown("## Year vs (Enriched) Cage prodcution")
df3 = pd.DataFrame(df["Year"], df["Number of eggs from hens in (enriched) cages"])
st.write(df3)


st.markdown("## Barns vs (Enriched) Cage prodcution")
df3 = pd.DataFrame(df["Number of eggs from hens in barns"], df["Number of eggs from hens in (enriched) cages"])
st.write(df3)  

st.title("Pie Chart Representation")
st.title('Egg Production in Organic farms')
counted = df["Number of eggs from hens in organic, free-range farms"].value_counts().reset_index()
counted.columns = ["Number of eggs from hens in organic, free-range farms", "count"]
organic2 = px.pie(counted, names = "Number of eggs from hens in organic, free-range farms", values = "count", title = "Organic Farm Production")
st.plotly_chart(organic2, use_container_width = True)


st.title('Egg Production in Non-organic farms')
counted = df["Number of eggs from hens in non-organic, free-range farms"].value_counts().reset_index()
counted.columns = ["Number of eggs from hens in non-organic, free-range farms", "count"]
n_organic2 = px.pie(counted, names = "Number of eggs from hens in non-organic, free-range farms", values = "count", title = "Non-organic Farm Production")
st.plotly_chart(n_organic2, use_container_width = True)


st.title('Egg Production in Cage')
counted = df["Number of eggs from hens in (enriched) cages"].value_counts().reset_index()
counted.columns = ["Number of eggs from hens in (enriched) cages", "count"]
cage2 = px.pie(counted, names = "Number of eggs from hens in (enriched) cages", values = "count", title = "Cages Production")
st.plotly_chart(cage2, use_container_width = True)

st.title('Egg Production in Barns')
counted = df["Number of eggs from hens in barns"].value_counts().reset_index()
counted.columns = ["Number of eggs from hens in barns", "count"]
barn2 = px.pie(counted, names = "Number of eggs from hens in barns", values = "count", title = "Barn Production")
st.plotly_chart(barn2, use_container_width = True) 

st.markdown("## Correlation")
numeric_df = df.select_dtypes(include='number')
correlation = numeric_df.corr()
st.write(correlation)

numeric_cols = [
    "Number of eggs from hens in organic, free-range farms",
    "Number of eggs from hens in non-organic, free-range farms",
    "Number of eggs from hens in barns",
    "Number of eggs from hens in (enriched) cages"
]
correlation_matrix = df[numeric_cols].corr() 
 
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Egg Production Systems')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show() 