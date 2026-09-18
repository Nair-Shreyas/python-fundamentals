"""
Unit Converter
"""

# This approach is intended to enhance understanding and demonstrate a strong grasp of 
# the programming concepts applied throughout the code.

# ============================================================================================
# QUESTION 3: UNIT CONVERTER SYSTEM
# --------------------------------------------------------------------------------------------
# Goal:
#   Create a user-friendly program that converts between:
#     ▪ Temperature (Celsius, Fahrenheit, Kelvin)
#     ▪ Length (Meters, Feet, Inches)
#     ▪ Weight (Kilograms, Pounds)
# ============================================================================================


#======================
# --- CODE START --- #
#======================


# Welcome to the Ultimate Unit Converter!
# "Convert Anything, Anytime, Instantly!"
# The all-in-one, easy-to-use calculator for temperature, length, and weight.
# This program lets you convert values between Celsius, Fahrenheit, Kelvin, Meters, Feet, Inches, Kilograms, and Pounds.
# Just follow the on-screen menus, and you'll have your answer in seconds.
# All inputs are validated, and the interface is designed for clarity and ease of use.
# Let's get converting!


# ============================================================================================
# FUNCTION 1: get_float(prompt)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Prompt the user to enter a floating-point number (e.g., 12.5, 100.0).
#   Repeats until valid input is received using error handling.
#
# Sample Usage:
#   temp = get_float("Enter the temperature in Celsius:")
# ============================================================================================

def get_float(prompt):  # ▶ Function Definition: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Begin an infinite loop to keep asking for input
    # ------------------------------------------------------------
    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        try:  # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
            # ------------------------------------------------------------
            # STEP 2: Prompt the user for input and convert to float
            # ------------------------------------------------------------

            # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
            # Ask the user with the given prompt
            user_input = input(prompt)  # ➕ "\n" moves cursor to the next line for spacing

            # ▶ float(): https://www.w3schools.com/python/ref_func_float.asp
            # Try converting the string to a floating-point number
            value = float(user_input)

            # ------------------------------------------------------------
            # STEP 3: Return the valid float and print a blank line
            # ------------------------------------------------------------
            print()  # ➕ Add spacing for a cleaner user experience
            return value  # ✅ If successful, return the number to the calling function

        except ValueError:
            # ------------------------------------------------------------
            # STEP 4: Handle errors caused by invalid numeric input
            # ------------------------------------------------------------

            # ▶ ValueError: https://www.w3schools.com/python/gloss_python_valueerror.asp
            # Input was not convertible to float (e.g., text or symbols)
            print("\n❌ Invalid number. Please enter a valid numeric value.\n")
            # Display error and continue the loop for a retry

# ============================================================================================
# FUNCTION 2: select_option(options, prompt)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Displays a numbered list of choices and prompts the user to select one.
#   Returns the selected item from the list after validating input.
#
# Sample Usage:
#   unit = select_option(["Meters", "Feet", "Inches"], "Choose a unit:")
# ============================================================================================

def select_option(options, prompt):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Print the numbered list of options
    # ------------------------------------------------------------
    for idx, option in enumerate(options, 1):  
        # ▶ enumerate(): https://www.w3schools.com/python/ref_func_enumerate.asp
        # `enumerate()` returns both index and value
        # We're starting from 1 instead of 0 for user-friendly numbering
        print(f"{idx}. {option}")  # Display menu option
    print()  # Add spacing after the menu for better visual separation

    # ------------------------------------------------------------
    # STEP 2: Begin loop to get a valid numeric selection from the user
    # ------------------------------------------------------------
    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        try:
            # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
            # ▶ int(): https://www.w3schools.com/python/ref_func_int.asp
            # Ask user to select a number corresponding to an option
            choice = int(input(prompt))  
            print()  # Blank line after user input for aesthetics

            # ------------------------------------------------------------
            # STEP 3: Check if choice is within valid range
            # ------------------------------------------------------------
            if 1 <= choice <= len(options):  # ▶ Comparison Operators: https://www.w3schools.com/python/python_operators.asp
                return options[choice - 1]  # Return the option selected (convert index back to 0-based)

            else:
                # If number is out of range, show an error
                print(f"❌ Enter a number between 1 and {len(options)}.\n")

        except ValueError:
            # ▶ ValueError: https://www.w3schools.com/python/gloss_python_valueerror.asp
            # If user entered a non-integer (e.g., letters), catch the error
            print("❌ Invalid input. Please enter a number.\n")


