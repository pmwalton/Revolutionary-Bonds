#import plotly.plotly as py
#from plotly.graph_objs import *
import datetime
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

#opening file
inFile = open("RI_Loan_Office.csv" )
df = pd.read_csv(inFile)
df = df.dropna(subset = [['CertDay']])

print df.describe()

df['CertDate'] = df[['CertYear', 'CertMonth', 'CertDay']].astype(int).apply(lambda s : datetime.datetime(*s),axis = 1)
print df.head()


#Making the graph for dollar amounts
data = [
    go.Scatter(
        x = df['CertDate'],
        y = df['90th'] + (0.01 * df['8th']),
        mode = 'markers',
        text = df['First name'] + " " + df['Last name']
    )
]
layout = go.Layout(
    title='Certificate Amounts over Dates for Rhode Island'
)
#data = [trace]
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename = 'loan-test-dos')

