# Dictionary mapping each alphabet to its position in the English alphabet
alphabetic_number_position = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

# String containing vowels
vowels = "aeiou"


def remove_vowels_from_string(lower_str):
    # convert the input string to a list of characters
    l_str_list = list(lower_str)
    
    # reads through the characters, replacing vowels with spaces
    for i, c in enumerate(l_str_list):
        if c in vowels:
            l_str_list[i] = " "
    
    #join the characters back into a string
    return "".join(l_str_list)


def calculate_consonant_values(l_str):
    # Remove vowels from the input string
    only_consonant_str = remove_vowels_from_string(l_str)
    
    # Split the string into groups of consecutive consonants
    constant_list_groups = only_consonant_str.split(" ")
    
    # Create a list of lists, where each inner list contains the characters of a consonant group
    constant_list_of_char_list = [[c for c in s] for s in constant_list_groups]
    
    # Calculated the sum of position values for each consonant group
    summed_list_values_for_list_of_contants = [
        sum([alphabetic_number_position[c] for c in l]) for l in constant_list_of_char_list if l != []
    ]

    return summed_list_values_for_list_of_contants


def find_maximum_consonant_value(lower_case_str):
    # Find the highest consonant value among all  of them
    return max(calculate_consonant_values(lower_case_str))


# Example usage
input_string = "hello world"
lower_case_str = input_string.lower()

max_consonant_value = find_maximum_consonant_value(lower_case_str)

# Prints the result
print(f"The maximum consonant value in '{input_string}' is {max_consonant_value}.")
