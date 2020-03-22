'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

ALGORITHM:
1) identify the root:
- We know that the root is the first element of preorder
- Split inorder list by key value

2) Recurcivly constrict the tree

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            #1) - identify the root
            v = preorder.pop(0)
            root_index = inorder.index(v)
            root = TreeNode(inorder[root_index])
            
            #2) restore left part
            root.left = self.buildTree(preorder,inorder[:root_index])

            #3) restore right part
            root.right = self.buildTree(preorder,inorder[root_index+1 :])
            

            return root

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = Solution().buildTree(preorder,inorder)
    print(root)
