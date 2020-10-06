import functools
def plane_list(arr):
    # Getting an array of arrays, we need to return one array with the contain of all subarrays.
    # Try with only one iteration.
    # [[1, 2], [[3, 4]], [1,[]]] returns [1, 2, [3, 4], [1, []]]
    # Challenge of Hola Mundo Channel on https://www.youtube.com/watch?v=MXmQM_Uehtk&t=584s

    #This is my first version. Later I tried with reduce
    #result =[]
    #for val in arr:
    #    result += val
    
    result = functools.reduce(lambda a,b: a + b , arr)
    return result

if __name__ == "__main__":
    print(plane_list([[1,4],[6,5],[3,[4,7]]]))
    print(plane_list([[1, 2], [[3, 4]], [1,[]]]))
    print(plane_list([[1,2,3],[4,5],[6]]))
    