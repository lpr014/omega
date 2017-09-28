#Multiplication
#
#
#
#
#
#


def multiply(num1, num2):
    ans = num1 * num2
    return ans

def power(num1, num2):
    if num2 == 0:
        return 1

    ans=1
    for i in range(num2):
        ans = ans * num1
    return ans

def fact(num1):
    if num1 == 0:
        return 1
    
    ans = num1
    num1 = num1 - 1

    for i in range(num1):
        ans = ans * num1
        num1 = num1 - 1
    return ans

