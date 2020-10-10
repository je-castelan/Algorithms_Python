"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
"""

def missing_number(nums):
    value = len(nums) #Take extra one for the missing one (in this case we don't need to remove one)
    sumatoria = (value*(value + 1)) // 2
    
    sumatoriareal = sum(nums)
    return sumatoria - sumatoriareal 

if __name__ == "__main__":
    print(missing_number([9,6,4,2,3,5,7,0,1]))

    