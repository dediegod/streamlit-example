import pandas as pd
import streamlit as st
#import plotly.express as px


url = "https://raw.githubusercontent.com/dediegod/streamlit-example/431b7fd882c39f0adf220651110ec58c910c3bf3/penguins%20lter.csv"
df = pd.read_csv(url, index_col=0)
print(df.head(5))


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

st.set_page_config(
    page_title="Pingüinos Archipiélago Palmer",
    page_icon="🐧",
    layout="wide",
)
st.title('Datos de pingüinos del Archipiélago Palmer (Antártida)')
st.subheader("Autor: Diego de Diego González")
st.header("Introducción")
st.markdown('Los datos fueron recopilados y puestos a disposición por la Dra. Kristen Gorman y la Estación Palmer, Antártida LTER , miembro de la Red de Investigación Ecológica a Largo Plazo.')
#st.markdown("> ")
st.subheader('Primero seleccione qué campos quiere filtrar en la columna de la izquierda, después seleccione qué desea mostrar:')



st.sidebar.title('Filtros')
st.sidebar.write('Puede elegir una o multiples opciones por cada desplegable')


container = st.sidebar.container()

all_specie = container.checkbox("Seleccionar todas las especies")

if all_specie:
    selected_Species = container.multiselect("Selecciona una o más especies de pingüino",
         pd.unique(df["Species"]), pd.unique(df["Species"]))
else:
    selected_Species =  container.multiselect("Selecciona una o más especies de pingüino:",
        options=(pd.unique(df["Species"])))
Species = df['Species'].isin(selected_Species)
df = df[Species]


all_Island = container.checkbox("Seleccionar todas las islas")
if all_Island:
    selected_Island = container.multiselect("Selecciona una o más islas del pingüino:",
         pd.unique(df["Island"]), pd.unique(df["Island"]))
else:
    selected_Island =  container.multiselect("Selecciona una o más islas del pingüino:",
        options=(pd.unique(df["Island"])))
Island = df['Island'].isin(selected_Island)
df = df[Island]


all_Sex = container.checkbox("Seleccionar ambos sexos")
if all_Sex:
    selected_Sex = container.multiselect("Seleccionel sexo del pingüino:",
         pd.unique(df["Sex"]), pd.unique(df["Sex"]))
else:
    selected_Sex =  container.multiselect("Seleccionel sexo del pingüino:",
        options=(pd.unique(df["Sex"])))
Sex = df['Sex'].isin(selected_Sex)
df = df[Sex]


   
mostrar_tabla = st.checkbox('Mostrar tabla de datos')
if mostrar_tabla:
        st.header("Tabla dataset")
        st.dataframe (df)
        
        
mostrar_graficos = st.checkbox('Mostrar gráficas')

if mostrar_graficos:
    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### Body Mass (g)")
        st.write.px.histogram(df, x='Island', y='Flipper Length (mm)', hover_data=['Culmen Length (mm)', 'Culmen Depth (mm)'], color='Sex', barmode='group', height=450)
           
    with fig_col2:
        st.markdown("### Flipper Length (mm)")
        fig2 = px.histogram(df, x="Flipper Length (mm)", color='Sex', barmode='group', height=450)
        st.write(fig2)



