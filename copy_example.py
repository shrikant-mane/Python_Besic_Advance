import copy

# Original list containing a nested list
original = [[1, 2, 3], [4, 5, 6]]

# Create a shallow copy using slicing
shallow = original[:]

# 1. Modifying the outer container (Safe)
shallow.append([7, 8, 9])
print("Original:", original)  # Output: [[1, 2, 3], [4, 5, 6]]
print("Shallow: ", shallow)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Notice that adding a whole new sublist to 'shallow' did NOT affect 'original'.

# 2. Modifying the INNER nested object (Dangerous!)
shallow[0][0] = 99

print("Original after inner change:", original)
# Output: [[99, 2, 3], [4, 5, 6]]  <- SURPRISE! Original changed too!

print("Shallow after inner change: ", shallow)
# Output: [[99, 2, 3], [4, 5, 6], [7, 8, 9]]
print("id Original:", id(original))
print("id Shallow:", id(shallow))