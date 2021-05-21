import random 
import plotly.express as py 
import plotly.figure_factory as ff
import pandas as pd 
from pandas import DataFrame

df = pd.read_csv('data.csv')

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Mobile Brand"],show_hist=False)
fig.show()

