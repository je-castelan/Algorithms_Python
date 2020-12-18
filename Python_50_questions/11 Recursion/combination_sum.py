"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Runtime: 48 ms, faster than 79.85% of Python online submissions for Combination Sum.
        Memory Usage: 13.4 MB, less than 66.19% of Python online submissions for Combination Sum.
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        for i in range(len(candidates)):
            diff = target - candidates[i]
            if diff == 0:
                combinations.append([candidates[i]])
            elif diff > 0:
                news = self.combinationSum(candidates[i:], diff)
                if news:
                    for n in news:
                        toappend = sorted(n + [candidates[i]])
                        if toappend not in combinations:
                            combinations.append(toappend)
        return combinations


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))