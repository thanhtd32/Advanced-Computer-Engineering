#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/05/30
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #visualize the ultrafine dust and fine dust data using Pandas' DataFrame object.
    # Also,it so that it can visualize and show the sum of the ultrafine dust and fine dust data.
    # 1. I changed the value of ultrafine dust and fine dust to get full of colors list
    # 2. Write 2 methods mapping Color for ultrafine dust and fine dust
    # 3. Write getSumOfDust function reuse both ultrafine dust and fine dust
    # 4. Write showNotation function for plot
    # 5. Use DataFrame of Pandas object and combine with pyplot to show the chart
import  numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
#This function use to mapping color for pm25
def mappingColorPm25(value):
    if value < 15:
        return 'blue'
    elif 15 <= value < 35:
        return 'green'
    elif 35 <= value< 75:
        return 'orange'
    elif value >= 75:
        return 'red'
#This function use to mapping color for Pm10
def mappingColorPm10(value):
    if value < 30:
        return 'blue'
    elif 30 <= value < 80:
        return 'green'
    elif 80 <= value < 150:
        return 'orange'
    elif value >= 150:
        return 'red'
#this function use to get sum of value for pm25 or pm10
def getSumOfDust(data):
    sum=0
    for x in data:
        sum = sum + x
    return sum
#this function use to show the notation for pm25 or pm10
def showNotation(ax):
    for i in ax.patches:
        ax.text(i.get_x() + 0.1,
                 i.get_height() + .5,
                 i.get_height(),
                 fontsize=8,
                 color='dimgrey')
#set the subplots and some configuration
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5)
fig.set_size_inches(8, 8)

#hour to show the chart
hour=['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h']
#pm25 value
pm25=np.array([34,37,30,14,35,75,43,42,37,35])
#call DataFrame of Pandas object for pm25
dfpm25 = pd.DataFrame({'Ultrafine Dust Data':hour, 'pm25':pm25})
#create color mapping list for pm25
pm25colors = [mappingColorPm25(x) for x in dfpm25["pm25"]]
#get the sum of pm25
sumpm25=getSumOfDust(dfpm25["pm25"])
#draw bar chart
axpm25 = dfpm25.plot.bar(x='Ultrafine Dust Data', y='pm25', rot=0,color=pm25colors,ax=ax1,legend=False)
#set title for pm25 char
axpm25.set_title("PM25-Sum Of Ultrafine Dust Data is "+str(sumpm25))
#show notation for pm25
showNotation(axpm25)

#pm10 value
pm10=np.array([46,29,41,40,81,90,53,52,151,51])
#call DataFrame of Pandas object for pm10
dfpm10 = pd.DataFrame({'Fine Dust Data':hour, 'pm10':pm10})
#create color mapping list for pm10
pm10colors = [mappingColorPm10(x) for x in dfpm10["pm10"]]
#get the sum of pm10
sumpm10=getSumOfDust(dfpm10["pm10"])
#draw bar chart
axpm10 = dfpm10.plot.bar(x='Fine Dust Data', y='pm10', rot=0,color=pm10colors,ax=ax2,legend=False)
#set title for pm10 char
axpm10.set_title("PM10-Sum Of Fine Dust Data is "+str(sumpm10))
#show notation for pm10
showNotation(axpm10)
#Show the chart
plt.show()
