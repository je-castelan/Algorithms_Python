"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""

class Solution(object):
    """
    ADVICE: This isn't my response. I admit than I haven't defined myself the solution
    """
    def isPalin(self, seg):
        i = 0
        j = len(seg)-1
        while(i < j):
            if(seg[i] != seg[j]):
                return False
            i += 1
            j -= 1
        return True

    def dfs(self, s):
        if(len(s) == 0 and len(self.temp) > 0):
            self.res.append(self.temp[:])
            return
        n = len(s)+1
        for i in range(1, n):
            seg = s[0:i]
            if(self.isPalin(seg)):
                self.temp.append(seg)
                self.dfs(s[i:])
                self.temp.pop()

    def partition(self, s: str):
        self.res = []
        self.temp = []
        self.dfs(s)
        return self.res

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))