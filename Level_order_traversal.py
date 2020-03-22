'''

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        levels = []
        
        def traverse_level(level,root):
            if root:
                print('root is not null')
                if level == len(levels):
                    levels.append([])
                    print('creating level')
                levels[level].append(root.val)
                print('on level ', level,'appending value')

                print('traversing level ',level+1,'left')
                traverse_level(level+1,root.left)
                
                print('traversing level ',level+1,'right')
                traverse_level(level+1,root.right)
        traverse_level(0,root)
        return levels


s = Solution()
s.levelOrder()