"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""

class Solution(object):
    """
    I got based on the couse solution
    """

    def makePartitions(self, word):
        if len(word) == 0:
            self.solution.append(self.tmp[:])
        else:
            for x in range(1, len(word) + 1):
                part = word[0:x]
                if part == part[::-1]:
                    self.tmp.append(part)
                    self.makePartitions(word[x::])
                    self.tmp.pop()


    def partition(self, word):
        self.solution = []
        self.tmp = []
        self.makePartitions(word)
        return self.solution

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))