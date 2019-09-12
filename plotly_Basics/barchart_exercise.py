import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Data/mocksurvey.csv', index_col=0)

data = [go.Bar(x=df[responce], y=df.index, orientation='h',
        name=responce) for
        responce in df.columns]

layout = go.Layout(title='Survey Results', barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)