"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.
"""

def containsDuplicateList(nums):
    """
    O(n) time
    O(n) space
    Leetcode mentioned than this algoritm th 5% faster than others
    """
    existing  = []
    for num in nums:
        if num in existing:
            return True
        existing.append(num)
    return False

def containsDuplicateHashmap(nums):
    """
    O(n) time
    O(n) space
    Leetcode mentioned than this algoritm th 87% faster than others
    """
    existing  = {}
    for num in nums:
        if num in existing:
            return True
        existing[num] = 1
    return False

def printResult(nums):
    print("*"*100)
    print("Duplicates (using list) in {}: {} ".format(nums, containsDuplicateList(nums)))
    print("Duplicates (using hash) in {}: {} ".format(nums, containsDuplicateHashmap(nums)))


if __name__ == "__main__":
    printResult([1,2,3,1])
    printResult([1,2,3,4])
    printResult([1,1,1,3,3,4,3,2,4,2])