# .sort() array
# Find midpoint of array by doing left_range_index plus right_range_index divided by 2 ((0 + len(array)) / 2 for first run), then floor()
# Check what value is at the midpoint 
# If it is the value, return the index and terminate
# If it is less than the desired value, then it must lie in the right side and the left_range_index becomes the midpoint
# If it is greater than the desired value, then it must lie in the left side the right_range_index becomes the midpoint

import math

def binary_search(array, value, left_range_index=0, right_range_index=None):
    # If this is the first iteration, set the righthand limit to the length of the array
    if right_range_index is None:
        right_range_index = len(array)
    
    # Calculate the midpoint
    midpoint_index = math.floor((left_range_index + right_range_index) / 2)

    # Determine whether we have found the value or not, adjusting the limits accordingly
    midpoint_value = array[midpoint_index]
    if midpoint_value == value:
        return midpoint_index
    elif midpoint_value < value:
        return binary_search(array, value, midpoint_index, right_range_index)   
    elif midpoint_value > value:
        return binary_search(array, value, left_range_index, midpoint_index)

array = [4, 9, 23, 7, 93, 52, 63, 8, 90, 3, 74, 193, 54, 43, 25, 87, 42]
desired_value = 193
array.sort()
print(f'Array: {array} with {len(array)} elements')
index = binary_search(array, desired_value)
print(f'Found {desired_value} at index {index}')