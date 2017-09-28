#Group:
#
#Last_Edit: Sept. 28 1:10 PM by Lorantz
#
#Calc_Main.py


#Main Program
from user import *

print('Welcome to Calculator! \n')

while True:
    cont = True
    while cont == True:
        num1=raw_input('Please enter your first number:').strip()
        if(num1.isdigit()==False): #error case: test if num1 is digit
            print("INVALID INPUT")
            break
    
    
        op=raw_input('Please enter the operation symbol you wish to perform:').strip()
        #error case added by Lorantz
        if(op != '*'and op != '/'and op != '+' and op != '-'):
            print("You must enter a mathematical operation symbol")
            break

        num2=raw_input('Please enter your second number:').strip()
        if(num2.isdigit()==False): #error case: test if num2 is digit
            print("INVALID INPUT")
            break

        print('CALCULATING.... \n')
