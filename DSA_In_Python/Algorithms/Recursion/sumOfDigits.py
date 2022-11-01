"""
Author: Sujit Sugathan
Date: 01 Nov 2022
Description: This program computes the sum of the digits of an integer recursively.
"""
def sum_of_digits(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer" ## check for non-negative integers
    if n == 0:
       return 0
    else: 
        return int(n%10) + sum_of_digits(int(n/10))  

if __name__ == "__main__":
    num = int(input("Enter the number: "))

    print(sum_of_digits(num))