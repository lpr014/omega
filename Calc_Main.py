#Group:
#
#Last_Edit: Sept. 26 3:15
#
#Calc_Main.py


#Main Program


print('Welcome to Calculator! \n')


num1=raw_input('Please enter your first number:')
if(num1.isdigit()==False): #error case: test if num1 is digit
    print("INVALID INPUT")
    
    
op=raw_input('Please enter the operation symbol you wish to perform:')
#error case

num2=raw_input('Please enter your second number:')
if(num2.isdigit()==False): #error case: test if num2 is digit
    print("INVALID INPUT")

print('CALCULATING....')
