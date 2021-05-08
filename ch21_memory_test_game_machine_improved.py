#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/05/08
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #1. Study string join method to convert list to string with comma-seperated
    #   and get ascii lower and upper case list
    #2. study functools to listening event and get the value from keyboard
    #3. Design GUI for Memory Game
    #4. allow user choose any number alphabet to test (recommendation 5)

import string
from turtle import * # Turtle 모듈 -# Turtle module
from random import randint #난수 관련 모듈-#Random number related module
from time import  sleep #시간 솬련 모듈#Time training module
import functools
import turtle as turtle

#get ascii lower case list
alphabets_lowercase=list(string.ascii_lowercase)
#get ascii upper case list
alphabets_uppercase=list(string.ascii_uppercase)
#convert to 52 alphabets (Upper + lower)
alphabets=alphabets_lowercase+alphabets_uppercase
#save alphabets that player has to memorize
alphabets_memory=[]
#current position alphabet that player has to answer
position_memory=-1
#needToRemoveListen remove listening when finish the GAME
needToRemoveListen=False
#cursor, font size
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

#random_turtle show the random Alphabet that user has to memorize
random_turtle=Turtle()
#turtle_title draw: Welcome title
turtle_title=Turtle()
#alphabets_uppercase_title: draw list of upper class
alphabets_uppercase_title=Turtle()
#alphabets_lowercase_title: draw list of lower class
alphabets_lowercase_title=Turtle()

#this function use to write a string with many parameter
def drawLabel(turleItem, msg, x, y, color, style, align):
    turleItem.reset()
    turleItem.penup()
    turleItem.setposition(x, y)
    turleItem.color(color)
    turleItem.write(msg, move=False, font=style, align=align)
    turleItem.hideturtle()
#this function process to Start Game
#When user click on the Red Circle
#alphabets will be stored in the alphabets_memory
#and show on the random_turtle
def draw_onclick(x, y):
    qno = int(textinput("", "몇 개의 숫자를 기억하시겠습니까?"))
    style = ('tahoma', 50, 'bold')

    alphabets_memory.clear()
    for i in range(qno):
        position = randint(0, len(alphabets) - 1)
        alphabet = alphabets[position]
        alphabets_memory.append(alphabet)
        drawLabel(random_turtle, alphabet, 0, 10, 'blue', style, "left")
        sleep(2)
    style = ('tahoma', 20, 'bold')
    drawLabel(random_turtle, "Please press key to answer!",
              -150, 10, 'red', style, "left")

    #listening event
    for k in alphabets_lowercase:
        turtle.onkeypress(functools.partial(event_handler, k), key=k)
    for k in alphabets_uppercase:
        turtle.onkeypress(functools.partial(event_handler, k), key=k)
    global needToRemoveListen,position_memory
    needToRemoveListen=False
    position_memory=0
    turtle.listen()
#this function use to draw welcome and alphabet
def drawWelcomeAndAlphabet():
    #draw welcome
    style = ('tahoma', 20, 'bold')
    drawLabel(turtle_title, "Welcome to Memory Testing!",
              -150, 250,  'blue', style, "left")
    style = ('tahoma', 12, 'italic')
    #draw upper case alphabets
    s_uppercase=""
    for s in alphabets_uppercase:
        s_uppercase=s_uppercase+s+"   "
    s_uppercase="Uppercase alphabet:"+s_uppercase
    drawLabel(alphabets_uppercase_title, s_uppercase,
              -350, 200, 'blue', style, "left")
    #draw lower case alphabets
    s_lowercase=""
    for s in alphabets_lowercase:
        s_lowercase=s_lowercase+s+"   "
    s_lowercase="Lowercase alphabet:"+s_lowercase
    style = ('tahoma', 12, 'italic')
    drawLabel(alphabets_lowercase_title, s_lowercase, -350, 150, 'blue', style, "left")
#this function use to draw red Circle button
#player will click on this Button to Start the Game
def drawRedCircleButton():
    button = Turtle()
    button.hideturtle()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(0, 100)
    button.write("Click red Circle to Start Game!", align='center', font=FONT)
    button.sety(100 + CURSOR_SIZE + FONT_SIZE)
    button.onclick(draw_onclick)
    button.showturtle()
#this function use to process listening player press the Key on Keyboard
#if all Alphabets is right position->show congratulations
#if any an alphabet is wrong->show Condolatory!
def event_handler(key):
    global needToRemoveListen,position_memory
    if needToRemoveListen == True:
        return
    print(key)
    style = ('tahoma', 20, 'bold')
    drawLabel(random_turtle, key, -150, 10, 'blue', style, "left")
    sleep(0.5)
    if key != alphabets_memory[position_memory]:
        needToRemoveListen=True
        style = ('tahoma', 20, 'bold')
        drawLabel(random_turtle, "Condolatory!\nYou are wrong, the memory list:" +
                  ','.join(alphabets_memory), -150, 10,'red', style, "left")
    position_memory = position_memory+1;
    if position_memory == len(alphabets_memory) and needToRemoveListen ==False:
        style = ('tahoma', 20, 'bold')
        drawLabel(random_turtle, "Congratulations!\nYou answered correctly:"+
                  ','.join(alphabets_memory),-150, 10, 'blue', style, "left")
turtle.setup(900, 600)
turtle.title("Memory Testing!")
drawWelcomeAndAlphabet()
drawRedCircleButton()
turtle.mainloop()