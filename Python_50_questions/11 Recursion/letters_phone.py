"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""
class Solution(object):
    def __init__(self):
        self.phone_map = {"2": ["a","b","c"],
                    "3": ["d","e","f"],
                    "4": ["g","h","i"],
                    "5": ["j","k","l"],
                    "6": ["m","n","o"],
                    "7": ["p","q","r","s"],
                    "8": ["t","u","v"],
                    "9": ["w","x","y","z"]
                    } 
    
    def letterCombinations(self, digits):
        """
        Runtime: 4 ms, faster than 100.00% of Python online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 13.6 MB, less than 15.83% of Python online submissions for Letter Combinations of a Phone Number.
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return None
        elif len(digits) == 1:
            return self.phone_map[digits] 
        letters = self.phone_map[digits[0]]
        combinations = []
        for letter1 in letters:
            letters2 = self.letterCombinations(digits[1::])
            for letter2 in self.letterCombinations(digits[1::]):
                combinations.append("{}{}".format(letter1,letter2))
        return combinations

if __name__ == "__main__":
    s = Solution()
    print("Combinations are {}".format(s.letterCombinations("23")))
    


