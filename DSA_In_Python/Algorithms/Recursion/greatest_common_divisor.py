"""'
Author: Sujit Sugathan
Date: 03 November 2022
Description: This is a recursive function to calculate the GCD(Greatest Common Divisor) between two numbers
"""
def greatest_common_divisor(a,b):
    assert int(a) == a and int(b) == b, "The number must be integer" ## check for non-negative integers
    if a < 0:
        a = -1 * a

    if b < 0: 
        b= -1 * b

    if b == 0: 
        return a
    else: 
        return greatest_common_divisor(b, a%b)

if __name__ == '__main__':
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number: "))

    if a > b :
        print(f"The gcd of {a} and {b} is:", end=" ")
        print(greatest_common_divisor(a,b))

    else:
        print(f"The gcd of {a} and {b} is:", end=" ")
        print(greatest_common_divisor(b,a))

