"""
Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times <<<--- remember this
You may assume that the array is non-empty and the majority element always exist in the array.
"""

def majorityElement(nums):
    freqs = {}
    for num in nums:
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
        if freqs[num] > len(nums)/2:
            return num
    return 0



def printResult(nums):
    print("*"*100)
    print("Majority element in {} is {} ".format(nums, majorityElement(nums)))


if __name__ == "__main__":
    printResult([3,2,3])
    printResult([2,2,1,1,1,2,2])