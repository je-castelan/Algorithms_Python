"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""


from single_list import Node
from merge_sorted_list import mergeTwoLists

def mergeKListsv1(lists):
    """
    it checks every element on the list (my original ideal)
    
    Runtime: 7232 ms, faster than 5.00% of Python online submissions for Merge k Sorted Lists.
    Memory Usage: 19.5 MB, less than 79.49% of Python online submissions for Merge k Sorted Lists.
    """
    finallist = None
    for plist in lists:
        finallist = mergeTwoLists(finallist, plist)
    return finallist

def mergeKListv2(lists):
    """
    Based on the course. It check with two pointer (from begin to middle, and from end to middle) and merge
    Loop repeats until exist only one list.

    Runtime: 104 ms, faster than 59.46% of Python online submissions for Merge k Sorted Lists.
    Memory Usage: 19.3 MB, less than 91.55% of Python online submissions for Merge k Sorted Lists.
    """
    if not lists:
        return None
    while len(lists) != 1:
        initial = 0
        ending = len(lists) - 1
        while (initial < ending):
            lists[initial] = mergeTwoLists(lists[initial], lists[ending])
            lists.pop()
            initial += 1
            ending -= 1
        return lists[0]




if __name__ == "__main__":
    pass
