#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/05/17
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #re-design GUI for quiz game
    #1. Add 4 radio button to show sample question (4 question)
    #2. Add more data for problem.txt
    #3. Create a FileFactory class, use to read a text file and return a List string
    #4. Create a Question class, it is a model class for a question
    #   includes attributes: problemContent(string), problemAnser(string), image (string)
    #   isCorrect method to check user correct nor not
    #5. Create a ListQuestion to store list of question from file problem.txt
    #   5.1 read all data from probem.txt and store to a set object
    #   5.2 add isEmpty method to check list question is empty or not
    #   5.3 add getQuestion method to get question object at the current postion
    #   5.4 add sample method to get random and shuffle the question
    #   5.5 add sizeOfList method to return size of the element
    #6. Create a QuizeUI class to design the GUI
    #   all the UI is designed in this class
    #   process show question when user click next question
    #   show the result when user answer the question
    #   add center place for the screen of the desktop
import random
from  tkinter import *
#This class use to text file factory
class FileFactory:
    questionBank="problem.txt"
    encoding="utf8"
    mode="r"
    #this function use to read the content of file
    #return a List String
    def readData(self):
        file = open(self.questionBank, self.mode, encoding=self.encoding)
        datas = file.readlines()
        file.close()
        return  datas
#this class use to build a model of question
#each line in the file, we will build a model for question object
class Question:
    problemContent=None
    problemAnser=None
    image=None
    def __init__(self,problemContent,problemAnser,image):
        self.problemContent=problemContent
        self.problemAnser=problemAnser
        self.image=image
    def isCorrect(self,answer):
        return self.problemAnser==answer
#This class use to store all question model object
#check empty, get sample , getQuestion current postion
class ListQuestion:
    questions=set()
    def __init__(self):
        #constructor read all data in file and store to a set
        datas=FileFactory().readData()
        for item in datas:
            arrDataOfItem =item.strip().split(":")
            if len(arrDataOfItem) == 3:
                question =Question(arrDataOfItem[0],arrDataOfItem[1],arrDataOfItem[2])
                self.questions.add(question)
    #this function check the listquestion is empty or not
    def isEmpty(self):
        return len(self.questions)<=0
    #this function return question at index position
    def getQuestion(self,index):
        if self.isEmpty():
            return None
        if index<0 or index>=len(self.questions):
            return None
        return  list(self.questions)[index]
    #function to get sample 4 question
    #and shuttle the question
    def sample(self,index):
        currentQuestion = self.getQuestion(index)

        currentSet=set()
        currentSet.add(currentQuestion)
        remainList=self.questions-currentSet

        samples=random.sample(remainList,3)
        samples.append(currentQuestion)
        random.shuffle(samples)
        return samples
    #this function return size of the list
    def sizeOfList(self):
        return len(self.questions)
#this class use to design GUI for the Quiz game
#   all the UI is designed in this class
#   process show question when user click next question
#   show the result when user answer the question
#   add center place for the screen of the desktop
class QuizeUI:
    window = None
    qlabel = None
    ilabel = None
    rlabel = None
    radVars =None
    questionBanks = None
    currentPosition=-1
    currentQuestion=None
    #4 radio buttons
    rad1 = None
    rad2 = None
    rad3 = None
    rad4 = None
    def __init__(self):
        self.window = Tk()
        # 질문 레이블
        self.qlabel = Label(self.window, width=100, text="",fg="blue")
        self.qlabel.pack()
        # 이미지 레이블
        self.ilabel = Label(self.window)
        self.ilabel.pack()
        Label(self.window, text="Choose the correct answer and click [Next Question]").pack()
        # 정답/오답 결과 레이블
        # Correct/Incorrect result label
        self.rlabel = Label(self.window,text="")
        self.rlabel.pack()
        frame = Frame(self.window)
        self.radVars = StringVar(frame, "<none>")
        self.rad1 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad1.grid(row=0, column=0)
        self.rad2 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad2.grid(row=0, column=1)
        self.rad3 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad3.grid(row=0, column=2)
        self.rad4 = Radiobutton(frame, text="", value="", variable=self.radVars, command=self.selection)
        self.rad4.grid(row=0, column=3)
        frame.pack()
        # 다음 문제-Next problem
        Button(self.window, text="Next Question",command=self.checkAnswerAndMoveNextQuestion).pack()

        self.questionBanks = ListQuestion()
        if self.questionBanks.isEmpty() == False:
            self.currentPosition = 0
            self.showQuestion()
    #this function use to show the value of radiobutton when user selection
    def selection(self):
        s = "You selected the option [" + str(self.radVars.get())+"]"
        self.rlabel.config(text=s,fg='blue')
    #This function use to show the next question and
    def showQuestion(self):
        self.currentQuestion=self.questionBanks.getQuestion(self.currentPosition)
        self.qlabel.config(text=self.currentQuestion.problemContent)
        img = PhotoImage(file=self.currentQuestion.image).subsample(2, 2)
        self.ilabel.config(image=img)
        self.ilabel.image = img
        randomAnswers= self.questionBanks.sample(self.currentPosition)
        self.rad1.config(text=randomAnswers[0].problemAnser,value=randomAnswers[0].problemAnser)
        self.rad2.config(text=randomAnswers[1].problemAnser,value=randomAnswers[1].problemAnser)
        self.rad3.config(text=randomAnswers[2].problemAnser,value=randomAnswers[2].problemAnser)
        self.rad4.config(text=randomAnswers[3].problemAnser,value=randomAnswers[3].problemAnser)
        self.currentPosition +=1

    # this function use to the  result of the current question
    def checkAnswerAndMoveNextQuestion(self):
        if self.currentQuestion == None:
            return
        if self.currentQuestion.isCorrect(str(self.radVars.get())) == True:
            self.rlabel.config(text="You are right", fg='blue')
        else:
            self.rlabel.config(text="You are wrong!", fg='red')
        if self.currentPosition >= self.questionBanks.sizeOfList():
            self.currentPosition=0
        self.radVars.set("<none>")
        self.showQuestion()
    #this function use to set the screen is center of the desktop
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
    #this function use to show the GUI of the Quiz
    def showUI(self):
        # Take the quiz
        self.window.title("퀴즈 풀기 - Improved")
        self.window.geometry("550x400")
        self.center(self.window)
        self.window.mainloop()
#call showUI() to start the program
QuizeUI().showUI()
