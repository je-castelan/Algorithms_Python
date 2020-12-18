"""
Given an m x n board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, 
where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""


class Solution(object):
    def exist(self, board, word):
        """
        I was trying to put a dictionary to have the elements checked, but it was making to many space used.
        So, I check to change the analized element to null and recover again if it wasn't useful.
        Runtime: 336 ms, faster than 64.05% of Python online submissions for Word Search.
        Memory Usage: 16.9 MB, less than 88.87% of Python online submissions for Word Search.
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.__searchLetter(board, word, x, y, 0):
                    return True
        return False
    
    def __searchLetter(self, board, word, xpos, ypos, pointer):
        if xpos < 0 or ypos < 0 or xpos >= len(board) or ypos >= len(board[0]):
            return False
        if board[xpos][ypos] != word[pointer]:
            return False
        if pointer + 1 == len(word):
            return True
        tmp = board[xpos][ypos] #Letter corresponds, so I will remove it temporaly in order to not check it again.
        board[xpos][ypos] = ''
        if self.__searchLetter(board, word, xpos, ypos + 1, pointer + 1):
            return True
        if self.__searchLetter(board, word, xpos + 1, ypos, pointer + 1):
            return True
        if self.__searchLetter(board, word, xpos, ypos - 1, pointer + 1):
            return True
        if self.__searchLetter(board, word, xpos - 1, ypos, pointer + 1):
            return True
        board[xpos][ypos] = tmp # I restored the value due than I haven't the words here
        return False
        
if __name__ == "__main__":
    s = Solution()
    print("----------Solution is {}".format(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")))
    print("----------Solution is {}".format(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")))
    print("----------Solution is {}".format(s.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaaa")))  
