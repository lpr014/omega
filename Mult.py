#Multication

#multiply
def multiply(num1, num2):
    ans = num1 * num2
    return float(ans)

#power
def power(num1, num2):
    ans=1
    
    if num2<0:
        if num1==0:
            return("invalid input")
        for i in range(int(-num2)):
            ans = ans * num1
        return 1.0/ans
    
    if num2 == 0:
        return 1
    
    if num1==0:
        return 0
        
    for i in range(int(num2)):
        ans = ans * num1
    return float(ans)

#factorial
def fact(num1):
    if num1<0:
        return "invalid input"
    if num1 == 0:
        return 1
    
    ans = num1
    num1 = num1 - 1

    for i in range(num1):
        ans = ans * num1
        num1 = num1 - 1
    return float(ans) 
