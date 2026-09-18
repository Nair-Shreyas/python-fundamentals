"""
Palindrome Checker
"""

# This approach is intended to enhance understanding and demonstrate a strong grasp of 
# the programming concepts applied throughout the code.

# ======================================================================================================================
# QUESTION 4: PALINDROME CHECKER AND WORD ANALYSIS
# ----------------------------------------------------------------------------------------------------------------------
# Goal:
#   - Check if a sentence is a palindrome (ignoring spaces, punctuation, and case).
#   - Display a list of words with their cleaned lengths.
#   - Count the total number of words.
# ======================================================================================================================


#======================
# --- CODE START --- #
#======================


# ============================================================================================
# ▶ IMPORT REQUIRED MODULES
# --------------------------------------------------------------------------------------------
# Purpose:
#   Import the built-in `string` module, which provides a list of punctuation characters 
#   (via `string.punctuation`) to help clean and normalize sentences during analysis.
# ============================================================================================

import string  # ▶ import: https://www.w3schools.com/python/ref_keyword_import.asp
# Imports Python's built-in `string` module, which includes useful constants like `string.punctuation`.
# Used to remove punctuation from input strings for accurate palindrome checks and word length analysis.

# ============================================================================================
# ▶ FUNCTION 1: Check if a sentence is a palindrome
# --------------------------------------------------------------------------------------------
# Purpose:
#   This function determines whether a sentence is a palindrome by:
#   1. Converting to lowercase.
#   2. Removing punctuation.
#   3. Removing spaces.
#   4. Comparing the cleaned sentence to its reverse.
# ============================================================================================

def is_palindrome(sentence):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # -------------------------------------------------------------
    # STEP 1: Convert entire sentence to lowercase
    # -------------------------------------------------------------
    sentence = sentence.lower()  
    # ▶ lower(): https://www.w3schools.com/python/ref_string_lower.asp
    # This ensures that 'A' and 'a' are treated the same when comparing characters.
    
    # -------------------------------------------------------------
    # STEP 2: Remove punctuation from the sentence
    # -------------------------------------------------------------
    sentence = ''.join(char for char in sentence if char not in string.punctuation)  
    # ▶ join(): https://www.w3schools.com/python/ref_string_join.asp
    # ▶ string.punctuation: gives standard punctuation marks like !, ., ?, etc.
    # Removes all punctuation characters by using a generator expression inside join().
    
    # -------------------------------------------------------------
    # STEP 3: Remove spaces between words
    # -------------------------------------------------------------
    sentence = sentence.replace(" ", "")  
    # ▶ replace(): https://www.w3schools.com/python/ref_string_replace.asp
    # Eliminates spaces to treat the sentence as one continuous string.
    
    # -------------------------------------------------------------
    # STEP 4: Check if sentence equals its reverse
    # -------------------------------------------------------------
    return sentence == sentence[::-1]  
    # ▶ slicing [::-1]: https://www.w3schools.com/python/gloss_python_string_slice.asp
    # [::-1] creates a reversed version of the string.
    # Returns True if the sentence reads the same forward and backward (i.e., a palindrome).


# ============================================================================================
# ▶ FUNCTION 2: List each word with its cleaned length (punctuation removed)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Takes a sentence and returns a list of tuples, where each tuple contains:
#   ▪ the word (with punctuation removed)
#   ▪ the length of the cleaned word
#
#   Ensures that blank or empty words (e.g., only punctuation) are not included.
# ============================================================================================

def word_lengths(sentence):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # -------------------------------------------------------------------------
    # STEP 1: Split the sentence into words using space as the delimiter
    # -------------------------------------------------------------------------
    words = sentence.split()  # ▶ split(): https://www.w3schools.com/python/ref_string_split.asp
    # 'split()' breaks the sentence wherever it sees a space
    # Example: "Hello, world!" → ['Hello,', 'world!']

    cleaned = []  # ▶ List: https://www.w3schools.com/python/python_lists.asp
    # This list will hold all cleaned words and their lengths as (word, length) tuples

    # -------------------------------------------------------------------------
    # STEP 2: Loop through each word and clean it by removing punctuation
    # -------------------------------------------------------------------------
    for word in words:  # ▶ for loop: https://www.w3schools.com/python/python_for_loops.asp

        # -------------------------------------------------------------
        # Use list comprehension + join to remove punctuation characters
        # -------------------------------------------------------------
        clean_word = ''.join(char for char in word if char not in string.punctuation)
        # ▶ join(): https://www.w3schools.com/python/ref_string_join.asp
        # ▶ string.punctuation: https://www.w3schools.com/python/ref_string_punctuation.asp
        # This filters out any symbols like ! , . ? etc. from each word

        # -----------------------------------------------------------------
        # STEP 3: Only include non-empty cleaned words in the final list
        # -----------------------------------------------------------------
        if clean_word:  # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp
            # Prevents blank/empty strings from being added (e.g., if word was just punctuation)
            cleaned.append((clean_word, len(clean_word)))  # ▶ tuple: https://www.w3schools.com/python/python_tuples.asp
            # Stores result as a tuple (word, length) for structured output

    # -------------------------------------------------------------------------
    # STEP 4: Return final cleaned word list with character lengths
    # -------------------------------------------------------------------------
    return cleaned  # ▶ return: https://www.w3schools.com/python/ref_keyword_return.asp


