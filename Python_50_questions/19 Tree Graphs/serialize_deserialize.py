
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(self, node):
        if node:
            return "{}#{}{}".format(node.val, self.serialize(node.left), self.serialize(node.right))
        else:
            return "X#"

    def deserialize(self, s):
        values = s.split("#")
        return self._helper_deserialize(values)

    def _helper_deserialize(self, stack):
        value = stack.pop(0)
        if value == "X":
            return None
        n = TreeNode(val = value)
        n.left = self._helper_deserialize(stack)
        n.right = self._helper_deserialize(stack)
        return n




if __name__ == "__main__":
    t = TreeNode(val = 1)
    t.left = TreeNode(val = 2)
    t.right = TreeNode(val = 3)
    t.right.left = TreeNode(val = 4)
    t.right.right = TreeNode(val = 5)

    s = Solution()
    print("*****Serializing**********")
    print(s.serialize(t))

    node = s.deserialize("1#2#X#X#3#4#X#X#5#X#X#")
    print("*****Deserializing**********")
    print("{} - {} - {}".format(node.val, node.left.val, node.right.val))
    print("{} - {}".format(node.right.left.val, node.right.right.val))