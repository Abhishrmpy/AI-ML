# NumPy Multidimensional Arrays Tutorial
import numpy as np 

"""
Multidimensional Arrays in NumPy
------------------------------
A multidimensional array is an array with more than one dimension. NumPy provides powerful
support for these arrays, which can be 2D (matrices), 3D, or even higher dimensions.
"""

# 1. Creating Multidimensional Arrays
print("1. Basic Multidimensional Array Creation:")
# 2D Array (Matrix)
matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
                   
print("\n2D Array (Matrix):")
print(matrix)

# 3D Array
array_3d = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                     [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                     [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print("\n3D Array:")
print(array_3d)

# 2. Understanding Array Dimensions (ndim)
"""
ndim: Returns the number of dimensions (axes) of the array
"""
print("\n2. Array Dimensions (ndim):")
print(f"2D Array dimensions: {matrix.ndim}")
print(f"3D Array dimensions: {array_3d.ndim}")

# 3. Understanding Array Shape
"""
shape: Returns a tuple of integers indicating the size of the array in each dimension
"""
print("\n3. Array Shapes (shape):")
print(f"2D Array shape: {matrix.shape}")  # Will show (3, 3) for 3x3 matrix
print(f"3D Array shape: {array_3d.shape}")  # Will show (3, 3, 3) for 3x3x3 array

# 4. Multidimensional Array Indexing
print("\n4. Array Indexing Examples:")

# Basic indexing
print("\nBasic indexing:")
print(f"First row of matrix: {matrix[0]}")
print(f"Element at position (1,2) in matrix: {matrix[1,2]}")
print(f"Element at position (0,1,2) in 3D array: {array_3d[0,1,2]}")

# 5. Chain Indexing
"""
Chain indexing allows us to access elements by providing multiple index operations
"""
print("\n5. Chain Indexing Examples:")

# Example of creating a word using chain indexing
word = array_3d[0,0,0] + array_3d[1,1,1] + array_3d[1,0,0] + array_3d[0,0,0] + array_3d[1,0,2] + array_3d[0,2,2]
print(f"Created word using chain indexing: {word}")

# Additional chain indexing examples
print("\nMore chain indexing examples:")
# Get first row of each 2D array in 3D array
first_rows = array_3d[:,0,0]
print(f"First element of each 2D array: {first_rows}")

# Get middle column of middle matrix
middle_column = array_3d[1,:,1]
print(f"Middle column of middle matrix: {middle_column}")

# Slicing in multiple dimensions
print("\n6. Multidimensional Slicing:")
sub_matrix = matrix[0:2, 1:3]
print(f"Sub-matrix (2x2) from main matrix:\n{sub_matrix}")

# Shape manipulation
print("\n7. Reshaping Arrays:")
reshaped = matrix.reshape(1, 9)  # Reshape 3x3 to 1x9
print(f"Reshaped matrix (1x9):\n{reshaped}")

"""
Key Points to Remember:
1. ndim tells us the number of dimensions
2. shape gives us the size in each dimension
3. Indexing starts at 0
4. Chain indexing allows complex element access
5. Slicing works in all dimensions
6. Arrays can be reshaped while preserving total elements
"""
