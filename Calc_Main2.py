#Group:
#
#Last_Edit: Sept. 28 1:10 PM by Lorantz 
#
#Calc_Main.py


#Main Program
from Mult import *
from InputParser import *
from Add import *
from Divide import *
#the .pyc files are created because we are importing them into the main
#simply ignore them, dont bother adding them to github.


print('Welcome to Calculator!')

while True:
    while True:
        #parse the users input
        ans = -1
        arr = inputParser()
       	
	print arr 
        
	args=len(arr)
        #testing
	num1=0
	num2=0
	#testing#
        if args==1:
            print ('\n\t'+str(arr[0]))
            break

        if arr=='invalid input': 
            print("\n\t"+arr)
            break

        if args >= 2:
            num1=arr[0]
            op=arr[1]

        if args >= 3:
            num2=arr[2]

        print('\nCalculating...\n')

        #decide op ( + - * / ^ !)
        if op == '*':
            ans=multiply(num1, num2)
        
        elif op == '!':
            ans=fact(int(num1))
        
        elif op == '^':
            ans=power(num1, num2)
            
        elif op == '+':
            ans=add(num1, num2) 

	elif op == '/':
		ans=divide(num1, num2)

        print '\tANSWER: ', ans
