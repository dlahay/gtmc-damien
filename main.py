from dash import Dash, dcc, Output, Input # pip install dash
import dash_bootstrap_components as dbc   # pip install dash-bootstrap-components
import plotly.express as px
import pandas as pd                        # pip install pandas
from datetime import datetime
import numpy as np

# incorporate data into app
# Source - https://www.cdc.gov/nchs/pressroom/stats_of_the_states.htm
# df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Good_to_Know/Dash2.0/social_capital.csv")

# Jour,Distance,Denivele,Duree,VMoy,VMax,DistMoy,DeniveleMoy,DureeMoy,VMoyCumul,DCumul,DeniveleCuml,DureeCmul,DiffDistance,DiffDev,DiffCumulDist,DiffCumulDev
columns = ['Jour','Distance','Denivele','Duree','VMoy','VMax','DistMoy','DeniveleMoy','DureeMoy'] 
dtypes = {'Jour':'float','Distance':'float','Denivele':'float','Duree':'float','VMoy':'float','VMax':'float','DistMoy':'float','DeniveleMoy':'float','DureeMoy':'float'}
parse_dates = ['Duree', 'DureeMoy']
df = pd.read_csv("2022_GTMC_Damien_Statistiques.csv", usecols=columns, dtype=dtypes, parse_dates=parse_dates)
print(df.head())


# Define the graphs
fig_denivele_vmoy = px.scatter(df, x='Denivele', y='VMoy', color='Jour', hover_name='Jour', size='Distance')
fig_denivele_dist = px.scatter(df, x='Denivele', y='Distance', color='Jour', hover_name='Jour')
fig_dist_vmoy = px.scatter(df, x='Distance', y='VMoy', color='Jour', hover_name='Jour', size='Denivele')
fig_distance = px.bar(data_frame=df, x="Jour", y='Distance', orientation='v')
fig_denivele = px.bar(data_frame=df, x="Jour", y='Denivele', orientation='v')
fig_duree = px.bar(data_frame=df, x="Jour", y='Duree', orientation='v')

# Build your components
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
mytitle = dcc.Markdown(children='Statistiques Damien GTMC')
mygraph = dcc.Graph(figure={})
graph_denivele_vmoy = dcc.Graph(figure=fig_denivele_vmoy)
graph_denivele_dist = dcc.Graph(figure=fig_denivele_dist)
graph_dist_vmoy = dcc.Graph(figure=fig_dist_vmoy)
graph_dist = dcc.Graph(figure=fig_distance)
graph_denivele = dcc.Graph(figure=fig_denivele)
graph_duree = dcc.Graph(figure=fig_duree)



# ajouter les graphes souhaités
dropdown = dcc.Dropdown(options=df.columns.values[1:],
                        value='Distance',  # initial value displayed when page first loads
                        clearable=False)

# Customize your own Layout
# ajouter les widgets sur le layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=6)
    ], justify='center'),
    dbc.Row([
        dbc.Col([graph_dist_vmoy], width=4),
        dbc.Col([graph_denivele_vmoy], width=4),
        dbc.Col([graph_denivele_dist], width=4)
    ]),
    dbc.Row([
        dbc.Col([graph_dist], width=4),
        dbc.Col([graph_denivele], width=4),
        dbc.Col([graph_duree], width=4)
    ]),
    dbc.Row([
        dbc.Col([mygraph], width=4),
    ]),
    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify='center'),

], fluid=True)

# Pas d'interaction
# Callback allows components to interact
@app.callback(
    Output(mygraph, component_property='figure'),
    Output(mytitle, component_property='title'),
    Input(dropdown, component_property='value')
)
def update_graph(column_name):  # function arguments come from the component property of the Input
    print(column_name)
    print(type(column_name))
    fig = px.bar(data_frame=df, x="Jour", y=column_name, orientation='v')
    return fig, "# "+column_name 


# Run app
if __name__=='__main__':
    app.run_server(port=8051)
