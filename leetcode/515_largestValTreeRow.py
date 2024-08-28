# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []

        largestVals = [root.val]
        nextRow = []
        if root.left != None: nextRow.append(root.left)
        if root.right != None: nextRow.append(root.right)

        while len(nextRow) > 0:
            newRow = []
            thisMax = nextRow[0].val
            for el in nextRow:
                thisMax = max(thisMax, el.val)
                if el.left  != None: newRow.append(el.left)
                if el.right != None: newRow.append(el.right)
            largestVals.append(thisMax)
            nextRow = newRow
        
        return largestVals

        