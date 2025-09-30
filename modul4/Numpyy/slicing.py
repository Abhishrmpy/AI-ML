import numpy as np 

array = np.array([[1, 2, 3],
                  [4, 5, 6], 
                  [7, 8, 9],
                  [10, 11, 12]])

# array[start:stop:step]

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])

# =============================
# NumPy Slicing Notes (2D Array)
# =============================
# Slicing allows you to extract subarrays from a NumPy array using the syntax:
# array[start:stop:step]
# For 2D arrays, you can slice rows, columns, or both.

print("Original 2D Array:")
print(array)

# 1. Slicing Rows
print("\n1. Slicing Rows (first two rows):")
print(array[0:2, :])  # Rows 0 and 1, all columns

# 2. Slicing Columns
print("\n2. Slicing Columns (first two columns):")
print(array[:, 0:2])  # All rows, columns 0 and 1

# 3. Slicing a Submatrix
print("\n3. Slicing a Submatrix (rows 1-2, columns 1-2):")
print(array[1:3, 1:3])  # Rows 1 and 2, columns 1 and 2

# 4. Slicing with Steps
print("\n4. Slicing with Steps (every other row):")
print(array[::2, :])  # Every other row, all columns

# 5. Single Row or Column
print("\n5. Single Row (row 2):")
print(array[2, :])  # Row 2, all columns

print("\n6. Single Column (column 1):")
print(array[:, 1])  # All rows, column 1

# 6. Negative Indices
print("\n7. Last two rows using negative indices:")
print(array[-2:, :])  # Last two rows, all columns

"""
Summary:
- array[start:stop, :] slices rows
- array[:, start:stop] slices columns
- array[start1:stop1, start2:stop2] slices a submatrix
- Negative indices count from the end
- Steps can be used to skip rows/columns
"""
print(array[0:2:1])
