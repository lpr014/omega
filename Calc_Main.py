#Group:
#
#Last_Edit: Sept. 28 1:10 PM by Lorantz 
#
#Calc_Main.py


#Main Program
import os
from Mult import *
from InputParser import *
from Add import *
from Divide import *
from SquareRoot import *
from Subtract import *
#the .pyc files are created because we are importing them into the main
#simply ignore them, dont bother adding them to github.


print('Welcome to Calculator!')
#History.txt code here
if os.path.exists('.history'):
    history=open('.history','r+')
else:
    history=open('.history','w')
    history.close()
    history=open('.history','r+')


while True:
    while True:
        #parse the users input
        ans = -1
        arr = inputParser()


        #Testing
        '''        
        if arr=='history':
            his=open('.history')
            lines=his.readlines()
            his.close()
            lines
            for i in range(0, len(lines)):
                print lines[i]
            break
        '''
        #Testing
        
               	
	    #print arr 
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
	    if arr[0] == 'sqrt(': #test for sqrt
	    	op='sqrt'
		num1=arr[1]
		
	    else:
                num1=arr[0]
                op=arr[1]

        if(op != '*'and op != '/'and op != '+' and op != '-' and op != '!' and op != '//' and op !="^" and op !='%' and op !='sqrt'):
            break
        
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
        
        elif op == '//': #int Division
            ans=whole(num1, num2)
	
        elif op == '%':
	        ans=mod(num1, num2)
	
    	elif op == '-':
    	    ans=subtract(num1, num2)
	
    	elif op == 'sqrt':
	        ans=squareroot(num1)

        print '\tANSWER: ', ans
	    
        #Write ans to the history file
        history.write(str(ans)+'\n') 

    
