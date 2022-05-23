import pandas as pd
import streamlit as st
#import plotly.express as px  # interactive charts

#df = pd.read_csv(https://github.com/dediegod/streamlit-example/blob/431b7fd882c39f0adf220651110ec58c910c3bf3/penguins%20lter.csv)
#df = pd.read_csv(url, index_col=0)
#print(df.head(5))

url = "https://raw.githubusercontent.com/dediegod/streamlit-example/431b7fd882c39f0adf220651110ec58c910c3bf3/penguins%20lter.csv"
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))


primaryColor="#6eb1ff"
backgroundColor="#f1eded"
secondaryBackgroundColor="#e4e4e4"
textColor="#000b4c"

#print('Cantidad de Filas y columnas:',df.shape)
#print('Nombre columnas:',df.columns)
#df.info()

df["Sex"] = df["Sex"].fillna("Sexo sin identificar")
df["Comments"] = df["Comments"].fillna("")
df["Sex"] = df["Sex"].replace(to_replace = ["."], value ="Sexo sin identificar")
df["Sex"] = df["Sex"].replace(to_replace = ["MALE"], value ="Male")
df["Sex"] = df["Sex"].replace(to_replace = ["FEMALE"], value ="Female")
df["Sex"] = df["Sex"].dropna()
df = df.dropna()
df = df.drop(['Sample Number', 'Region'], axis=1)