# ============================================================================================
# ▶ FUNCTION 3: Count total number of words
# --------------------------------------------------------------------------------------------
# Purpose:
#   Calculates the total number of words in a given sentence.
#   This is done using the `split()` method which breaks the sentence at spaces,
#   followed by the `len()` function to count the number of resulting words.
# ============================================================================================

def word_count(sentence):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ▶ split(): https://www.w3schools.com/python/ref_string_split.asp
    # The split() function breaks the sentence into a list of words using whitespace.
    # Example: "Hello world again" → ['Hello', 'world', 'again']

    # ▶ len(): https://www.w3schools.com/python/ref_func_len.asp
    # The len() function counts how many words are in the list created by split().
    # len(['Hello', 'world']) returns 2

    return len(sentence.split())  # ✅ Returns the total number of space-separated words


# ============================================================================================
# ▶ MAIN FUNCTION: Analyze Sentence with Palindrome Check
# --------------------------------------------------------------------------------------------
# Purpose:
#   This function serves as the user interface.
#   It:
#     ▪ Prompts the user for input (sentence, word, or number)
#     ▪ Checks if it is a palindrome (ignoring punctuation, spaces, and case)
#     ▪ Displays cleaned version of the sentence
#     ▪ Displays each word with its cleaned length (punctuation removed)
#     ▪ Shows the total number of words
#     ▪ Allows the user to repeat or exit
# ============================================================================================

def analyze_sentence():  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    first_run = True  # Flag to ensure title is printed only once during loop

    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        # ----------------------------------------------------------------------------
        # STEP 1: Display heading only on the first run
        # ----------------------------------------------------------------------------
        if first_run:
            print("\n============================================================")
            print("📝 PALINDROME & WORD ANALYSIS TOOL")
            print("============================================================")
            first_run = False  # Set flag to False so heading doesn't repeat

        # ----------------------------------------------------------------------------
        # STEP 2: Get input from user
        # ----------------------------------------------------------------------------
        sentence = input("\n✍️  Enter any sentence, word, or number to analyze: ").strip()
        # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
        # Removes leading/trailing whitespace to clean the input

        # ----------------------------------------------------------------------------
        # STEP 3: Call helper functions to perform analysis
        # ----------------------------------------------------------------------------
        palindrome_result = is_palindrome(sentence)     # Check if sentence is a palindrome
        word_list = word_lengths(sentence)              # Get cleaned words and their lengths
        total_words = word_count(sentence)              # Get total word count

        # ----------------------------------------------------------------------------
        # STEP 4: Display formatted results
        # ----------------------------------------------------------------------------
        print("\n============================================================")
        print(f"🔍 Is Palindrome: {'✅ Yes' if palindrome_result else '❌ No'}")
        print("------------------------------------------------------------")

        # ➕ Show cleaned sentence used in palindrome check
        cleaned_sentence = ''.join(char for char in sentence.lower() if char.isalnum())
        # ▶ lower(): https://www.w3schools.com/python/ref_string_lower.asp
        # ▶ isalnum(): https://www.w3schools.com/python/ref_string_isalnum.asp
        # Removes case, punctuation and spaces
        print(f"🧹 Cleaned Version (removed: spaces, punctuation and capitalization): {cleaned_sentence}")
        print("------------------------------------------------------------")

        # ➕ Show each word with its length after punctuation removal
        print("📏 Word Lengths (punctuation excluded):")
        for word, length in word_list:
            print(f"   - {word}: {length} characters")
        print("------------------------------------------------------------")

        # ➕ Display total number of words entered by user
        print(f"🧮 Total Words: {total_words}")
        print("============================================================\n")

        # ----------------------------------------------------------------------------
        # STEP 5: Ask the user if they want to try another input
        # ----------------------------------------------------------------------------
        again = input("🔁 Would you like to analyze another one? (y/n): ").strip().lower()
        # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
        # ▶ lower(): https://www.w3schools.com/python/ref_string_lower.asp

        if again not in ['y', 'yes']:  # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp
            print("\n------------------------------------------------------------")
            print("👋 Thank you for using the Palindrome Analyzer. Goodbye!")
            print("============================================================\n")
            break  # ▶ break: https://www.w3schools.com/python/ref_keyword_break.asp


# ============================================================================================
# ▶ RUN PROGRAM
# ============================================================================================

analyze_sentence() # Function call to launch the main converter loop


#====================
# --- CODE END --- #
#====================


# ============================================================================================
# 📚 CONSOLIDATED W3SCHOOLS REFERENCES
# ------------------------------------------------------------------------------------------------
# ▶ import keyword:               https://www.w3schools.com/python/ref_keyword_import.asp
# ▶ lower():                      https://www.w3schools.com/python/ref_string_lower.asp
# ▶ join():                       https://www.w3schools.com/python/ref_string_join.asp
# ▶ replace():                    https://www.w3schools.com/python/ref_string_replace.asp
# ▶ slicing:                      https://www.w3schools.com/python/gloss_python_string_slice.asp
# ▶ split():                      https://www.w3schools.com/python/ref_string_split.asp
# ▶ strip():                      https://www.w3schools.com/python/ref_string_strip.asp
# ▶ len():                        https://www.w3schools.com/python/ref_func_len.asp
# ▶ input():                      https://www.w3schools.com/python/python_user_input.asp
# ▶ list comprehension:           https://www.w3schools.com/python/python_lists_comprehension.asp
# ▶ while loop:                   https://www.w3schools.com/python/python_while_loops.asp
# ============================================================================================
