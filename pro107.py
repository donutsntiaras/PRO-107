import pandas as pd
import csv
import plotly.graph_objects as ps
inp = input("Enter student id")
dataFrame=pd.read_csv('data.csv')
df1 = dataFrame.loc[dataFrame['student_id']==inp]
print(df1.groupby('level')['attempt'].mean())
fg = ps.Figure(ps.Scatter(x =df1.groupby('level')['attempt'].mean(),
              y=['Level 1','Level 2','Level 3','Level 4'],mode='markers',marker_size=[120,100,85,60], marker_color=['red','blue','green','yellow']))
fg.show()