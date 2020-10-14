"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
"""

def singleNumberv1(numbers):
    """
    Use a hash map
    O(N) time, O(N) space
    """
    freq = {}
    for number in numbers:
        if freq.get(number):
            freq[number] += freq[number] + 1
        else:
            freq[number] = 1
    for key,value in freq.items():
        if value == 1:
            return key

def singleNumberv2(numbers):
    """
    Math formula 2∗(a+b+c)−(a+a+b+b+c)=c
    O(N) time, O(N) space
    set(list) create a tuple (no repeats)
    """
    unicos = set(numbers)
    return 2*sum(unicos)-sum(numbers)


def singleNumberv3(numbers):
    """
    XOR function
    O(N) time, O(1) space
    Ex: [2,3,1,2,1]
    2 xor 3 = 1 xor 1 = 0 xor 2 = 2 nox 1 = 3
    Xor uses ^ operator
    """
    x = 0
    for n in numbers:
        x = x^n
    return x
    

def printResult(numbers):
    print("*"*100)
    print("Single number version 1 on {} is {}".format(numbers,singleNumberv1(numbers)))
    print("Single number version 2 on {} is {}".format(numbers,singleNumberv2(numbers)))
    print("Single number version 3 on {} is {}".format(numbers,singleNumberv3(numbers)))


if __name__ == "__main__":
    printResult([2,2,1])
    printResult([4,1,2,1,2])
    printResult([2,1,2,1,4])
    printResult([1])