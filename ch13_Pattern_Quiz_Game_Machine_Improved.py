#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/04/10
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #1.use 2d array dimension to improve program
    #2.give any postion to user guess (use randomn position)
    #eg: [2, 4, 6, ?], [13, ?, 19, 22], [?, 3, 5, 7, 11],...
    #3.use try..exception to catch user problem input
import  random

#pattern 2D array to stored all pattern
patterns=[  [2, 4, 6, 8],[13, 16, 19, 22],
            [2, 3, 5, 7, 11],[1, 1, 2, 3, 5, 8],
            [31, 28, 31, 30]
         ]
#this function use to check matching value between pattern and guessing value
#it will return True (right) or False (wrong)
def patternmatch(pattern):
    #variable to store right or wrong guessing number
    correctAns=False
    #get the len of pattern (1D array)
    lenOfPattern = len(pattern)
    #random a postion
    guessPosition = random.randint(0, lenOfPattern-1)
    #user has to guess value at this position
    valueAtQuestionMark = pattern[guessPosition]
    for i in range(lenOfPattern):
        if i == guessPosition:
            print("?", end=" ")#print ? mark, user must guess this number
        else:
            print(pattern[i],end=" ")
    while True:#user must enter valid value
        try:#use try except
            guessAns = int(input("What is the value at ? position:"))
            break
        except ValueError:
            print("Value input is not valid! please enter an integer number")
    if guessAns == valueAtQuestionMark:
        correctAns = True
        print("Well done! Congratulations")
    else:
        correctAns = False
        print("You are wrong, the correct answer is %d " %valueAtQuestionMark)
    return correctAns
#this function pass the 2D pattern array
#it will iterate all data in 2D to ask user give guessing number
def playQuiz(patterns):
    # variable to count correct or wrong guessing number
    correctAns = 0
    wrongAns = 0
    lenOfPattern=len(patterns)
    for i in range(lenOfPattern):
        #get an 1D array pattern to resuse the patternmatch function above
        pattern=patterns[i]
        result= patternmatch(pattern)
        if result == True:
            correctAns = correctAns + 1
        else:
            wrongAns = wrongAns + 1
    print("%d patterns, correct %d, wrong %d."%(lenOfPattern,correctAns,wrongAns))
#this function will use while loop to ask user re-play Quiz Game:
def playQuizLoop():
    while True:
        print("Welcome to Quiz Game!")
        playQuiz(patterns)
        confirm=input("Do you want to re-play Quiz Game?[y,n]:")
        if confirm == 'n' or confirm == 'N':
            break
    print("Thank you so much for your playing the Quiz Game!")

#call playQuizLoop functioin:
playQuizLoop()