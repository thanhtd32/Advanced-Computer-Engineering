#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/04/18
#Description:
    #These codes I improved from Professor's document and translate to English to.
    # 1.Create an enum to calculate Ranking for Student
    # 2.Create getRanking method to calculate ranking for Student
    # 3.Create printInfor and printInforWithTitle to print information for Student
    # 4.make a loop with menu to test some test case for Student
    #   4.1.make a new Student
    #   4.2.make a list to store and print all Student that entered
    #   4.3.Find a student
    #   4.4.Exit the application
from enum import Enum
#enum for ranking
#name is A,B,C,D, F level
#value is description for the level
class Ranking(Enum):
     A = "90->100"
     B = "80->89"
     C = "70->79"
     D = "60->69"
     F = "<60"
class Student:#클래스 정의-Class definition
    def __init__(self,name, midScore, finalScore, projectScore):
        self.name=name
        self.midScore=midScore
        self.finalScore=finalScore
        self.projectScore=projectScore

    def get_name(self):
        return self.name

    def get_sum(self):
        return  self.sum
    def get_avg(self):
        return  self.avg

    def calculate(self):
        self.sum=self.midScore+ self.finalScore + self.projectScore
        self.avg=round(self.sum/3)
    def getRanking(self):
        if self.avg >=90:
            self.ranking=Ranking.A
        elif self.avg>=80:
            self.ranking = Ranking.B
        elif self.avg>=70:
            self.ranking=Ranking.C
        elif self.avg>=60:
            self.ranking = Ranking.D
        else:
            self.ranking = Ranking.F
        return self.ranking
    def printInfor(self):#print information only
        print(f'{self.get_name():<15}{self.get_sum():<10}{self.get_avg():<10}'
              f'{self.getRanking().name:<10}{self.getRanking().value:<10}')
    def printInforWithTitle(self):#print information with title
        print(f'{"Name":<15}{"Sum":<10}{"Avg":<10}{"Rank":<10}{"(Note)":<10}')
        self.printInfor()
listOfStudent=[]#list to save student
while True:#loop to test student
    print("1.Enter a new grade Student")
    print("2.Print All grade Student")
    print("3.Find a Student")
    print("4.Exit")
    choose=input("Please choose[1..4]>>")
    if choose=="1":
        name=input("Student Name:")
        #Enter midterm grades
        midScore=int(input("Enter midterm grades:"))
        #Enter final exam grades
        finalScore=int(input("Enter final exam grades:"))
        #Enter assignment grade
        projectScore=int(input("Enter assignment grade:"))

        #객체 생성-Object creation
        stObj=Student(name,midScore,finalScore,projectScore)
        #Sum and average calculation method call
        stObj.calculate() #합과 평균 계산 메소드 호출
        print("Student infor that you entered:")
        stObj.printInforWithTitle()
        listOfStudent.append(stObj)
    elif choose =="2":
        print("List Of Students:")
        print(f'{"Name":<15}{"Sum":<10}{"Avg":<10}{"Rank":<10}{"(Note)":<10}')
        for stObj in listOfStudent:
            stObj.printInfor()
    elif choose =="3":
        name = input("Enter Student Name you want to find:")
        foundObj=None
        for stObj in listOfStudent:
            if stObj.get_name().lower()==name.lower():
                foundObj=stObj
                break
        if foundObj==None:
            print("Can not find student name [%s]",name)
        else:
            foundObj.printInforWithTitle()
    elif choose =="4":
        print("Thank you for your using the app")
        break
