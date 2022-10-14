# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output, State, dash_table, ctx
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime, date, timedelta
from tools import modify_twitter_json, modify_telegram_json
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

JSON_FILE = 'config_nb.json'
SOCIAL_MEDIA_LIST = ["Twitter", "Telegram"]
TWITTER_SEARCH_LIST = ["Topic", "User", "Raw"]
DEFAULT_KEYWORD_SEARCH = ["SS-26",
    "bmp",
    "S-400",
    "SS-N-30",
    "TOS-1A",
    "kh-101",
    "kh-102",
    "SA-17",
    "SA-27",
    "SS-NX-33",
    "Shahed-136",
    "Shahed-236",
    "Geran-2",
    "Zoopark",
    "rocket",
    "ukraine",
    "elon"]

app.layout = html.Div([
    dcc.RadioItems(
        list(SOCIAL_MEDIA_LIST),
        value='Twitter',
        id='social-media-list'
    ),
    html.Div(id='telegram-search',
        children=[
            html.Hr(),
            html.Label("Enter channel to search:  "),
            dcc.Input(id='telegram-search-text', type='text', value=''),
            html.Div(id='telegram-search-results'),],
        style={'display':'none'}),
    html.Div(id='twitter-search',
        children=[
            html.Hr(),
            html.Label("Select type of Twitter Search:  "),
            dcc.RadioItems(list(TWITTER_SEARCH_LIST), value='Topic', id='twitter-search-list'),
            html.Hr(),
            html.Label("Enter number of tweets to return:  "),
            dcc.Input(id='twitter-num-input', type='number', value=''),
            html.Hr(),
            html.Label("Enter search text:  "),
            dcc.Input(id='twitter-search-text', type='text'),
            html.Label(children="Select the specific dates you would like to search: "),
            dcc.DatePickerRange(
                id='calendar-button-dates',
                start_date=(datetime.now() - timedelta(days=1)),
                clearable=True,
                with_portal=True,
                end_date=datetime.now(),
            ),
            html.Div(id='twitter-search-results'),
        ],
        style={'display':'none'}),
    html.Button("RUN SEARCH", id="run-search", style={"margin": "15px"}, n_clicks=0),
    # html.Div(id='twitter-search-results'),
    # dash_table.DataTable(id='search-results'),
])


# DISPLAY TELEGRAM DIALOG
@app.callback(
    Output('telegram-search', 'style'),
    Input('social-media-list', 'value')
)
def build_telegram(social_media):
    if social_media == "Telegram":
        return {'display':'block'}
    else:
        return {'display':'none'}


# DISPLAY TWITTER DIALOG
@app.callback(
    Output('twitter-search', 'style'),
    Input('social-media-list', 'value')
)
def build_twitter(social_media):
    if social_media == "Twitter":
        return {'display':'block'}
    else:
        return {'display':'none'}


# MODIFY TWITTER JSON
@app.callback(
    Output('twitter-search-results','children'),
    Input('social-media-list', 'value'),
    Input('twitter-search-list', 'value'),
    Input('twitter-num-input', 'value'),
    Input('twitter-search-text', 'value'),
    Input('calendar-button-dates', 'start_date'),
    Input('calendar-button-dates', 'end_date'),
    Input('run-search', 'n_clicks'), prevent_initial_call=True
)
def twitter_feedback(social_media, search_list, num_tweets, search_text, start_date, end_date, run_search):
    if social_media == "Twitter":
        if "run-search" == ctx.triggered_id:
            search_type = search_list
            start_date = start_date
            end_date = end_date
            search = search_text
            n_tweets = num_tweets
            kwList = DEFAULT_KEYWORD_SEARCH
            modify_twitter_json(JSON_FILE, values=[search_type, start_date, end_date, search, n_tweets, kwList])
            return "All Done!"


# MODIFY TELEGRAM JSON
@app.callback(
    Output('telegram-search-results','children'),
    Input('social-media-list', 'value'),
    Input('telegram-search-text', 'value'),
    Input('run-search', 'n_clicks'), prevent_initial_call=True
)
def telegram_feedback(social_media, search_text, run_search):
    if social_media == "Telegram":
        if "run-search" == ctx.triggered_id:
            search = search_text
            kwList = DEFAULT_KEYWORD_SEARCH
            modify_telegram_json(JSON_FILE, values=[search, kwList])
            return "All Done!"


if __name__ == '__main__':
    app.run_server(debug=True)