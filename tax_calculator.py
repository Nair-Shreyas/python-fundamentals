"""
Tax Calculator
"""

# This approach is intended to enhance understanding and demonstrate a strong grasp of 
# the programming concepts applied throughout the code.

# ===========================================================================================
# QUESTION 1: TAX CALCULATION SYSTEM
# -------------------------------------------------------------------------------------------
# Goal:
#   Create a Python program that calculates taxes (USC, PRSI, Income Tax),
#   applies applicable tax credits, and outputs a clean tax liability statement.
#   Based on real-world Irish tax slabs.
#   This version is written with full tutorial-style comments and explanations.
# ===========================================================================================


#======================
# --- CODE START --- #
#======================


# --- Importing required libraries ---
# No external libraries are used in this program.
# This decision is intentional to demonstrate knowledge of core Python functions and ensure portability.


# ===========================================================================================
# FUNCTION 1: calculate_usc(income)
# -------------------------------------------------------------------------------------------
# Purpose:
#   Calculate Universal Social Charge (USC) using slab-based progressive taxation.
#   The tax rates apply to slices of income, not the entire amount.
#
# Why slabs and 'if-elif-else'?
#   USC is progressive: each slab applies only to a certain portion of income.
#   We use if-elif-else to apply the correct calculation path based on income amount.
# ===========================================================================================

def calculate_usc(income):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp
    usc = 0  # ▶ Variable declaration: https://www.w3schools.com/python/python_variables.asp
    # Start with USC as zero — we will add values progressively based on income slabs.

    if income <= 12012:  # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp
        # If the total income is less than or equal to €12,012, only the first slab (0.5%) applies.
        usc = income * 0.005  # ▶ Arithmetic operator (*): https://www.w3schools.com/python/python_operators.asp
        # Multiply the entire income by 0.5% to get the USC for this case.

    elif income <= 27382:  # ▶ elif statement: https://www.w3schools.com/python/python_conditions.asp
        # If the income is more than €12,012 but less than or equal to €27,382, two slabs apply:
        # - 0.5% on the first €12,012
        # - 2% on the income between €12,013 and €27,382
        usc = 12012 * 0.005 + (income - 12012) * 0.02  # ▶ Arithmetic operators (+, -, *): https://www.w3schools.com/python/python_operators.asp
        # First slab: 0.5% on €12,012
        # Second slab: 2% on the amount exceeding €12,012

    elif income <= 70044:  # ▶ elif statement: https://www.w3schools.com/python/python_conditions.asp
        # If the income is more than €27,382 but less than or equal to €70,044, three slabs apply:
        # - 0.5% on the first €12,012
        # - 2% on the next €15,370
        # - 3% on the income between €27,383 and €70,044
        usc = 12012 * 0.005 + 15370 * 0.02 + (income - 27382) * 0.03
        # We directly use 15,370 for the second slab and subtract €27,382 to get the range for the third.

    else:  # ▶ else statement: https://www.w3schools.com/python/python_conditions.asp
        # If the income is more than €70,044, all four slabs apply:
        # - 0.5% on the first €12,012
        # - 2% on the next €15,370
        # - 3% on the next €42,662
        # - 8% on the remaining income above €70,044
        usc = 12012 * 0.005 + 15370 * 0.02 + 42662 * 0.03 + (income - 70044) * 0.08
        # Each slab is calculated and summed up sequentially — last part handles income over €70,044

    return round(usc, 2)  # ▶ round(): https://www.w3schools.com/python/ref_func_round.asp
    # Round the final USC to 2 decimal places for currency formatting before returning the result


# ===========================================================================================
# FUNCTION 2: calculate_prsi(income)
# -------------------------------------------------------------------------------------------
# Purpose:
#   PRSI is a flat 4.1% tax on total income. No slabs or thresholds.
#   Simply multiply the gross income by 0.041.
# ===========================================================================================

def calculate_prsi(income):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp
    # This function calculates PRSI (Pay Related Social Insurance)
    # PRSI is a fixed-rate tax, meaning it does not use slabs like USC or Income Tax.
    # The flat rate is 4.1%, applied directly to the entire gross income.

    return round(income * 0.041, 2)  # ▶ Arithmetic + round(): https://www.w3schools.com/python/ref_func_round.asp
    # Multiply the gross income by 0.041 to calculate 4.1% PRSI.
    # round(..., 2) is used to ensure the returned value is formatted to two decimal places,
    # which is essential when working with monetary values like tax.
    # Example: If income = 50,000 → PRSI = 50,000 * 0.041 = €2,050.00


