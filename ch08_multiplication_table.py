#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/21
#Description: These codes I modified from Professor's document and translate to English to do
# -	Check duplication random number for multiplication
# -	Update the limit time about 45 second, if user answered the product is over limit time,
#   program will set wrong answer.
import random #랜덤 모듈을 가져옴-#Import random module
import time#시간 관련 모듈을 가져옴-Import time-related modules

correctAns=0 #맞은 개수 -Right count
wrongAns=0#틀린 개수-Wrong count
duplicateListA=[]#a list to check duplicate random number (for number a
duplicateListB=[]#a list to check duplicate random number (for number b)
limitTime=45#45 second, if user answers over limitTime, the result is refused
count=int(input("몇번할까요?"))#How many times should I do?
while count!=0:
    a=random.randint(3,9) #3단부터 9단까지 숫자 생성-Generate numbers from 3rd to 9th
    b=random.randint(3,9)
    if a==5 or b==5: #5단이면 다시 난수 발생-If it is 5th stage, random number is generated again
        continue
    isDuplicated=False
    for i in range(len(duplicateListA)):#loop to check duplicate random number
        if duplicateListA[i]==a and duplicateListB[i]==b:
            isDuplicated=True
            break
    if isDuplicated == True:#if the multiplication value was already asked
        continue#"Computer duplicated random number, it will random again! "
    else:
        duplicateListA.append(a)
        duplicateListB.append(b)
    count=count-1
    print("%d X %d?" %(a,b))
    startTime=time.time() #반응 시간을 측정-#Measure reaction time
    product=int(input())
    endTime=time.time()
    calculateTime=endTime-startTime#get answered time
    print("%1.f 초만에 답을 했어요"%calculateTime)#I answered in seconds
    if calculateTime>limitTime:
        print("You took long time to answer, limit time is ",limitTime," second you answered in %1.f second"%calculateTime)
    if product==a*b and calculateTime<=limitTime: #곱셈이 맞았는 지 점검-Check if the multiplication is correct
        correctAns=correctAns+1
        print("맞았습니다\n")#Right
    else:
        wrongAns=wrongAns+1
        print("다시 도전해 보세요\n")#Try again

#전체 맞힌 개수를 알려줌-#Shows the total number of hits-%d번중 %d번 맞았어요
print("%d번중 %d번 맞았어요" % (correctAns+wrongAns,correctAns))