# ============================================================================================
# FUNCTION 3: temp_convert(value, from_unit, to_unit)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Converts temperature between Celsius, Fahrenheit, and Kelvin using standard formulas.
#   Handles bidirectional conversion using nested if statements.
#
# Sample Usage:
#   temp_convert(100, "Celsius", "Fahrenheit") → 212.0
# ============================================================================================

def temp_convert(value, from_unit, to_unit):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Handle conversions from Celsius
    # ------------------------------------------------------------
    if from_unit == "Celsius":  # ▶ if: https://www.w3schools.com/python/python_conditions.asp
        if to_unit == "Fahrenheit":
            # Celsius to Fahrenheit: (°C × 9/5) + 32
            return value * 9 / 5 + 32  # ▶ Arithmetic: https://www.w3schools.com/python/python_operators.asp
        elif to_unit == "Kelvin":
            # Celsius to Kelvin: °C + 273.15
            return value + 273.15

    # ------------------------------------------------------------
    # STEP 2: Handle conversions from Fahrenheit
    # ------------------------------------------------------------
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            # Fahrenheit to Celsius: (°F − 32) × 5/9
            return (value - 32) * 5 / 9
        elif to_unit == "Kelvin":
            # Fahrenheit to Kelvin: ((°F − 32) × 5/9) + 273.15
            return (value - 32) * 5 / 9 + 273.15

    # ------------------------------------------------------------
    # STEP 3: Handle conversions from Kelvin
    # ------------------------------------------------------------
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            # Kelvin to Celsius: K − 273.15
            return value - 273.15
        elif to_unit == "Fahrenheit":
            # Kelvin to Fahrenheit: ((K − 273.15) × 9/5) + 32
            return (value - 273.15) * 9 / 5 + 32

    # ------------------------------------------------------------
    # STEP 4: If both units are the same, return original value
    # ------------------------------------------------------------
    return value  # No conversion needed if from_unit == to_unit


# ============================================================================================
# FUNCTION 4: length_convert(value, from_unit, to_unit)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Converts a given length value from one unit to another (Meters, Feet, Inches).
#   Uses a dictionary of base conversion factors (relative to meters).
#
# Sample Usage:
#   length_convert(10, "Meters", "Feet") → 32.8084
# ============================================================================================

def length_convert(value, from_unit, to_unit):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Define base conversion factors to meters
    # ------------------------------------------------------------
    factors = {  # ▶ Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
        "Meters": 1,         # 1 meter = 1 meter (base unit)
        "Feet": 0.3048,      # 1 foot = 0.3048 meters
        "Inches": 0.0254     # 1 inch = 0.0254 meters
    }

    # ------------------------------------------------------------
    # STEP 2: Convert input value to meters (base unit)
    # ------------------------------------------------------------
    value_in_meters = value * factors[from_unit]
    # ▶ Dictionary access: factors[from_unit]
    # ▶ Arithmetic (*): https://www.w3schools.com/python/python_operators.asp
    # Convert the input from its original unit to meters
    # Example: 10 Feet → 10 × 0.3048 = 3.048 meters

    # ------------------------------------------------------------
    # STEP 3: Convert from meters to the desired target unit
    # ------------------------------------------------------------
    result = value_in_meters / factors[to_unit]
    # ▶ Division (/): https://www.w3schools.com/python/python_operators.asp
    # Converts the intermediate meter value to the target unit
    # Example: 3.048 meters → 3.048 ÷ 0.0254 = 120 inches

    # ------------------------------------------------------------
    # STEP 4: Return the converted value
    # ------------------------------------------------------------
    return result  # Final result after both conversions


