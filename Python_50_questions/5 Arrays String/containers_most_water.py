"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

def maxArea(arr):
    """
    I needed to review the video to understand the solution :(
    """
    left = 0
    right = len(arr) - 1
    maxarea = 0
    while left < right:
        base = min(arr[left], arr[right]) # The maxium value with overflow the container, so we need the minimum
        height = right - left #distance
        maxarea = max(maxarea , base * height) # Check the new  max area
        if arr[left] >= arr[right]:
            right -= 1
        else:
            left += 1
    return maxarea



def printResult(arr):
    print("*"*100)
    print("List of vertical lines: {}".format(arr))
    print("Max container area is {}".format(maxArea(arr)))


if __name__ == "__main__":
    printResult([1,8,6,2,5,4,8,3,7]) #49
    printResult([1,1]) #1
    printResult([4,3,2,1,4]) #16
    printResult([1,2,1]) #2