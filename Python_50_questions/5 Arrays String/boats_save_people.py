# Given an array with rhe people weight and a boat weight with maximum 2 people.
# We need ot get the minimal numbers of boats to save everyone
# Every peoples is lighter than the limit

def boats_save_people_my_version(arr,limit):
    arr = sorted(arr,reverse=True)
    boats = 0
    
    while arr:
        if arr[0] == limit or len(arr) == 1:
            boats += 1
            arr.pop(0)
        else:
            if limit - arr[0] <= arr[-1]:
                arr.pop(len(arr)-2)
            arr.pop(0)
            boats += 1
    return boats

def boats_save_people_course_version(arr,limit):
    # This version is almost equal. Seems like it doesn't need to manipulate the array
    # It uses pointers
    # Complex time O(nlogn) ; Space time O(n)
    # First n in order to order the array
    # logn for the divided steps on the check
    arr= sorted(arr,reverse=True)
    left = 0
    right = len(arr) -1
    boats = 0
    while left <= right:
        if left == right:
            boats += 1
            break
        if arr[left] + arr[right] <= limit:
            right -= 1
        left += 1
        boats += 1
    return boats
    

def printResult(arr,limit):
    print("*"*100)
    print("Weight people: {}".format(arr))
    print("Limit: {}".format(limit))
    print("Boats with my version is {}".format(boats_save_people_my_version(arr,limit)))
    print("Boats with course version is {}".format(boats_save_people_course_version(arr,limit)))


if __name__ == "__main__":
    printResult([1,2],3) #1
    printResult([3,2,2,1],3) #3
    printResult([1,3,2],4) #2
    printResult([1,2,3,3],3) #2