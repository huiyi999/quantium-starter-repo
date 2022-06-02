"""
Created on 2022-06-02
@author: chy
"""

from dash.testing.application_runners import import_app
from task4 import app


def test_header_present(dash_duo):
    # fire up a selenium instance which will load your dash app in a browser session
    dash_duo.start_server(app)
    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element_by_id("graph", timeout=10)


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=10)
