"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        initial = 0
        ending = len(nums) - 1
        
        while initial <= ending: 
            middle = (initial + ending) // 2
            if nums[middle] == target:
                firstrange = middle
                while firstrange >= 0 and (nums[firstrange - 1] if (firstrange - 1) >= 0 else None) == nums[firstrange]:
                    firstrange -= 1 
                lastrange = middle
                while lastrange  <  len(nums) and (nums[lastrange + 1] if len(nums) > lastrange + 1 else None) == nums[lastrange]:
                    lastrange += 1 
                return [firstrange, lastrange]
            else:
                if nums[middle] > target:
                    ending = middle - 1
                else:
                    initial = middle + 1
        return [-1,-1]

        
if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([10,11,11,11,14,15],11))
    print(s.searchRange([10,11,11,11,14,15],10))
    print(s.searchRange([10,11,11,11,14,15],15))
    print(s.searchRange([11,11,11,14,15],11))
    print(s.searchRange([7,9,10,11,11,11],11))
    print(s.searchRange([1,2,2,3,4,4,4,4],4))
    print(s.searchRange([1,2,2,3,4,4,4,4],1))
    print(s.searchRange([1,2,2,3,4,4,4,4],2))
