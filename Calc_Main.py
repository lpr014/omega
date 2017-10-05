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
    history=open('.history','r+b')
    for line in history:
        pass
else:
    history=open('.history','wb')
    history.close()
    history=open('.history','r+b')


while True:
    while True:
        #parse the users input
        ans = -1
        arr = inputParser()

        if arr==0:
            break


        #Print ANS history        
        if arr=='history':
            history.close()
            hist=open('.history','rb')
            lines = hist.readlines()
            
            for i in range(0, len(lines)):
                print lines[i]

            hist.close()
            history=open('.history','r+b')
            for line in history:
                pass
            break
        
        
               	
	    #print arr 
        args=len(arr)

        if args==1:
            print ('\n\t'+str(arr[0]))
            break

        if arr=='invalid input': 
            print("\n\t"+arr)
            break
        
        if args >= 2:
            if arr[0] == 'sqrt(': #test for sqrt
                op = 'sqrt'
                num1=arr[1]
            else:
                num1=arr[0]
                op=arr[1]
                 
        #Use Prev. Ans
        if(arr[0] == '*' or arr[0] == '/' or arr[0] == '+' or arr[0] == '-' or arr[0] == '//' or arr[0] == '^' or arr[0] == '%'):
            op=arr[0]
            num2=arr[1]
            

            history.close()
            hist = open('.history','rb')

            lines = hist.readlines()
            last = len(lines)
            if last==0:
                print 'NO HISTORY'
                break
            
            num1 = float(lines[last-1].strip())
           
            hist.close()
            history = open('.history','r+b')
            for line in history:
                pass
	    

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

    if arr==0:
        break


history.close() 

    
