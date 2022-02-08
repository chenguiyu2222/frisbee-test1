# -*- coding: cp936 -*-
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd

token = 'pk.eyJ1IjoiZ2FyeTE5OTciLCJhIjoiY2t3dDc1ZGVyMWJibzJ4cnVkczZ3eXI4NiJ9.mXgtn0LyD63wkGMBijyqZg'

px.set_mapbox_access_token(token)
df = pd.read_csv('frisbee_city_84.csv')
df['text'] = df['Sheet1__Name'] + '<br>' + df['Sheet1__Contact']
print(df.columns)
fig = px.scatter_mapbox(df, text = 'text',lat="lat84", lon="lon84",  size_max=30, zoom=3,height=900)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div(
    dbc.Container(
        [
            html.H1('国内飞盘队伍组织分布图'),
            dcc.Graph(figure=fig)
        ]
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
