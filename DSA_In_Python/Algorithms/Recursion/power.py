"""
Author: Sujit Sugathan
Date: 01 Nov 2022 
Description: This is a recursive function which returns the nth power of a given integer
"""

def power(base,exp):
    # check for non-negative integers
    assert exp >= 0 and int(exp) == exp, "The number must be a positive integer"
    if exp ==0:
        return 1
    else:
        return base * power(base, exp-1)


if __name__ == "__main__":
    x = int(input("Enter the base number: "))
    n = int(input("Enter the exponent number: "))
    print(power(x,n))