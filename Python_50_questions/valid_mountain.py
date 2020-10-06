# Given an array of integer, return true if:
# - Lenght of the array is bigger or equal to 3
# - A[0] < A[1] < ... A[i-1] < A[i]
# - A[i] > A[i+1] > ... > A[A.length - 1]

def valid_mountain_myver(arr):
    if len(arr) < 3:
        return False
    # Checking increasing side
    i = 0
    while arr[i] < arr[i+1]:
        i += 1
        # What if it will never decrease???
        if i + 1 == len(arr):
            return False
    # What if never increase???
    if i == 0:
        return False
    # Checking decresing side
    j = len(arr) -1
    while arr[j] < arr[j-1]:
        j -= 1
    return i == j


def printResult(arr):
    print("*"*100)
    print("Array: {}".format(arr))
    print("Mountain on my version is {}".format(valid_mountain_myver(arr)))


if __name__ == "__main__":
    printResult([0,2,3,4,5,2,1,0]) #True
    printResult([0,2,6,4,5,2,1,0]) #False
    printResult([1,3,5,7,9,11,13,15,10,8,2]) # True
    printResult([3,5,5]) #False
    printResult([0,3,2,1]) #True
    printResult([3,4,5]) #False
    printResult([5,4,3]) #False