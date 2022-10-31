def factorial(n):
    assert n >=0 and int(n) == n, "The number must be a positive integer"
    if n in (0,1):
        return 1
    else: 
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter the number for factorial:"))
    results= factorial(num)
    print(f"The factorial of {num} is {results}")