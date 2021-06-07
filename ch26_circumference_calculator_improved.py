#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/06/07
#Description:
    #These codes I improved from Professor's document and translate to English to.
    # It can be seen that the value of pi can be obtained as a probabilistic approximation
    # using the Monte Carlo simulation. Let's write a program that calculates the ratio of
    # the area size of a circle with a circle radius of 1 to a circle with a circle radius
    # of 2 using Monte Carlo simulation probabilistically.
    # 1.use subplot to display 2 graphic of Circle
    # 2.Write isPointInCircle method to check random x,y is inside the circle
    # 3.Write approximateCircleArea method to calculate CircleArea by Monte Carlo sampling
    # 4.Test many case to camparing the Approximate area
import math
import random
import matplotlib.pyplot as plt

#function use to check the random x, y is inside the circle
def isPointInCircle(x, y, Cx, Cy, radius):
    return math.sqrt((x - Cx) ** 2 + (y - Cy) ** 2) <= radius
#function use to calculate area of circle use to sampling mento carlo
#ax: pilot for the circle
#thick: size of point drawing on the chart
#radius: radius for circle
#simCount: Maximum number of simulations
def approximateCircleArea(ax,thick,radius, simCount):
    squareSide = radius * 2
    Cx = radius
    Cy = radius
    pointsInside = 0
    for i in range(simCount):
        x = random.random() * squareSide
        y = random.random() * squareSide
        ax.scatter(x, y, s=thick)
        if (isPointInCircle(x, y, Cx, Cy, radius)):
            pointsInside = pointsInside + 1
    return pointsInside / simCount * squareSide ** 2

plt.figure(figsize=(5,3)) #그림 가로, 세로 크기 설정
#create subplot for Circle with radius =1
ax1=plt.subplot(1,2,1)
ax1.set_xlim([0, 2])
ax1.set_ylim([0, 2])
ax1.set_title("Circle with Radius = 1")
circle_center1=(1,1)
circle_radius1=1
#draw circle 1
c1=plt.Circle(circle_center1,circle_radius1,ec='b',fill=False)

paths1=ax1.add_patch(c1)
ax1.set_aspect('equal')

#create subplot for Circle with radius =2
ax2=plt.subplot(1,2,2)
ax2.set_xlim([0, 4])
ax2.set_ylim([0, 4])
ax2.set_title("Circle with Radius = 2")
circle_center2=(2,2)
circle_radius2=2
#draw circle 2
c2=plt.Circle(circle_center2,circle_radius2,ec='r',fill=False)

paths2=ax2.add_patch(c2)
ax2.set_aspect('equal')

simCount=int(input("Maximum number of simulations?"))
area1=approximateCircleArea(ax1,2,circle_radius1,simCount)
area2=approximateCircleArea(ax2,2,circle_radius2,simCount)
print("Area 1 =",area1)
print("Area 2 =",area2)
ax1.set_title("Area ="+str(area1))
ax2.set_title("Area ="+str(area2))
plt.show()