# ============================================================================================
# FUNCTION 5: weight_convert(value, from_unit, to_unit)
# --------------------------------------------------------------------------------------------
# Purpose:
#   Converts a given weight from one unit to another — specifically between:
#     ▪ Kilograms (kg)
#     ▪ Pounds (lb)
#
#   This function uses base conversion factors relative to kilograms.
#
# Example Usage:
#   weight_convert(50, "Kilograms", "Pounds") → 110.23
# ============================================================================================

def weight_convert(value, from_unit, to_unit):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Define base conversion factors relative to kilograms
    # ------------------------------------------------------------
    factors = {  # ▶ Dictionary: https://www.w3schools.com/python/python_dictionaries.asp
        "Kilograms": 1,         # 1 kilogram = 1 kg (base unit)
        "Pounds": 0.453592      # 1 pound = 0.453592 kg
    }

    # ------------------------------------------------------------
    # STEP 2: Convert the input value to kilograms
    # ------------------------------------------------------------
    value_in_kg = value * factors[from_unit]
    # ▶ Arithmetic (*): https://www.w3schools.com/python/python_operators.asp
    # Multiply the input by the conversion factor to get its value in kilograms
    # Example: 100 pounds → 100 × 0.453592 = 45.36 kg

    # ------------------------------------------------------------
    # STEP 3: Convert from kilograms to the desired target unit
    # ------------------------------------------------------------
    result = value_in_kg / factors[to_unit]
    # ▶ Arithmetic (/): https://www.w3schools.com/python/python_operators.asp
    # Divide the kg value by the target unit's factor to convert
    # Example: 45.36 kg → 45.36 ÷ 0.453592 = 100 pounds

    # ------------------------------------------------------------
    # STEP 4: Return the final converted weight
    # ------------------------------------------------------------
    return result


# ============================================================================================
# FUNCTION 6: ask_repeat()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Asks the user whether they would like to perform another conversion.
#   Accepts both full and short forms: 'yes', 'y', 'no', 'n' (case-insensitive).
#
# Keeps prompting the user until valid input is provided.
# ============================================================================================

def ask_repeat():  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------
    # STEP 1: Start a loop that continues until valid input is received
    # ------------------------------------------------------------
    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp

        # ------------------------------------------------------------
        # STEP 2: Ask the user if they want to repeat the conversion
        # ------------------------------------------------------------
        again = input("🔁 Would you like to convert another value? (y/n): ")  # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        again = again.strip().lower()  # ▶ .strip(): https://www.w3schools.com/python/ref_string_strip.asp | ▶ .lower(): https://www.w3schools.com/python/ref_string_lower.asp
        # 🧹 .strip() removes extra spaces; .lower() standardizes case for easy comparison

        print()  # Extra spacing for output clarity

        # ------------------------------------------------------------
        # STEP 3: Check if the user's response is valid
        # ------------------------------------------------------------

        if again in ['y', 'yes']:  # ▶ in operator: https://www.w3schools.com/python/ref_keyword_in.asp
            # User wants to repeat → return True to continue
            return True

        elif again in ['n', 'no']:
            # User does not want to continue → return False to stop
            return False

        else:
            # Invalid input → show error and prompt again
            print("❌ Please enter 'y' for yes or 'n' for no.\n")


# ============================================================================================
# MAIN FUNCTION 7: unit_converter()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Displays the main conversion menu and handles user input across 3 conversion types:
#   ▪ Temperature (Celsius, Fahrenheit, Kelvin)
#   ▪ Length (Meters, Feet, Inches)
#   ▪ Weight (Kilograms, Pounds)
#
#   Allows repeated conversions in a loop and exits gracefully on user command.
# ============================================================================================

