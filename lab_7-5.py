def find_min_max(input_list):
    # Check if the list has at least 2 unique numbers.
    unique_numbers = set(input_list)
    
    if len(unique_numbers) < 2:
        return "error: list does not meet specifications"
    
    # Find the highest and lowest values in the list.
    min_value = min(input_list)
    max_value = max(input_list)

    # Return the results.
    return f"Highest Value: {max_value}, Lowest Value: {min_value}"

def unique_words_list():
    # Ask the user to input 5 unique words.
    word1 = input("usher")
    word2 = input("ducks")
    word3 = input("books")
    word4 = input("money")
    word5 = input("trees")

    # Construct a list of the 5 input values in the order given.
    user_words_list = [word1, word2, word3, word4, word5]

    # Display a list where each index corresponds to the length of the word given by the user at the corresponding index.
    lengths_list = [len(word1), len(word2), len(word3), len(word4), len(word5)]

    # Return the original list and the lengths list.
    return user_words_list, lengths_list

def double_numeric_values():
    # Ask the user to input 3 numeric values.
    numeric_value1 = float(input("3.4"))
    numeric_value2 = float(input("87"))
    numeric_value3 = float(input("67"))

    # Construct a list of the 3 input values in order.
    numeric_values_list = [numeric_value1, numeric_value2, numeric_value3]

    # Display a list with each of the values as integers that have been doubled.
    doubled_values_list = [int(value * 2) for value in numeric_values_list]

    # Return the original list and the list with doubled integer values.
    return numeric_values_list, doubled_values_list

def classify_numeric_values():
    #input 3 numeric values.
    numeric_value1 = int(input("3"))
    numeric_value2 = int(input("9"))
    numeric_value3 = int(input("12"))

    # Construct a list of the 3 input values in the order given.
    numeric_values_list = [numeric_value1, numeric_value2, numeric_value3]

    # Check if all numbers in the list are even, odd, or mixed.
    if all(value % 2 == 0 for value in numeric_values_list):
        result = "even"
    elif all(value % 2 != 0 for value in numeric_values_list):
        result = "odd"
    else:
        result = "mixed"

    # Return the result.
    return result

# Test Cases
# Test find_min_max function
test_list_7 = [2, 5, 8, 4, 1, 10, 5]  # Test on a list meeting specifications
result_7 = find_min_max(test_list_7)
print("Test 4 - find_min_max:", result_7)

test_list_8 = [3, 3, 3, 3]  # Test on a list not meeting specifications
result_8 = find_min_max(test_list_8)
print("Test 5 - find_min_max:", result_8)

# Test unique_words_list function
result_9 = unique_words_list()
print("Test 6 - unique_words_list:", result_9)

# Test double_numeric_values function
result_10 = double_numeric_values()
print("Test 7 - double_numeric_values:", result_10)

# Test classify_numeric_values function
result_11 = classify_numeric_values()
print("Test 8 - classify_numeric_values:", result_11)
