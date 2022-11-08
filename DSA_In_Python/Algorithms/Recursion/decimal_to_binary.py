"""
Author: Sujit Sugathan
Date: 8 Nov 2022
Description: This is a simple recursive function that evaluates the binary of a decimal number
"""

def dec_to_bin(n):
    assert int(n) == n, "The number must be a positive integer" ## check for non-negative integers
    if n == 0 : 
        return 0
    
    return n%2 + 10 * dec_to_bin(int(n/2))


if __name__ == "__main__":
    n = int(input("Please enter a number:"))

    print(f"The decimal value of {n} is: {dec_to_bin(n)}")


