import plotly.plotly as py
import plotly.graph_objs as go
import csv

with open('votebystate.csv', 'r') as f:
	reader = csv.reader(f)
	for x in reader:
		print("state = " + x[0])
		print("Dem Votes = " + x[1])
		print("Repub Votes = " + x[2])

trace1 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[20, 14, 23],
    name='SF Zoo'
)
trace2 = go.Bar(
    x=['giraffes', 'orangutans', 'monkeys'],
    y=[12, 18, 29],
    name='LA Zoo'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='grouped-bar')