#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/14
#Description: These codes I type again from Professor's document and translate to English to do
import  random  #난수 를 사용하기 위해 필요합-#Necessary to use random numbers

print("나랑 숫자 맞히기 게임을 해 보자\n")#Let's play a number guessing game with me
print("네 이름은 뭐니?\n")#What's your name
playerName=input()#플레이어 이름 입력-Enter player name
count=1
guessNumber=-1
limit=5 #제한 횟수 5 로 초기화-Reset to limit number of 5
playAgain='YES'#게임 반복 상태 설정-Setting the game repeat state

ansNumber=random.randint(1,30)
print("반가워."+playerName+", 내가 1부터 30사이에 수를 가지고 있어. 맞혀봐\n")
#Nice to meet you, Thanh, I have a number between 1 and 30. Guess it

while playAgain=='YES':
    print(limit,"번만에 맞혀야 돼")#You only have to guess 5 times
    while count<=limit and guessNumber!=ansNumber:
        guessNumber=int(input("추측한 숫가를 입력하세요->"))#Please enter the guessed number
        if guessNumber==ansNumber:
            break#정답을 맞혔으면 안쪽 while 문을 빠져나감-If you get the correct answer, exit the inner while statement.
        elif guessNumber<ansNumber:
            print("추측한 숫자가 컴퓨터가 있는 숫자보다 작아요")  # The guessed number is less than the number with the computer.
        else:
            print("추축한 숫자가 컴퓨터가 가지고 있는 숫자보다 커요")  # The guessed number is greater than the number with the computer.
        count=count+1

    if guessNumber == ansNumber:
        print(count, "번만에 맞혔어요!! 축하해요\n")  # I got it right once!! Congratulations
        if limit > 1:
            limit = limit - 1
    else:
        print("컴퓨터가 가진수는", ansNumber, "야.")  # The number of computers
        limit = limit + 1

    playAgain=input("게임을 다시 할까요?(YES or NO)\n")#Shall we play the game again
    count=1
    guessNumber=-1