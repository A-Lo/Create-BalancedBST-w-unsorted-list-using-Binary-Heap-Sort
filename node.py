import collections

class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right


  def view_BST_level_order(self, root) :
    if not root: return None #If an empty root
      
    result = []
    queue = collections.deque([root])

    while queue:
      level = []
      for i in range(len(queue)):
        node = queue.popleft()
        if node: #If not None/Null
          level.append(node.val)
          queue.append(node.left)
          queue.append(node.right)

      if level: result.append(level)

    return result

  def print_level_order(self, result:list):
    for indx, level in enumerate(result):
      print(f"Level ({indx}):  {level}")

    
