

def move_zeros_v1(arr):
    """
    We need to move the zeros values at the end of the array.
    """
    non_zero = [i for i in arr if i != 0]
    return non_zero + [0]*(len(arr)-len(non_zero))

def move_zeros_v2(arr):
    """
    We need to move the zeros values at the end of the array.

    """
    countzeros = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.pop(i)
            countzeros += 1 
        else:
            i += 1
    return arr + [0]*countzeros

def move_zeros_video_solution(arr):
    """
    We need to move the zeros values at the end of the array
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for k in range(j,len(arr)):
        arr[k] = 0
    return arr


def printSolutions(arr):
    print("*"*100)
    print("Solution with version 1 is {}".format(move_zeros_v1(arr.copy())))
    print("Solution with version 2 is {}".format(move_zeros_v2(arr.copy())))
    print("Solution with version video version is {}".format(move_zeros_video_solution(arr)))

if __name__ == "__main__":
    printSolutions([0,1,0,3,12])