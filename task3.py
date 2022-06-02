"""
Created on 2022-06-02
@author: chy
"""

# Run this app with `python task3.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# path of data file
DATA_PATH = "./task2_data.csv"

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

fig = px.bar(data, x="Date", y="Sales", title="Pink Morsel")

# create the header
# header = html.H1(
#     "Pink Morsel Visualizer",
#     id="header"
# )

app.layout = html.Div(children=[
    html.H1(
        "Pink Morsel Visualizer",
        id='header'
    ),

    dcc.Graph(
        id='visualizer',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

# 1. Activate the virtual environment
#  source venv/bin/activate
# 2. run app
# python task3.py
# 3. visit http://127.0.0.1:8050/ in web browser.