# ============================================================================================
# MAIN FUNCTION 7: unit_converter()
# --------------------------------------------------------------------------------------------
# Purpose:
#   This is the main controller for the program.
#   It:
#     ▪ Shows the main category menu to the user (Temperature, Length, Weight, Exit)
#     ▪ Calls the appropriate conversion function based on user input
#     ▪ Loops back after each operation unless the user selects "Exit"
# ============================================================================================

def unit_converter():  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ========================================================================================
    # STEP 1: Begin the main program loop (keeps the program running)
    # ========================================================================================

    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        # This loop runs indefinitely until the user chooses to "Exit"
        # It allows the user to perform multiple conversions without restarting the program

        # ====================================================================================
        # STEP 2: Display welcome header and ask user what they want to convert
        # ====================================================================================

        print("\n============================================================")
        print("🌟 WELCOME TO THE ULTIMATE UNIT CONVERTER 🌟")
        print("============================================================\n")

        # Ask user for the conversion category using a dropdown-style numbered menu
        # ▶ select_option(): displays numbered menu and returns selected value from list
        # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        kind = select_option(
            ["Temperature", "Length", "Weight", "Exit"],  # List of available categories
            "---------------------------------------------\n➡️  Enter your choice (1–4): "
        )
        # User input is processed by select_option() to ensure valid menu selection

        # Output (kind) will be a string like: "Temperature", "Length", etc.

        # ====================================================================================
        # STEP 3: Exit Condition — User selected "Exit" from the menu
        # ====================================================================================

        if kind == "Exit":
            # If the selected category is "Exit", the program ends gracefully

            print("\n============================================================")
            print("👋 Thank you for using the Unit Converter. Have a great day!")
            print("============================================================\n")

            break  # ▶ break: https://www.w3schools.com/python/ref_keyword_break.asp
            # 💡 The 'break' statement exits the while loop, ending the program


        # -------------------------------------------------------------------------------------
        # 🌡️ TEMPERATURE CONVERSION BLOCK
        # -------------------------------------------------------------------------------------
        
        if kind == "Temperature":  # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp

            # ▶ List: https://www.w3schools.com/python/python_lists.asp
            units = ["Celsius", "Fahrenheit", "Kelvin"]  # Available temperature units

            # Display section title for clarity
            print("==========================================================")
            print("🌡️  TEMPERATURE CONVERSION")
            print("==========================================================")

            # -----------------------------------------------------------------
            # STEP 1: Ask user which temperature unit they are converting from
            # -----------------------------------------------------------------
            print("\nWhich temperature unit are you converting from?\n")

            from_u = select_option(  # ▶ Custom function: Shows a numbered menu
                units,
                "---------------------------------------------\n🔸 Enter your choice (1–3): "
            )

            # -----------------------------------------------------------------
            # STEP 2: Ask user the target unit they want to convert to
            # -----------------------------------------------------------------
            print("---------------------------------------------\n\nWhich unit would you like to convert to?\n")

            to_u = select_option(  # ▶ Custom function: Ensures only valid list item is selected
                units,
                "---------------------------------------------\n🔸 Enter your choice (1–3): "
            )

            # -----------------------------------------------------------------
            # STEP 3: Check if conversion is needed
            # -----------------------------------------------------------------
            if from_u == to_u:
                # ▶ Equality check: https://www.w3schools.com/python/python_operators.asp
                # If source and target units are same → skip conversion
                print("============================================================")
                print("⚠️  No conversion needed. Units are the same.")
                print("============================================================\n")

            else:
                # -----------------------------------------------------------------
                # STEP 4: Get numeric value from user and perform conversion
                # -----------------------------------------------------------------
                val = get_float(  # ▶ get_float(): Prompts user and validates float input
                    f"---------------------------------------------\n🌡️  Enter the temperature in {from_u}: "
                )  # ▶ f-string: https://www.w3schools.com/python/ref_string_format.asp

                result = temp_convert(val, from_u, to_u)  # ▶ Custom logic function for temperature

                # -----------------------------------------------------------------
                # STEP 5: Display Result
                # -----------------------------------------------------------------
                print("============================================================")
                print(f"✅ Result: {val} {from_u} = {result:.2f} {to_u}")
                print("============================================================\n")

        # -------------------------------------------------------------------------------------
        # 📏 LENGTH CONVERSION BLOCK
        # -------------------------------------------------------------------------------------

        elif kind == "Length":  # ▶ elif: https://www.w3schools.com/python/python_conditions.asp

            # ▶ List: https://www.w3schools.com/python/python_lists.asp
            units = ["Meters", "Feet", "Inches"]  # 📏 Available options for length conversion

            # Display section header for clarity
            print("==========================================================")
            print("📏 LENGTH CONVERSION")
            print("==========================================================")

            # -----------------------------------------------------------------
            # STEP 1: Ask user which length unit they are converting from
            # -----------------------------------------------------------------
            print("\nWhich length unit are you converting from?\n")

            from_u = select_option(  # ▶ Custom function with input validation
                units,
                "---------------------------------------------\n🔸 Enter your choice (1–3): "
            )

            # -----------------------------------------------------------------
            # STEP 2: Ask user the unit they wish to convert to
            # -----------------------------------------------------------------
            print("---------------------------------------------\n\nWhich unit would you like to convert to?\n")

            to_u = select_option(  # ▶ select_option(): Displays menu and returns valid choice
                units,
                "🔸---------------------------------------------\n Enter your choice (1–3): "
            )

            # -----------------------------------------------------------------
            # STEP 3: Handle identical unit selection (no conversion needed)
            # -----------------------------------------------------------------
            if from_u == to_u:  # ▶ Comparison operator: https://www.w3schools.com/python/python_operators.asp
                print("============================================================")
                print("⚠️  No conversion needed. Units are the same.")
                print("============================================================\n")

            else:
                # -----------------------------------------------------------------
                # STEP 4: Prompt user for input value and convert it
                # -----------------------------------------------------------------
                val = get_float(  # ▶ get_float(): Prompts user for numeric input
                    f"---------------------------------------------\n📐 Enter the length in {from_u}: "
                )  # ▶ f-string: https://www.w3schools.com/python/ref_string_format.asp

                result = length_convert(val, from_u, to_u)  # ▶ Custom function using conversion factors

                # -----------------------------------------------------------------
                # STEP 5: Display final result
                # -----------------------------------------------------------------
                print("============================================================")
                print(f"✅ Result: {val} {from_u} = {result:.2f} {to_u}")
                print("============================================================\n")

        # -------------------------------------------------------------------------------------
        # ⚖️ WEIGHT CONVERSION BLOCK
        # -------------------------------------------------------------------------------------

        elif kind == "Weight":  # ▶ elif statement: https://www.w3schools.com/python/python_conditions.asp

            # ▶ List: https://www.w3schools.com/python/python_lists.asp
            units = ["Kilograms", "Pounds"]  # Available units for weight conversion

            # ============================================================
            # Display section header for readability
            # ============================================================
            print("============================================================")
            print("⚖️  WEIGHT CONVERSION")
            print("============================================================")

            # -----------------------------------------------------------------
            # STEP 1: Ask user which unit they are converting from
            # -----------------------------------------------------------------
            print("\nWhich weight unit are you converting from?\n")
            from_u = select_option(  # ▶ Custom function for menu selection
                units,
                "---------------------------------------------\n🔸 Enter your choice (1–2): "
            )

            # -----------------------------------------------------------------
            # STEP 2: Ask user which unit they are converting to
            # -----------------------------------------------------------------
            print("---------------------------------------------\n\nWhich unit would you like to convert to?\n")
            to_u = select_option(  # ▶ select_option(): ensures only valid input
                units,
                "---------------------------------------------\n🔸 Enter your choice (1–2): "
            )

            # -----------------------------------------------------------------
            # STEP 3: Handle same unit selected (no conversion needed)
            # -----------------------------------------------------------------
            if from_u == to_u:  # ▶ Comparison operator: https://www.w3schools.com/python/python_operators.asp
                print("============================================================")
                print("⚠️  No conversion needed. Units are the same.")
                print("============================================================\n")

            else:
                # -----------------------------------------------------------------
                # STEP 4: Ask for weight input and perform conversion
                # -----------------------------------------------------------------
                val = get_float(  # ▶ get_float(): Gets validated float input
                    f"---------------------------------------------\n⚖️  Enter the weight in {from_u}:"
                )  # ▶ f-string: https://www.w3schools.com/python/ref_string_format.asp

                result = weight_convert(val, from_u, to_u)  # ▶ weight_convert(): custom logic with conversion factors

                # -----------------------------------------------------------------
                # STEP 5: Display conversion result
                # -----------------------------------------------------------------
                print("============================================================")
                print(f"✅ Result: {val} {from_u} = {result:.2f} {to_u}")
                print("============================================================\n")

        # ====================================================================================
        # STEP 5: Ask if user wants to convert another value
        # ====================================================================================

        if not ask_repeat():  # ▶ ask_repeat(): Prompts user to answer Yes/No to repeat
            # ▶ not operator: https://www.w3schools.com/python/python_operators.asp
            # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp
            # The function returns True if the user types 'y' or 'yes',
            # so `not True` becomes False and skips break.
            # If the function returns False (user typed 'n' or 'no'), `not False` becomes True and executes break.

            # Display a friendly farewell message in a framed layout
            print("============================================================")
            print("👋 Goodbye! Thank you for using the converter.")
            print("============================================================\n")

            break  # ▶ break keyword: https://www.w3schools.com/python/ref_keyword_break.asp
            # Exits the main while loop and ends the program


