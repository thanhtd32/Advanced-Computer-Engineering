#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/05/17
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #Use label instead Entry
    #create a new function labelConfig(string,append=False)
    #   string: text to display
    #   append false if user wants to clear old data and display new text
    #  true if user wants to append the new text
    #create a new function center(window) to set center screen of the desktop
from tkinter import  *
window =Tk()
#Create a calculator
window.title("계산기 만들기")
lformula=Label(window, text='', anchor='w',width=40,bg="black",fg="white",bd=5)
lformula.grid(row=0,column=0,columnspan=5)
buttons=[
    '0', '1', '2', '+', '%',
    '3', '4', '5', '-', '//',
    '6', '7', '8', '*', "**",
    '9', '.', '=', '/', 'C']
row = 1
col =0
#this function use to update text for label
#string: text to display
#append false if user wants to clear old data and display new text
#       true if user wants to append the new text
def labelConfig(string,append=False):
    if append:
        text = lformula.cget("text") + string
        lformula.configure(text=text)
    else:
        lformula.configure(text=string)
for char in buttons:
    def click(key = char):
        if key == '=':
            result=eval(lformula.cget("text"))
            s=str(result)
            labelConfig("=", True)
            labelConfig(s, True)
        elif key =='C':
            #reset text for Label
            labelConfig("",False)
        else:
            #concat string for label
            labelConfig(key, True)
    b=Button(window, text=char, width=7, height=3, command=click)
    b.grid(row=row,column=col)
    col +=1
    if col >4:
        row +=1
        col=0
#this function use to set the screen is center of the desktop
def center(window):
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()
center(window)
window.mainloop()