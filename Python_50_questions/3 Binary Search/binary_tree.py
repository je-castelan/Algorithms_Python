

def binarySearchRecursive(arr,obj,initial,final):
    middle = (initial+final) // 2
    if arr[middle] == obj:
        return middle
    elif initial > final:
        return -1
    elif arr[middle] < obj:
        return binarySearchRecursive(arr,obj,middle + 1,final)
    else:
        return binarySearchRecursive(arr,obj,initial,middle - 1)

def binarySearchWhile(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def printfunc(arr,obj):
    res = binarySearchRecursive(arr,obj,0,len(arr)-1)
    print ("BUSQUEDA BINARIA CON RECURSIVIDAD DE {} EN {} ES {}".format(obj,arr, res))
    res = binarySearchWhile(arr,obj)
    print ("BUSQUEDA BINARIA CON WHILE DE {} EN {} ES {}".format(obj,arr, res))


if __name__ == "__main__":
    printfunc([11,12,14,15,16,17,18],18)
    printfunc([11,12,14,15,16,17,18],17)
    printfunc([11,12,14,15,16,17,18],16)
    printfunc([11,12,14,15,16,17,18],15)
    printfunc([11,12,14,15,16,17,18],14)
    printfunc([11,12,14,15,16,17,18],13)
    printfunc([11,12,14,15,16,17,18],12)
    printfunc([11,12,14,15,16,17,18],11)
    printfunc([11,12,14,15,16,17,18,19],19)
    printfunc([11,12,14,15,16,17,18,19],18)
    printfunc([11,12,14,15,16,17,18,19],17)
    printfunc([11,12,14,15,16,17,18,19],16)
    printfunc([11,12,14,15,16,17,18,19],15)
    printfunc([11,12,14,15,16,17,18,19],14)
    printfunc([11,12,14,15,16,17,18,19],13)
    printfunc([11,12,14,15,16,17,18,19],12)
    printfunc([11,12,14,15,16,17,18,19],11)
    
    
    