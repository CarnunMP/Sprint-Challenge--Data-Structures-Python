import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: # O(1)
#             duplicates.append(name_1) # O(1)

# Runtime complexity of the above is O(n^2).

### Attempt 1 using a BST, copied over from work done in the week (time: ~0.13s):
# from binary_search_tree import BinarySearchTree
# names_2_BST = BinarySearchTree(names_2[0])

# for i in range(1, 10000): # O(n)
#     names_2_BST.insert(names_2[i]) # O(nlog(n)), average of O(1)

# for name in names_1: # O(n)
#     if names_2_BST.contains(name): # O(nlog(n)), average of O(1)
#         duplicates.append(name) # O(1)

### Attempt 2 using Python's built-in _set_ (time: ~0.006s !!! :D )
names_1_set = set(names_1)
names_2_set = set(names_2)
duplicates = list(names_1_set.intersection(names_2_set))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

### 