# ===========================================================================================
# FUNCTION 3: calculate_income_tax(income)
# -------------------------------------------------------------------------------------------
# Purpose:
#   Calculates Income Tax using two slabs:
#   ▪ 20% on first €44,000
#   ▪ 40% on the amount above €44,000
#
# Strategy:
#   Use if-statement to check whether income crosses the slab threshold.
# ===========================================================================================

def calculate_income_tax(income):  # ▶ Function: https://www.w3schools.com/python/python_functions.asp
    # This function calculates the Income Tax using a dual-slab tax system.
    # In Ireland, income tax is applied as:
    # - 20% on income up to €44,000
    # - 40% on income exceeding €44,000

    if income <= 44000:  # ▶ if statement: https://www.w3schools.com/python/python_conditions.asp
        # This condition checks whether the income falls entirely within the lower tax bracket.
        # If true, the entire income is taxed at 20%.
        return round(income * 0.20, 2)  # ▶ Arithmetic + rounding: https://www.w3schools.com/python/ref_func_round.asp
        # Multiply income by 0.20 to get 20% tax
        # Example: income = €35,000 → Tax = €35,000 × 0.20 = €7,000.00
        # round(..., 2) is used to return the result as a currency-friendly two-decimal number

    else:  # ▶ else statement: https://www.w3schools.com/python/python_conditions.asp
        # This block handles income above €44,000.
        # In this case, the income is split into two parts:
        # - €44,000 is taxed at 20%
        # - The remaining amount (income - 44,000) is taxed at 40%
        return round(44000 * 0.20 + (income - 44000) * 0.40, 2)  # ▶ Arithmetic + round(): https://www.w3schools.com/python/python_operators.asp
        # Breakdown:
        #   First €44,000 → 44000 × 0.20 = €8,800
        #   Remaining amount → (income - 44000) × 0.40
        # Example: income = €60,000
        #   → €8,800 + (€16,000 × 0.40 = €6,400) = €15,200.00
        # round(..., 2) ensures the result is rounded properly to 2 decimal places


# ===========================================================================================
# FUNCTION 4: calculate_tax_credits(...)
# -------------------------------------------------------------------------------------------
# Purpose:
#   Sums all applicable tax credits:
#   ▪ Marital status: €4,000 (married) / €2,000 (single)
#   ▪ Employee Credit: €2,000
#   ▪ Rent Credit: €1,000
#   ▪ Dependent Credit: €305 per child (max 2)
#
# Why use min(dependents, 2)?
#   To cap dependent credit at 2 children.
# ===========================================================================================

def calculate_tax_credits(married, employee_credit, rent_credit, dependents):  # ▶ Function with parameters
    # This function calculates total tax credits based on:
    #    - marital status
    #    - employee credit
    #    - rent credit
    #    - number of dependents (max 2)
    # These credits reduce the total tax liability (but do not result in a refund if tax is zero).

    total_credit = 0  # ▶ Variable initialization
    # Start with a base credit of 0. We'll add to this depending on the user's inputs.

    if married.lower() == 'yes':  # ▶ String .lower(): https://www.w3schools.com/python/ref_string_lower.asp
        # Normalize input to lowercase to handle inputs like "Yes", "YES", "yes"
        # If user is married, they receive a tax credit of €4,000
        total_credit += 4000  # ▶ Assignment operator +=: https://www.w3schools.com/python/python_operators.asp
    else:
        # If user is single, they receive a tax credit of €2,000
        total_credit += 2000

    if employee_credit.lower() == 'yes':
        # Add €2,000 if the person qualifies for the employee credit
        total_credit += 2000

    if rent_credit.lower() == 'yes':
        # Add €1,000 if the person qualifies for the rent credit
        total_credit += 1000

    total_credit += min(dependents, 2) * 305  # ▶ min(): https://www.w3schools.com/python/ref_func_min.asp
    # Each dependent qualifies for €305 credit
    # But a maximum of **2 dependents** are allowed for credit, hence we use min(dependents, 2)
    # Example: 0 → €0, 1 → €305, 2 → €610, 3 or more → capped at €610

    return total_credit
    # Return the total tax credit after all applicable additions
    # This amount will later be subtracted from the total tax to get final tax liability


