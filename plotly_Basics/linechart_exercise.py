import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Data/2010YumaAZ.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

print(df.head())
data = [{
    'x': df['LST_TIME'],
    'y': df[df['DAY']==day]['T_HR_AVG'],
    'name': day
} for day in df['DAY'].unique()]

# for day in days:

#     trace = go.Scatter(x=df[df['DAY']==day]['LST_TIME'],
#                         y=df[df['DAY']==day]['T_HR_AVG'],
#                         mode='lines',
#                         name=day)
#     data.append(trace)

layout = go.Layout(title='Daily temp avgs')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)