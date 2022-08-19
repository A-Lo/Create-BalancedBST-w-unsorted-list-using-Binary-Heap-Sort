import heap_sort 
import create_bst 

l = [1,10,5,3,2,0,7]

#----- Sorting the unsorted list using Heap Sort:  -----
'''
In heap sort:
  First: Create a max_heapify from the unsorted list
  Second: Heapsort the Max_heapified list
'''

sort_obj = heap_sort.HeapSort()
heapified_ls = sort_obj.create_max_heap(l)
print('Heapified:',heapified_ls)
sorted_ls = sort_obj.heap_sort(heapified_ls)
print('Sorted:',sorted_ls)


#-----  Creating BST from sorted list:  -----


root_obj = create_bst.BST()
root = root_obj.listToBST(sorted_ls)

print()
#-----  Viewing BST structure:  -----
print(f"Root value: {root.val}")
print(f"Root left child: {root.left.val}")
print(f"Root right child: {root.right.val}")

print(f"Root left-left child: {root.left.left.val}")
print(f"Root left-right child: {root.left.right.val}")

print(f"Root right-left child: {root.right.left.val}")


#-----  Viewing BST structure by Level Order Traversal:  -----
print("\nLevel Order Traversal:")

view_levelOrder_ls = create_bst.node.TreeNode().view_BST_level_order(root)

create_bst.node.TreeNode().print_level_order(view_levelOrder_ls)



  
#-----  Manual Creation of Unbalanced BT:  -----

root_unbalaned = create_bst.node.TreeNode(4)
root_unbalaned.left = create_bst.node.TreeNode(3)
root_unbalaned.right = create_bst.node.TreeNode(5)