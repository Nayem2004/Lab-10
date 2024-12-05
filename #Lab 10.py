#Lab 10

import string  # Imports the string module to access lowercase alphabetic characters

# Defines a recursive function that checks if a string is a palindrome
def is_palindrome(s):
    # Normalizes the string by removing non-alphanumeric characters and converting it to lowercase
    s = ''.join(filter(str.isalnum, s)).lower()
    
    # Returns True if the string length is 0 or 1, indicating it is a palindrome
    if len(s) <= 1:
        return True
    
    # Returns False if the first and last characters are different
    if s[0] != s[-1]:
        return False
    
    # Recursively calls itself with the inner substring, excluding the first and last characters
    return is_palindrome(s[1:-1])

# Defines a recursive function that counts vowels and consonants in a string
def count_vowels_consonants(s, vowels=0, consonants=0):
    # Returns the current counts if the string is empty (base case)
    if not s:
        return vowels, consonants

    # Converts the first character to lowercase for consistent comparison
    char = s[0].lower()
    
    # Increments the vowel count if the character is a vowel
    if char in 'aeiou':
        return count_vowels_consonants(s[1:], vowels + 1, consonants)
    
    # Increments the consonant count if the character is a consonant
    elif char in string.ascii_lowercase:
        return count_vowels_consonants(s[1:], vowels, consonants + 1)
    
    # Skips non-alphabetic characters and continues recursion
    else:
        return count_vowels_consonants(s[1:], vowels, consonants)

# Defines the main function that coordinates the program's actions
def main():
    # Prompts the user to input a string and stores it in input_string
    input_string = input("Enter a string: ")
    
    # Calls is_palindrome to check if the input string is a palindrome
    if is_palindrome(input_string):
        # Prints the result if the string is a palindrome
        print("The string is a palindrome.")
    else:
        # Prints the result if the string is not a palindrome
        print("The string is not a palindrome.")
    
    # Calls count_vowels_consonants to count vowels and consonants in the input string
    vowels, consonants = count_vowels_consonants(input_string)
    
    # Prints the counts of vowels and consonants
    print(f"Vowels: {vowels}, Consonants: {consonants}")
    
    # Compares the counts and prints whether vowels or consonants are more prevalent
    if vowels > consonants:
        print("The string contains more vowels than consonants.")
    else:
        print("The string contains more consonants than vowels.")

# Calls the main function to start the program
main()
