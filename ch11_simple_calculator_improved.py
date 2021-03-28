#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/03/28
#Description:
# These codes I improved from Professor's document and translate to English to
# to support calculation instructions with two or more operands, exponential '^'
value=0
while True:
    print("\n현재 값:",value)#Current value
    line=input("작업 명령 입력:")#Enter the work command:
    tokens=line.split()
    if len(tokens)>0:
        operator=tokens[0]
        if len(tokens) ==1:
            if operator =='x':
                break
            print("잘못된 작업 명령!!")#Wrong work order!!
        else:
            listOperand=[]#a list to store all operands
            isAllOperandValid=True
            for i in range(1,len(tokens)):#loop to store all operands into listOperand
                if tokens[i].isdigit() == False:
                    isAllOperandValid=False
                    break
                operand = float(tokens[i])
                listOperand.append(operand)
            if isAllOperandValid == True:
                if operator== '=':
                    value=listOperand[len(listOperand)-1]#get the last operand to asign for value
                elif operator=='+':
                    for operand in listOperand:#loop and plus all operand into value variable
                        value+=operand;
                elif operator=='-':
                    for operand in listOperand:#loop and minus all operand into value variable
                        value-=operand;
                elif operator=='*':
                    for operand in listOperand:#loop and multiply all operand into value variable
                        value*= operand;
                elif operator=='^':#loop and exponential all operand into value variable
                    for operand in listOperand:
                        value=pow(value,operand)
                elif operator=='/' or operator=='%':
                    checkDividedZore=False
                    for operand in listOperand:  # loop to check diveded by zero
                        if operand==0:
                            checkDividedZore=True
                            break
                    if checkDividedZore==False:
                        if operator=='/':
                            for operand in listOperand:#loop and devide all operand into value variable
                                value /= operand;
                        else:
                            for operand in listOperand:#loop and mod all operand into value variable
                                value %= operand;
                    else:#Illegal operation command (divided by zero)!!)
                        print("잘못된 작업 명령(0으로 나누기)!!)")
                else:
                    print("Operator is not exist![=,+,-,*,/,%,^]")
            else:
                print("Some operand is not valid!")
    else:
        print("Invalid string input format")
