'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


ALGORITHM:
1) identify the root:
- We know that the root is the last element in the postorder traversal.
- We know that in inorder list left from the root - is a left child/subchilds and to right - right child/subchild

2) Recurcivly constrict the tree

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            #1) - identify the root
            root_index = inorder.index(postorder.pop())
            root = TreeNode(inorder[root_index])
            
            #2) restore right part
            root.right = self.buildTree(inorder[root_index+1 :], postorder)
            
            #3) restore left part
            root.left = self.buildTree(inorder[:root_index],postorder)
            return root

