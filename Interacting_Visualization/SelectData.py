import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64

app = dash.Dash()

df = pd.read_csv('Data/wheels.csv')

def encode_image(image_file):
    encode = base64.b64encode(open(image_file, 'rb').read())
    return 'Data:image/png;base64,{}'.format(encode.decode())

app.layout = html.Div([
            html.Div(dcc.Graph(id='wheels-plot',
                                figure={'data':[go.Scatter(
                                                x=df['color'],
                                                y=df['wheels'],
                                                dy = 1,
                                                mode='markers',
                                                marker = {'size':15}
                                )],
                                'layout':go.Layout(title='Test', hovermode='closest')}
                                ),style={'width':'30%', 'float':'left'}),
            html.Div([
                html.Pre(id='selection', style={'paddingTop':25})
            ],style={'width':'30%'}),
])

@app.callback(Output('selection', 'children'),
            [Input('wheels-plot', 'selectedData')])
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)

if __name__ == '__main__':
    app.run_server()