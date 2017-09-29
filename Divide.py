# Created by Lorantz on 9/28/17 6:15 PM
# Last edit by Lorantz on 9/29/17 5:20 PM


def divide(num1, num2):
    
    # divide by zero error check
    if num2 == 0:
        print("CANNOT DIVIDE BY ZERO")
        return
    else:
        ans=num1/num2
        return ans
# remainder using the % symbol
def mod(num1, num2):
    if num2==0:
        print("CANNOT DIVIDE BY ZERO")
        return
    else:
        ans=num1%num2
        return ans
# used for integer division with the "//" symbol
def whole(num1, num2):
    if num2==0:
        print("CANNOT DIVIDE BY ZERO")
        return
    else:
        ans=num1//num2
        return ans
