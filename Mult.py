#Multication

#multiply
def multiply(num1, num2):
    ans = num1 * num2
    return ans

#power
def power(num1, num2):
    if num2 == 0:
        return 1

    ans=1
    for i in range(int(num2)):
        ans = ans * num1
<<<<<<< HEAD
    #return ans
    print(ans)
=======
    return ans

#factorial
>>>>>>> 2fdd3702f59f1881653c1c82a473625222b2e8d5
def fact(num1):
    if num1 == 0:
        return 1
    
    ans = num1
    num1 = num1 - 1

    for i in range(num1):
        ans = ans * num1
        num1 = num1 - 1
<<<<<<< HEAD
    return ans
        
power(2,5)
=======
    return float(ans)

>>>>>>> 2fdd3702f59f1881653c1c82a473625222b2e8d5