# ===========================================================================================
# FUNCTION 5: get_yes_no(prompt)
# -------------------------------------------------------------------------------------------
# Purpose:
#   Validates user input to accept only "yes" or "no" (case-insensitive).
#   Keeps prompting until valid input is entered.
# ===========================================================================================

def get_yes_no(prompt):  # ▶ Function definition
    #    This function ensures that the user only enters "yes" or "no" (case-insensitive).
    #    It keeps prompting the user until they provide a valid response.
    #    This is important to avoid errors and make the program more user-friendly.

    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        # This loop runs infinitely until a valid input ("yes" or "no") is given by the user.

        response = input(prompt + " (Yes / No): ").strip().lower()  
        # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        # Prompt the user with a custom question like "Are you married? (Yes / No):"
        # .strip() removes any leading/trailing spaces (e.g., " yes " becomes "yes")
        # .lower() converts input to lowercase so that "Yes", "YES", or "yes" are all treated the same

        if response in ['yes', 'no']:  # ▶ in keyword: https://www.w3schools.com/python/ref_keyword_in.asp
            # If the input matches one of the two acceptable answers, return it
            return response  # Passes back a clean 'yes' or 'no' to the calling function
        else:
            # Input was not valid — show an error message and repeat the loop
            print("❌ Please enter 'Yes' or 'No' only.")
            # This message helps guide the user back to correct input format


# ===========================================================================================
# FUNCTION 6: get_positive_float(prompt)
# -------------------------------------------------------------------------------------------
# Purpose:
#   Accepts numeric input for income. Strips commas (like "50,000") and validates positivity.
#   Uses try/except to prevent crashes from invalid types (e.g., text).
# ===========================================================================================

def get_positive_float(prompt):
    #    This function is used to safely accept a positive floating-point number from the user.
    #    It allows comma-separated input like "50,000", removes the comma, checks if the value
    #    is numeric and greater than 0. If not, it keeps prompting until a valid number is entered.

    while True:
        # This loop ensures the user cannot proceed until a valid positive float is entered.
        # It repeats on any error or invalid input.

        try:  # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
            # Begin error-handling block to catch any non-numeric input (e.g., letters or symbols)

            value = input(prompt).replace(",", "")  
            # ▶ replace(): https://www.w3schools.com/python/ref_string_replace.asp
            # Prompt the user to enter a number
            # .replace(",", "") removes commas so inputs like "50,000" are converted to "50000"

            value = float(value)  # ▶ float(): https://www.w3schools.com/python/ref_func_float.asp
            # Convert the cleaned string input into a floating-point number
            # If input is invalid (e.g., "abc"), this line will raise a ValueError and jump to except

            if value <= 0:
                # Income or tax values must be greater than 0 — no zero or negative allowed
                print("❌ Enter a positive number greater than 0.")
                # Error message guiding the user

            else:
                return value
                # Valid positive float is returned to the calling function

        except ValueError:
            # This block handles any input that cannot be converted to float (e.g., "abc", "--", etc.)
            print("❌ Invalid format. Example: 50000 or 50,000.")
            # Gives the user a correct input example and repeats the loop


# ===========================================================================================
# FUNCTION 7: get_dependents()
# -------------------------------------------------------------------------------------------
# Purpose:
#   Prompts the user to enter a number of dependents: only 0, 1, or 2 allowed.
#   Enforces input type as integer.
# ===========================================================================================

