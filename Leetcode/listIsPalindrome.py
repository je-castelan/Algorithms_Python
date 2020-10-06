# https://leetcode.com/problems/palindrome-linked-list/
# Given a singly linked list, determine if it is a palindrome.
# Example 1:
#
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true
#
# Solucion O(n)


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        value = str(self.__getCompleteValue(head,1))
        limit = len(value) - 1
        initial = 0
        while initial < limit:
            if value[initial] == value[limit]:
                limit -= 1
                initial += 1
            else:
                return False
        return True


    
    def __getCompleteValue(self,head,exponent):
        newvalue = head.val*exponent
        return newvalue + (self.__getCompleteValue(head.next,exponent*10) if head.next else 0)

if __name__ == "__main__":
    l1 = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
    l3 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(4,ListNode(3,ListNode(2,ListNode(1))))))))
    l4 = ListNode(1,ListNode(2,ListNode(2,ListNode(4,ListNode(4,ListNode(3,ListNode(2,ListNode(1))))))))
    l2 = ListNode(1,ListNode(2,ListNode(2,ListNode(1,ListNode(1)))))
    s = Solution()
    print(s.isPalindrome(l1))
    print(s.isPalindrome(l2))
    print(s.isPalindrome(l3))
    print(s.isPalindrome(l4))
        