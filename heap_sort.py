class HeapSort:

  def swap(self, A: list, i:int, j:int) ->None:
    A[i], A[j] = A[j], A[i]
    
     
  def max_heapify(self, A:list, i:int , upper_bound:int) ->None:

    left_child, right_child = i*2+1, i*2+2 
    #If a leaf node, return
    if max(left_child, right_child) > upper_bound: return

    #If parent has both childs   
    if max(left_child, right_child) < upper_bound:
      if  A[i] >= A[max(left_child,right_child)] : return  #If parent greater than both childs, no work needed
        
      elif A[left_child] > A[right_child]: 
          self.swap(A, left_child, i)
          self.max_heapify(A, left_child, upper_bound)
      else:
          self.swap(A, right_child, i)
          self.max_heapify(A,right_child, upper_bound)
  
    elif left_child < upper_bound: #If only one child: left_child
      if A[left_child] > A[i]:
        self.swap(A,left_child, i)
        self.max_heapify(A,left_child, upper_bound)


  def create_max_heap(self, A=[]) -> list:
    #Retrieving the Parents nodes only, to heapify
    parent_node = (len(A)-2) //2
    
    for indx in range(parent_node, -1, -1):
      self.max_heapify(A, indx, len(A))

    return A

  
  def heap_sort(self, A=[]) -> list:
    
    end_indx = len(A)-1
    for indx in range(end_indx, 0, -1):
      self.swap(A, indx, 0)
      self.max_heapify(A, 0, indx)

    return A

#      OG:               Max_heapified:      Heap Sorted 
#         1                 7                     0
#      0    2    ->     4        2    -->     1       2
#     3 4  7          3  0      1           3   4    7  


# Parents = 0,1,2 indexes 