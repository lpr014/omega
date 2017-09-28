#Group:
#
#Last_Edit: Sept. 28 1:10 PM by Lorantz 
#
#Calc_Main.py


#Main Program
from Mult import *
from InputParser import *
from Add import *

print('Welcome to Calculator!')

while True:
    while True:
        #parse the users input
        ans = -1
        arr = inputParser()
        
        args=len(arr)
        
        if args==1:
            print ('\n\t'+str(arr[0]))
            break
        if arr=='invalid input': 
            print("\n\t"+arr)
            break
        if args>=2:
            num1=arr[0]
            op=arr[1]
        if args>=3:
            num2=arr[2]

        print('\nCalculating...\n')

        #decide op ( + - * / ^ !)
        if op == '*':
            ans=multiply(num1, num2)
        
        elif op == '!':
            ans=fact(num1)
        
        elif op == '^':
            ans=power(num1, num2)
            
        elif op== '+':
            ans=add(num1, num2)

        print '\tANSWER: ', ans
    

'''
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
'''
