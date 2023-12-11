def find_sum(num1, num2):
    """
    This function takes two numbers, num1 and num2,
    adds them, and returns the sum.
    """
    # Adding num1 and num2
    num_sum = num1 + num2

    # Returning the sum
    return num_sum

# Calling the function with arguments 111 and 222
my_sum = find_sum(111, 222)

# Printing the result
print(my_sum)

# Test cases
# Case 1: Adding two positive numbers
result_case1 = find_sum(5, 8)
print(result_case1)  # Expected output: 13

# Case 2: Adding a positive and a negative number
result_case2 = find_sum(-10, 5)
print(result_case2)  # Expected output: -5

# Case 3: Adding two negative numbers
result_case3 = find_sum(-3, -7)
print(result_case3)  # Expected output: -10

# Case 4: Adding zero and a positive number
result_case4 = find_sum(0, 12)
print(result_case4)  # Expected output: 12
