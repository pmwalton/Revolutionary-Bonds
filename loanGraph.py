#import plotly.plotly as py
#from plotly.graph_objs import *
import datetime
import numpy as np
import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

#opening file
inFile = open("ledgerA.csv" )
df = pd.read_csv(inFile)
#dropping missing data for graph
df = df.dropna(subset = [['crDay', 'crMonth', 'crYear']])
#creating dates
df['crDate'] = df[['crYear', 'crMonth', 'crDay']].astype(int).apply(lambda s : datetime.datetime(*s),axis = 1)

print df['crDollarAmt']
#Making the graph for dollar amounts
trace = Scatter(
    x = df['crDate'],
    y = df['crDollarAmt'],
    mode = 'markers'
)

data = [trace]
fig = Figure(data=data)
plot_url = py.plot(fig, filename = 'loan-test')

#Who are the people with the high numbers? Are they quartermasters? 