def get_dependents():
    # Purpose:
    # This function collects the number of dependents from the user,
    # but only allows valid values: 0, 1, or 2 (as per credit policy).
    # It keeps prompting the user until a valid integer is entered.

    while True:
        # Loop runs continuously until valid input is received
        # Ensures user cannot move forward without giving a valid response

        try:
            # Start a try block to catch invalid (non-integer) inputs

            value = int(input("Enter number of dependents (0, 1, or 2): "))  
            # ▶ int(): https://www.w3schools.com/python/ref_func_int.asp
            # Prompt user to enter number of dependents
            # Converts the string input to an integer
            # If the user types letters or decimals, this line will raise ValueError

            if value in [0, 1, 2]:  # ▶ list & in operator: https://www.w3schools.com/python/ref_keyword_in.asp
                # Accept only 0, 1, or 2 as valid options
                return value  # 🎯 Return the valid dependent count to calling function

            else:
                # If the input is outside the allowed range
                print("❌ You can only claim up to 2 dependents.")
                # Tell the user what the valid options are

        except ValueError:
            # 🧯 Handles cases where input could not be converted to integer
            print("❌ Please enter a whole number (0, 1, or 2).")
            # Reminds the user to enter a number — not letters or symbols


# ===========================================================================================
# MAIN FUNCTION 8: generate_sol()
# -------------------------------------------------------------------------------------------
# Purpose:
#   This is the entry point of the program.
#   Collects all inputs, calls calculator functions, and prints formatted tax breakdown.
# ===========================================================================================

def generate_sol():
    # This is the main function — it orchestrates the full tax calculation process.
    # It collects user input, performs all calculations, and prints the results in a readable format.

    print("\n================================================================================")
    print("  🧾 Statement of Liability Calculator")
    print("================================================================================\n")
    # Decorative print lines used to create a clear title and structure in the terminal

    # ------------------------------------------------------------------------
    # STEP 1: Collect user input — ensure no empty responses using validation
    # ------------------------------------------------------------------------

    while True:
        emp_id = input("🔷 Enter Employee ID (e.g., E1023): ").strip()
        # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        # Prompt user to enter their unique employee ID
        # .strip() removes any accidental spaces around the input
        if emp_id != "":
            break  # Valid (non-empty) input accepted
        else:
            print("❌ Employee ID cannot be empty. Please try again.")
            # Error message if input was blank

    while True:
        name = input("🔷 Enter Full Employee Name: ").strip()
        # 📥 Prompt for name input, cleaned with .strip()
        if name != "":
            break  # Valid name entered
        else:
            print("❌ Name cannot be empty. Please enter a valid name.")
            # Prompt again if name is left blank

    gross_income = get_positive_float("🔷 Enter Annual Gross Income in Euros (e.g., 50,000): ")
    # Ask the user to enter gross income — validated separately to ensure it’s a positive float

    print("\n🔸 Answer the following questions with Yes or No:")
    # Transition into the next section asking eligibility questions for tax credits

    married = get_yes_no("Are you married?")
    # Determines marital credit eligibility: €4,000 if yes, €2,000 if no

    employee_credit = get_yes_no("Do you qualify for Employee Credit?")
    # Adds €2,000 credit if eligible

    rent_credit = get_yes_no("Do you qualify for Rent Credit?")
    # Adds €1,000 credit if eligible

    dependents = get_dependents()
    # Each dependent adds €305 credit (up to max of 2 children)

    # ----------------------------------------------------------------
    # STEP 2: Calculate all taxes and credits using modular functions
    # ----------------------------------------------------------------

    usc = calculate_usc(gross_income)  # Universal Social Charge
    prsi = calculate_prsi(gross_income)  # PRSI: flat 4.1%
    income_tax = calculate_income_tax(gross_income)  # Income Tax (dual slab)
    tax_credits = calculate_tax_credits(married, employee_credit, rent_credit, dependents)  # Total credits

    final_tax_liability = round(usc + prsi + income_tax - tax_credits, 2)
    # Total tax = sum of taxes - tax credits
    # round(..., 2) ensures proper currency formatting

    net_income = round(gross_income - final_tax_liability, 2)
    # Final income after tax deductions

    # ------------------------------------------------------------
    # STEP 3: Display the results in a clear, formatted statement
    # ------------------------------------------------------------

    print("\n================================================================================")
    print("                     📄 Statement of Liability")
    print("================================================================================\n")

    print(f"👤 Employee Name:       {name}")
    print(f"🆔 Employee ID:         {emp_id}")
    print(f"💰 Gross Income:        €{gross_income:,.2f}")  
    # ▶ format(): https://www.w3schools.com/python/ref_string_format.asp
    # Gross income is formatted with comma separator and 2 decimal places

    print("\n📌 Tax Deductions")
    print(f"   ▪ USC Deduction:     €{usc:,.2f}")
    print(f"   ▪ PRSI Deduction:    €{prsi:,.2f}")
    print(f"   ▪ Income Tax:        €{income_tax:,.2f}")
    # Displays tax amounts per category in a clean bullet format

    print(f"\n🎁 Total Tax Credits Applied: €{tax_credits:,.2f}")
    # Displays total credits granted

    print(f"\n🧮 Final Tax Liability:  €{final_tax_liability:,.2f}")
    # Final tax after credits are applied

    print(f"🏦 Net Income:           €{net_income:,.2f}")
    # Take-home pay after all deductions

    print("\n✅ Calculation complete. Thank you for using the calculator.\n")
    # Friendly closing message


