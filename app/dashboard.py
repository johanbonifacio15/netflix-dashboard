import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

output_dir = 'visualizations'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df = pd.read_csv('app/data/netflix-titles.csv')

# Top 10 directores
directors_count = df['director'].value_counts().head(10)
fig1 = px.bar(
    directors_count,
    x=directors_count.values,
    y=directors_count.index,
    orientation='h',
    labels={'x': 'Cantidad de Títulos', 'y': 'Director'},
    title='Top 10 Directores con Más Títulos en Netflix'
)

# Comparativa series vs peliculas
type_count = df['type'].value_counts()
fig2 = px.pie(
    values=type_count.values,
    names=type_count.index,
    title='Comparativa: Series vs Películas'
)

#  Top 5 clasificaciones
categories = df['listed_in'].str.split(', ').explode().value_counts().head(5)
fig3 = px.bar(
    categories,
    x=categories.values,
    y=categories.index,
    orientation='h',
    labels={'x': 'Cantidad de Títulos', 'y': 'Clasificación'},
    title='Top 5 Clasificaciones con Más Títulos'
)

# creando la app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard de Títulos en Netflix', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3)
])

if __name__ == '__main__':
    app.run_server(debug=True)