# ============================================================================================
# ▶ RUN PROGRAM
# ============================================================================================

unit_converter() # Function call to launch the main converter loop


#====================
# --- CODE END --- #
#====================


# ============================================================================================
# 📌 SAMPLE OUTPUT
# --------------------------------------------------------------------------------------------
# 🌟 WELCOME TO THE ULTIMATE UNIT CONVERTER 🌟
#
# What would you like to convert today?
#
# 1. Temperature
# 2. Length
# 3. Weight
# 4. Exit
# ➡️ Enter your choice (1–4):
#
# Which temperature unit are you converting from?
# 1. Celsius
# 2. Fahrenheit
# 3. Kelvin
# 🔸 Enter your choice (1–3):
#
# Which unit would you like to convert to?
# 1. Celsius
# 2. Fahrenheit
# 3. Kelvin
# 🔸 Enter your choice (1–3):
#
# 🌡️ Enter the temperature in Celsius:
# 100
#
# ✅ Result: 100.0 Celsius = 212.00 Fahrenheit
#
# 🔁 Would you like to convert another value? (y/n):
# n
#
# 👋 Goodbye! Thank you for using the converter.
# ============================================================================================


# ============================================================================================
# 📚 CONSOLIDATED W3SCHOOLS REFERENCES
# --------------------------------------------------------------------------------------------
# ▶ Python Functions:               https://www.w3schools.com/python/python_functions.asp
# ▶ User Input:                     https://www.w3schools.com/python/python_user_input.asp
# ▶ Try / Except:                   https://www.w3schools.com/python/python_try_except.asp
# ▶ If / Elif / Else:               https://www.w3schools.com/python/python_conditions.asp
# ▶ While Loop:                     https://www.w3schools.com/python/python_while_loops.asp
# ▶ String strip():                 https://www.w3schools.com/python/ref_string_strip.asp
# ▶ String lower():                 https://www.w3schools.com/python/ref_string_lower.asp
# ▶ String Formatting (f-strings):  https://www.w3schools.com/python/ref_string_format.asp
# ▶ List and Dictionaries:          https://www.w3schools.com/python/python_lists.asp
# ▶ Enumerate():                    https://www.w3schools.com/python/ref_func_enumerate.asp
# ▶ Arithmetic Operators:           https://www.w3schools.com/python/python_operators.asp
# ============================================================================================