# ===========================================================================================
# MAIN PROGRAM LOOP: Repeat Calculator Option
# -------------------------------------------------------------------------------------------
# Purpose:
#   Allows the user to run the tax calculator multiple times without restarting the program.
#   After completing one tax return, the user is asked whether they'd like to calculate another.
#   The program exits gracefully if the user chooses "No" (or "N").
# ===========================================================================================

while True:
    # Start an infinite loop to allow the program to be reused multiple times
    # The loop will only break when the user says they do not want to run it again

    generate_sol()  
    # ▶ Function call
    # Run one full tax calculation — handles input, tax computation, and output formatting

    again = get_yes_no("Would you like to calculate another tax return?")
    # Prompt the user to decide if they want to calculate another return
    # ▶ get_yes_no(): returns 'yes' or 'no' after accepting input like "yes", "no", "y", "n"
    # This input is stored in the variable `again`

    if again == 'no':
        # Check if the user chose to exit
        print("\n👋 Exiting the calculator. Goodbye!")
        # Friendly exit message before terminating
        break  # ▶ break keyword: https://www.w3schools.com/python/ref_keyword_break.asp
        # Break exits the loop — no further calculations will run


#====================
# --- CODE END --- #
#====================


# ===========================================================================================
# 📌 SAMPLE OUTPUT
# -------------------------------------------------------------------------------------------
# 👤 Employee Name:       Martin Cox
# 🆔 Employee ID:         E1234
# 💰 Gross Income:        €50,000.00
#
# 📌 Tax Deductions
#    ▪ USC Deduction:     €1,046.00
#    ▪ PRSI Deduction:    €2,050.00
#    ▪ Income Tax:        €11,200.00
#
# 🎁 Total Tax Credits Applied: €5,305.00
# 🧮 Final Tax Liability:        €8,991.00
# 🏦 Net Income:                 €41,009.00
# ===========================================================================================

# ===========================================================================================
# 📚 CONSOLIDATED W3SCHOOLS REFERENCES
# -------------------------------------------------------------------------------------------
# ▶ Python Functions:             https://www.w3schools.com/python/python_functions.asp
# ▶ Variables:                    https://www.w3schools.com/python/python_variables.asp
# ▶ if/elif/else Conditions:      https://www.w3schools.com/python/python_conditions.asp
# ▶ String Methods (.lower):      https://www.w3schools.com/python/ref_string_lower.asp
# ▶ min() Function:               https://www.w3schools.com/python/ref_func_min.asp
# ▶ round() Function:             https://www.w3schools.com/python/ref_func_round.asp
# ▶ input():                      https://www.w3schools.com/python/python_user_input.asp
# ▶ float():                      https://www.w3schools.com/python/ref_func_float.asp
# ▶ int():                        https://www.w3schools.com/python/ref_func_int.asp
# ▶ format():                     https://www.w3schools.com/python/ref_string_format.asp
# ▶ try/except:                   https://www.w3schools.com/python/python_try_except.asp
# ▶ replace():                    https://www.w3schools.com/python/ref_string_replace.asp
# ▶ Operators:                    https://www.w3schools.com/python/python_operators.asp
# ▶ while loop:                   https://www.w3schools.com/python/python_while_loops.asp
# ▶ in keyword:                   https://www.w3schools.com/python/ref_keyword_in.asp
# ▶ Comments in Python:           https://www.w3schools.com/python/python_comments.asp
# ===========================================================================================
