"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
import functools

def groupAnagrams(words):
    possible = {}
    for word in words:
        ordered = ''.join(sorted(word))
        if ordered in possible:
            possible[ordered].append(word)
        else:
            possible[ordered] = [word]
    return [element for element in possible.values()]
        

def printResult(words):
    print("*"*100)
    print("Group anagrams in {} are {} ".format(words, groupAnagrams(words)))


if __name__ == "__main__":
    printResult(["eat","tea","tan","ate","nat","bat"])
    printResult([""])
    printResult(["a"])