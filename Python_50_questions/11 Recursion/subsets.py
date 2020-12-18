"""
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
"""
class Solution(object):
    def subsets(self, nums):
        #return self.__createsubsetsv1(nums, [], {})
        return self.__createsubsetsv2(nums, [[]], {})


    def __createsubsetsv1(self, nums, currentsubsets, analized):
        """
        This version reanalize the initial found subsets. Efficient time was only 2%
        """
        if len(nums) == 0:
            return currentsubsets
        addelement = nums[0]
        nums.pop(0)
        if addelement in analized:
            return self.__createsubsets(nums, currentsubsets, analized)
        if not currentsubsets:
            newelements = [[],[addelement]]
        else:
            newelements = []
            for element in currentsubsets:
                newelements.append(element + [])
                newelements.append(element + [addelement])
        analized[addelement] = 1
        return self.__createsubsets(nums, newelements, analized)

    def __createsubsetsv2(self, nums, currentsubsets, analized):
        """
        Better version. Current found subset are not being reanalized. Only add new elements. Efficient time was 92.84%
        """
        if len(nums) == 0:
            return currentsubsets
        newelements = []
        addelement = nums[0]
        nums.pop(0)
        if addelement not in analized:
            for element in currentsubsets:
                newelements.append(element + [addelement])
            analized[addelement] = 1
            currentsubsets = currentsubsets + newelements
        return self.__createsubsetsv2(nums, currentsubsets, analized)


if __name__ == "__main__":
    s = Solution()
    print("Subsets = {}".format(s.subsets([1,2,3])))
    print("Subsets = {}".format(s.subsets([1,2,3,5])))
    print("Subsets = {}".format(s.subsets([1,2,3,2,5])))
    print("Subsets = {}".format(s.subsets([])))
    print("Subsets = {}".format(s.subsets([1])))