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
