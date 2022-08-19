import node 

#Creates a balanced binary serach tree from sorted Array
class BST:
  def listToBST(self, nums: list):
    
    if len(nums) == 0: return None
    if len(nums) == 1: return node.TreeNode(nums[0])

    mid = len(nums)//2
    root = node.TreeNode(nums[mid])  #Assign root as middle of list

    root.left = self.listToBST(nums[:mid]) #Cut list in half; take left
    root.right = self.listToBST(nums[mid+1:])

    return root


