
# Create an empty list
my_list = []

# Append a string to the list
my_list.append("Food")

# Insert a number at the beginning of the list
my_list.insert(0, 34)

# Extend the list with another list
my_list.extend([True, False])

# Add a tuple to the list
my_list.append(("biryani", "chocolate", "ice cream"))

# Add a set to the list
my_list.append({2, 3, 4})

# Add a dictionary to the list
my_list.append({"dosa": "chapathi", "idli": 22})

# Print the list
print(my_list)




# Create a list with numeric values
my_list = [10, 20, 30, 40, 50]

# Write a program to swap the first and last elements in a list
def swap_first_last(lst):
  # Copy the first element
  first = lst[0]
  # Replace the first element with the last element
  lst[0] = lst[-1]
  # Replace the last element with the copied first element
  lst[-1] = first
  # Return the modified list
  return lst

# Test the function
print(swap_first_last(my_list)) # [50, 20, 30, 40, 10]

# Write a program to find the sum of the digits in a list
def sum_digits(lst):
  # Initialize a variable to store the sum
  total = 0
  # Loop through each element in the list
  for num in lst:
    # Convert the number to a string and loop through each character
    for digit in str(num):
      # Convert the character back to an integer and add it to the sum
      total += int(digit)
  # Return the sum
  return total

# Test the function
print(sum_digits(my_list)) # 8

# Write a program to find the smallest element in a list
def min_element(lst):
  # Initialize a variable to store the minimum value as the first element
  minimum = lst[0]
  # Loop through each element in the list starting from the second one
  for num in lst[1:]:
    # Compare the current element with the minimum value and update it if needed
    if num < minimum:
      minimum = num
  # Return the minimum value
  return minimum

# Test the function
print(min_element(my_list)) # 10



# Create a dictionary with numeric as value in key-value pair
my_dict = {"a": 20, "b": 45, "c": 60}

# Sort the dictionary in ascending order based on the key of the dictionary
def sort_by_key(d):
  # Create a list of tuples from the dictionary items
  items = list(d.items())
  # Sort the list by the first element of each tuple (the key)
  items.sort(key=lambda x: x[0])
  # Return a new dictionary from the sorted list
  return dict(items)

# Test the function
print(sort_by_key(my_dict)) # {'a': 10, 'b': 20, 'c': 30}

# Find the sum of all the values in the dictionary
def sum_values(d):
  # Initialize a variable to store the sum
  total = 0
  # Loop through each value in the dictionary
  for value in d.values():
    # Add the value to the sum
    total += value
  # Return the sum
  return total

# Test the function
print(sum_values(my_dict)) # 60

# Write a Python code to demonstrate the sorting in descending order of values with lambda function
def sort_by_value_desc(d):
  # Create a list of tuples from the dictionary items
  items = list(d.items())
  # Sort the list by the second element of each tuple (the value) in reverse order
  items.sort(key=lambda x: x[1], reverse=True)
  # Return a new dictionary from the sorted list
  return dict(items)

# Test the function
print(sort_by_value_desc(my_dict)) # {'c': 30, 'b': 20, 'a': 10}
