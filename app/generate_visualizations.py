import os
import pandas as pd
import plotly.express as px

output_dir = 'visualizations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = pd.read_csv('app/data/netflix-titles.csv')

# Visualizacion 1
directors_count = df['director'].value_counts().head(10)
fig1 = px.bar(
    directors_count,
    x=directors_count.values,
    y=directors_count.index,
    orientation='h',
    labels={'x': 'Cantidad de Títulos', 'y': 'Director'},
    title='Top 10 Directores con Más Títulos en Netflix'
)
fig1.write_html('visualizations/directores.html')

# Visualizacion 2
type_count = df['type'].value_counts()
fig2 = px.pie(
    values=type_count.values,
    names=type_count.index,
    title='Comparativa: Series vs Películas'
)
fig2.write_html('visualizations/series_vs_peliculas.html')

# Visualizacion 3
categories = df['listed_in'].str.split(', ').explode().value_counts().head(5)
fig3 = px.bar(
    categories,
    x=categories.values,
    y=categories.index,
    orientation='h',
    labels={'x': 'Cantidad de Títulos', 'y': 'Clasificación'},
    title='Top 5 Clasificaciones con Más Títulos'
)
fig3.write_html('visualizations/clasificaciones.html')
