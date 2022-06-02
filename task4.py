"""
Created on 2022-06-02
@author: chy
"""

# Run this app with `python task3.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# path of data file
DATA_PATH = "./task2_data.csv"

colors = {
    'plot': '#E7A6FF',
    'paper': '#111111',
    'text': '#5DA0BA'
}


# read data
data = pd.read_csv(DATA_PATH)
data = data.sort_values(by="Date")

app = Dash(__name__)


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# create the data graph
def generate_figure(chart_data):
    fig = px.bar(chart_data, x="Date", y="Sales", title="Pink Morsel")
    fig.update_layout(
        plot_bgcolor=colors['plot'],
        paper_bgcolor=colors['paper'],
        font_color=colors['text']
    )
    return fig


# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        'textAlign': 'center',
        'color': colors['text']
    }
)

# create the Graph
graph = dcc.Graph(
    id='graph',
    figure=generate_figure(data)
)

# create dcc.RadioItems components
radio = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    'all',
    id='region',
    inline=True,
    style= {'color': colors['text']}
)
radio_wapper = html.Div(
    [
        radio
    ],
    style={'width': '48%',
           'display': 'inline-block',
           'font-size': '150%'
           }
)

app.layout = html.Div(children=[
    header,
    radio_wapper,
    graph
],
    style={
        "textAlign": "center",
        "background-color": colors["paper"],
        "border-radius": "10px"
    })


@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value'))
def update_graph(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["Region"] == region]

    figure = generate_figure(filtered_data)
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)

# 1. Activate the virtual environment
#  source venv/bin/activate
# 2. run app
# python task4.py
# 3. visit http://127.0.0.1:8050/ in web browser.
