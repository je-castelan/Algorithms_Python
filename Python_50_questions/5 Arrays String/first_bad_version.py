class VersionMaker:
    """
    This class will help us to generate the bad versions 
    """
    def __init__(self,firstbadversion):
        self.firstbadversion = firstbadversion
    
    def isBadVersion(self,version):
        return version >= self.firstbadversion


class Solution():  

    def __init__(self,versionmaker):
        self.versionmaker = versionmaker

    def firstBadVersionForceBrute(self, n):
        """
        It will search the first bad version with force brute
        """
        steps = 0
        for i in n:
            steps += 1
            if self.versionmaker.isBadVersion(i):
                return steps, i
        return steps, 0

    def firstBadVersionBinaryTree(self, n):
        initial = 0
        ending = len(n)
        steps = 0
        while initial <= ending:
            steps += 1
            middle = (initial + ending) // 2
            statusmiddle = self.versionmaker.isBadVersion(middle)
            if initial == ending:
                return steps, middle
            if statusmiddle:
                ending = middle
            else:
                initial = middle + 1
        return steps, 0

if __name__ == "__main__":
    software1 = VersionMaker(7)
    solution1 = Solution(software1)
    steps, firstbadversion = solution1.firstBadVersionForceBrute(range(10))
    print("First bad version with forcebrute is {} in {} steps".format(firstbadversion, steps))
    steps, firstbadversion = solution1.firstBadVersionBinaryTree(range(10))
    print("First bad version with binary tree is {} in {} steps".format(firstbadversion, steps))


    software2 = VersionMaker(9987877)
    solution2 = Solution(software2)
    steps, firstbadversion = solution2.firstBadVersionForceBrute(range(1000000000))
    print("First bad version with forcebrute is {} in {} steps".format(firstbadversion, steps))
    steps, firstbadversion = solution2.firstBadVersionBinaryTree(range(1000000000))
    print("First bad version with binary tree is {} in {} steps".format(firstbadversion, steps))


    software3 = VersionMaker(4567890)
    solution3 = Solution(software3)
    steps, firstbadversion = solution3.firstBadVersionForceBrute(range(1000000000))
    print("First bad version with forcebrute is {} in {} steps".format(firstbadversion, steps))
    steps, firstbadversion = solution3.firstBadVersionBinaryTree(range(1000000000))
    print("First bad version with binary tree is {} in {} steps".format(firstbadversion, steps))
