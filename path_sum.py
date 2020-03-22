'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root,csum):
        
        #if the node is leafe 
        if root is None:
            #check if the cumsum equal to input
            if csum == self.check:
                return True
            else:
                return False
        
        csum += root.val
        
        #find any matches
        return self.dfs(root.left,csum) or self.dfs(root.right,csum)
        
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.check = sum
        if not root:
            return False
        else:
            return self.dfs(root,0)

class Solution2:
    def dfs(self,root,csum):
        #if node exist
        if root:
            #if node a leafe
            #if not (root.left and root.right): NOT WORKING 
            #USE is None instead
            if root.left is None and root.right is None:
            
                #add value to cumsum
                csum += root.val
                
                #return
                #return True if csum ==self.check else False
                #is not working, == is used 
                if csum == self.check:
                    return True

            #check for children
            return self.dfs(root.left,csum) or self.dfs(root.right,csum)
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.check = sum
        return self.dfs(root,0)


root = TreeNode(5)
root.left = TreeNode(4)

root.left.left = TreeNode(11)
root.left.left.left =TreeNode(7)
root.left.left.right = TreeNode(2)


root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)


s = Solution()
s2 = Solution2()
res = s.hasPathSum(root,22)
res2 = s2.hasPathSum(root,22)
# res = s.hasPathSum(None,0)
print(res,'\n',res2)