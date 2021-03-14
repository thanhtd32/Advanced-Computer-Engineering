#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/14
blist=['아메리카노','카페라테','카푸치노','오렌지주스','콜라    ','자몽주스']
plist=[2500,3000,3000,4000,1500,4000]
blistUserChoose=[]#the index of food name that user selected
plistUserChoose=[]#the quantity of food name that user selected
#print the menu for food/drink
print("No.","Food Name\tPrice")
for i in range(len(blist)):
    print(i+1,'.',blist[i],'\t',plist[i])
print("주문할 음료 를 알씀하세요.")#Please tell me the drink you ordered.
while True:#the loop for choosing menu food/drink from menu
    noFoodName=0
    while noFoodName<=0 or noFoodName > len(blist):#User has to choose from 1->n
        strnoFoodName=input("Please choose the food name(enter number)[{}-{}]:".format(1,len(blist)))
        if strnoFoodName.isdigit():#If the value is a digit, we convert to int
            noFoodName=int(strnoFoodName)
        else:
            noFoodName=0#reset 0 if the user input
    blistUserChoose.append(noFoodName)
    noQuantity=0
    while noQuantity<=0:#quantity must >0
        strnoQuantity = input("Please enter quantity[>0]:")
        if strnoQuantity.isdigit():
            noQuantity=int(strnoQuantity)
        else:
            noQuantity=0
    plistUserChoose.append(noQuantity)
    question=input("Do you want to choose another food?(yes/no):")#confirm continue or not
    if question=='no':#if no, finish choosing the food/drink
        break
print("The list of ordered food/drink:")
sum = 0
print("Food Name\tPrice\tQuantity\tMoney")
for i in range(len(blistUserChoose)):#the loop to print all food/drink that user has chosen
    foodName=blist[blistUserChoose[i]-1]#get the food name from user's choosing
    quantity=plistUserChoose[i]#get quantity that user bought
    unitPrice=plist[blistUserChoose[i]-1]#get the unit price for food/drink
    money=quantity*unitPrice#calculate money for each food/drink
    sum=sum+money#sum every food/drink
    print(foodName,"\t",unitPrice,"\t",quantity,"\t\t\t",money)#print detail information for each item
print("\t\t\t\t\t총 금액은:\t",sum,"원")#The total amount is:
money=0
while True:#loop for user to pay money
    strmoney=input("지불하실 금액을 입력하세요.>>")#Enter the amount to be paid >>
    if strmoney.isdigit()==False:
        print(strmoney," is not valid, it should be a digit numer ")
    else:
        money=int(strmoney)
        if money<0:
            print(strmoney, " is not valid number, it should be positive")
        else:
            if money < sum:
                print("금액이 부족합니다., you have to pay ",sum,"원")  # Not enough money
            else:
                print("Paid is successfully!")
                if money>sum:
                    print("거스름돈은", money - sum, "원 입니다")  # Change is
                break
print("Thank you so much! see you again!")

