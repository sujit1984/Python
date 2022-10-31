"""
Author: Sujit Sugathan
Date: 19 Oct 2022
Description: This is a simple implementation of the very famous bubble sort algorithm
Time Complexity: O(N^2) Space complexity: O(1)
"""

def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range (0, n-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if not swapped:
            return 

if __name__ == '__main__':
    arr=[]
    n = int(input("Enter the number of elements in the array:"))
    for i in range(0,n):
        num = int(input())
        arr.append(num)
    print(arr)

    bubbleSort(arr)
    print("The sorted array is: ", arr)
