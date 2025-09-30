import numpy as np 

array = np.array([1,2,3,4,5])
#scalar arithmetic operations
print("original array:")
print(array)
print(array + 5)

print("original array:")
print(array)
print(array - 5)

print("original array:")
print(array)
print(array * 5)

print("original array:")
print(array)
print(array ** 5)

print("original array:")
print(array)
print(array / 5)

print("you can also perform operations between two arrays of the same size:")
array2 = np.array([5,4,3,2,1])
print("original array:")
print(array)
print("second array:")
print(array2)
print(array + array2)


# =============================
# NumPy Vectorized Math Operations (Notes)
# =============================
# Vectorized operations in NumPy allow you to perform element-wise mathematical operations
# on entire arrays without using explicit loops. This is much faster and more concise than
# using Python loops.

# Example arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("\nVectorized Addition:")
print(f"arr1: {arr1}")
print(f"arr2: {arr2}")
print(f"arr1 + arr2: {arr1 + arr2}")  # Adds each element

print("\nVectorized Subtraction:")
print(f"arr1 - arr2: {arr1 - arr2}")

print("\nVectorized Multiplication:")
print(f"arr1 * arr2: {arr1 * arr2}")

print("\nVectorized Division:")
print(f"arr1 / arr2: {arr1 / arr2}")

# Universal Functions (ufuncs)
print("\nUniversal Functions (ufuncs) Examples:")
print(f"np.sqrt(arr1): {np.sqrt(arr1)}")
print(f"np.exp(arr2): {np.exp(arr2)}")
print(f"np.sin(arr1): {np.sin(arr1)}")

# Comparison operations
print("\nElement-wise Comparison:")
print(f"arr1 > 25: {arr1 > 25}")
print(f"arr2 == 2: {arr2 == 2}")

"""
Summary:
- Vectorized operations apply math to each element of the array automatically
- No need for explicit loops
- Works for arithmetic, comparison, and universal functions (ufuncs)
- Arrays must be of the same shape for element-wise operations
"""

# =============================
# NumPy Element-wise Arithmetic Operations (Notes)
# =============================
# Element-wise arithmetic means performing operations between corresponding elements of two arrays of the same shape.
# The result is a new array where each element is the result of the operation on the corresponding elements.

arrA = np.array([2, 4, 6, 8])
arrB = np.array([1, 3, 5, 7])

print("\nElement-wise Addition:")
print(f"arrA: {arrA}")
print(f"arrB: {arrB}")
print(f"arrA + arrB: {arrA + arrB}")

print("\nElement-wise Subtraction:")
print(f"arrA - arrB: {arrA - arrB}")

print("\nElement-wise Multiplication:")
print(f"arrA * arrB: {arrA * arrB}")

print("\nElement-wise Division:")
print(f"arrA / arrB: {arrA / arrB}")

print("\nElement-wise Power:")
print(f"arrA ** arrB: {arrA ** arrB}")

"""
Summary:
- Element-wise operations require arrays to be the same shape
- Each operation is performed between corresponding elements
- The result is a new array of the same shape
"""

# =============================
# NumPy Element-wise Comparison Operators (Notes)
# =============================
# Comparison operators in NumPy are applied element-wise between arrays of the same shape or between an array and a scalar.
# The result is a boolean array of the same shape.

arrX = np.array([10, 20, 30, 40])
arrY = np.array([15, 20, 25, 40])

print("\nElement-wise Greater Than:")
print(f"arrX > arrY: {arrX > arrY}")

print("\nElement-wise Less Than:")
print(f"arrX < arrY: {arrX < arrY}")

print("\nElement-wise Equal To:")
print(f"arrX == arrY: {arrX == arrY}")

print("\nElement-wise Not Equal To:")
print(f"arrX != arrY: {arrX != arrY}")

print("\nElement-wise Greater Than or Equal To:")
print(f"arrX >= arrY: {arrX >= arrY}")

print("\nElement-wise Less Than or Equal To:")
print(f"arrX <= arrY: {arrX <= arrY}")

# Comparison with scalars
print("\nComparison with Scalar (arrX > 25):")
print(arrX > 25)

"""
Summary:
- Comparison operators (>, <, ==, !=, >=, <=) work element-wise
- Result is a boolean array
- Can compare array-to-array (same shape) or array-to-scalar
"""
