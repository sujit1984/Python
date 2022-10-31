"""
Author: Sujit Sugathan
Date: 31 Oct 2022
Description: This function is a simple recursive function to calculate the factorial of n.
"""

def factorial(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer" ## check for non-negative integers
    if n in (0,1):
        return 1
    else: 
        return n * factorial(n-1) # recursive function

if __name__ == "__main__":
    num = int(input("Enter the number for factorial:"))
    results= factorial(num)
    print(f"The factorial of {num} is {results}")