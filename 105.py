import csv
import pandas as pd
import plotly.express as px
import math

with open('1.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)

#filedata.pop(0)
totalmarks=0
totalentries=len(filedata)
for marks in filedata:
    totalmarks+=float(marks[0])
mean=totalmarks/totalentries
print(mean)

df=pd.read_csv('1.csv')
#fig=px.scatter(df,x='',y='Height(Inches)')
#fig.update_layout(shapes=[dict(
  #  type='line',y0=mean,y1=mean,
   # x0=0,x1=totalentries
#)])
#fig.show()
data=filedata[0]
squaredlist=[]
for number in data:
    a=float(number)-mean
    a=a**2
    squaredlist.append(a)
sum=0
for i in squaredlist:
    sum=sum+i

print(squaredlist)
print(data)
result=sum/(len(data)-1)
stdev=math.sqrt(result)
print(stdev)