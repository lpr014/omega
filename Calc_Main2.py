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
	    arr = []
	    arr = inputParser()
	    #num1, op, num2 = arr
	    if arr=="invalid input":
			print(arr)
			break
						
	    #needed for fact op.
	    if num2 == '':
		    num2 = '0'
	    '''
	    if not num1.isdigit() or not num2.isdigit():
		    print("\nINVALID INPUT!\n")
		    break
	    '''
	    print('\nCalculating...\n')


	    #decide op ( + - * / ^ !)
	    if op == "*":
		    ans=multiply(int(num1), int(num2))
	    
	    elif op == "!":
	    	ans=fact(int(num1))
	    
	    elif op == "^":
	    	ans=power(int(num1), int(num2))

	    print 'ANSWER: ', ans
	

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
