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
#the .pyc files are created because we are importing them into the main
#simply ignore them, dont bother adding them to github.


print('Welcome to Calculator!')
#History.txt code here
if os.path.exists('history.txt'):
    history=open('history.txt','r+')
else:
    history=open('history.txt','w')
    history.close()
    history=open('history.txt','r+')


while True:
    while True:
        #parse the users input
        ans = -1
        arr = inputParser()
       	
	#print arr 
        
	args=len(arr)
        #testing
	num1=0
	num2=0
	#testing#
	
	if args==0:
	    break
	    	    
        if args==1:
            print ('\n\t'+str(arr[0]))
            break

        if arr=='invalid input': 
            print("\n\t"+arr)
            break

        if args >= 2:
            num1=arr[0]
            op=arr[1]
            if(op != '*'and op != '/'and op != '+' and op != '-' and op != '!' and op != '//' and op !="^" and op !='%'):
                break
        if args >= 3:
            num2=arr[2]

        print('\nCalculating...\n')

        #decide op ( + - * / ^ !)
        if op == '*':
            ans=multiply(num1, num2)
	    history.write(str(ans)+'\n')
        
        elif op == '!':
            ans=fact(int(num1))
	    history.write(str(ans)+'\n')
        
        elif op == '^':
            ans=power(num1, num2)
	    history.write(str(ans)+'\n')
            
        elif op == '+':
            ans=add(num1, num2) 
	    history.write(str(ans)+'\n')

        elif op == '/': 
            ans=divide(num1, num2)
	    history.write(str(ans)+'\n')
        
        elif op == '//': #int Division
            ans=whole(num1, num2)
	    history.write(str(ans)+'\n')
	
	elif op == '%':
	    ans=mod(num1, num2)
	    history.write(str(ans)+'\n')

        print '\tANSWER: ', ans
    
    if args==0:
        break
