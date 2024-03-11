
#python algorithm for bubblesort
def bubbleSort(arr):
    n=len(arr)
#For loop to traverse through all element in array
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Range of the array is from 0 to n-i-1

# Swap the elements if the element found

#is greater than the adjacent element

# Driver code
# Example to test the above code

arr = [ 2, 1, 10, 23 ]
bubbleSort(arr)

print("Sorted array is:",arr)


