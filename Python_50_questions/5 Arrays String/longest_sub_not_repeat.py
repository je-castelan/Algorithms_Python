"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def longest_sub_no_repeat_myVer(word):
    if not word:
        return 0
    maxsize = 1
    initial = 0
    end = 1
    while end < len(word):
        if word[end] not in word[initial:end]:
            maxsize = max(maxsize, len(word[initial:end + 1]))
        else:
            initial = word[initial:end].index(word[end]) + 1
        end += 1
    return maxsize

def printResult(word):
    print("*"*100)
    print("String {}".format(word))
    print("Max substring with not repeat is {} size".format(longest_sub_no_repeat_myVer(word)))


if __name__ == "__main__":
    printResult("abcabcbb") #3
    printResult("bbbbb") #1
    printResult("pwwkew") #3
    printResult("") #0
    printResult("dghjht") #4