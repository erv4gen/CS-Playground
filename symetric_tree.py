'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 '''

def isSymmetric(self, root):

    #if root is None -> symetric 
    if not root:
        return True

    #apply dfs method for nodes
    return self.dfs(root.left, root.right)
    
def dfs(self, l, r):

    #if both child nodes exists
    if l and r:
        #nodels needs to have same vale and thir left.left - righ.righ and left.righ - righ.left shold also be the same
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)


    return l == r