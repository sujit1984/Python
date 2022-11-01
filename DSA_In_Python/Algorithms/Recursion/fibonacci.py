"""
Author : Sujit Sugathan
Date : 31 Oct 2022
Description : This is a recursive method to print the fibonacci series for a given value of n
"""

def fibonacci(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer" ## check for non-negative integers
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # condition for recursion


if __name__=="__main__":
    num = int(input("Enter the number for the fibonacci series: "))
    for i in range(0,num):
        print(fibonacci(i), end=" ")

        
 