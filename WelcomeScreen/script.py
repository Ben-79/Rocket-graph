import plotly.express as px
import pandas as pd
sheetInput=input("Enter the file name: ")
yInput=input("Enter Y axis: ")
sheet=pd.read_excel(sheetInput)
#Find time=0
start= sheet['T7_time'].loc[sheet.index[0]]
#Subtract all subsequent times by the first and divide to get time in seconds
test= (sheet['T7_time']-start) / 1000000000
fig = px.scatter(sheet, test, yInput,trendline='lowess', template='plotly_dark')
fig.update_traces(mode='lines')
fig.data[-1].line.color='red'
fig.show()