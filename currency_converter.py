"""
Currency Converter
"""

# This approach is intended to enhance understanding and demonstrate a strong grasp of 
# the programming concepts applied throughout the code.

# =========================================================================================================================
# QUESTION 5: Currency Converter Using forex-python
# -------------------------------------------------------------------------------------------------------------------------
# Goal:
#   Create a live currency converter using forex-python package, validating inputs and handling errors.
# =========================================================================================================================


#======================
# --- CODE START --- #
#======================


# ============================================================================================
# STEP 1: Import the required module or auto-install if missing
# --------------------------------------------------------------------------------------------
#     forex-python is an external Python package that provides currency exchange data
#     If it’s not already installed, this block ensures that it gets installed automatically.
#     This prevents runtime errors and makes the code user-friendly.
# ============================================================================================

try:
    # ▶ import: https://www.w3schools.com/python/ref_keyword_import.asp
    # Attempt to import the required module from forex-python package
    from forex_python.converter import CurrencyRates

except ModuleNotFoundError:
    # ▶ ModuleNotFoundError: https://www.w3schools.com/python/ref_exceptions.asp
    # This block executes if the module is not installed on the user's machine

    import subprocess  # ▶ subprocess: https://docs.python.org/3/library/subprocess.html
    import sys  # ▶ sys: https://www.w3schools.com/python/ref_sys.asp

    print("📦 'forex-python' not found. Installing now...")
    
    # ▶ subprocess.check_call(): Runs pip install via terminal
    # This command runs pip through the current Python executable to install the package
    subprocess.check_call([sys.executable, "-m", "pip", "install", "forex-python"])

    # After installation, re-import the CurrencyRates class
    from forex_python.converter import CurrencyRates


# ============================================================================================
# STEP 2: Define the Currency Converter function
# --------------------------------------------------------------------------------------------
#     This function uses forex-python to convert currencies in real-time using live exchange rates.
#     It repeatedly prompts the user for conversion until they decide to exit.
# ============================================================================================

def currency_converter():  # ▶ Function: https://www.w3schools.com/python/python_functions.asp

    # ------------------------------------------------------------------------
    # STEP 2.1: Welcome message
    # ------------------------------------------------------------------------
    print("\n============================================================")
    print("💱 WELCOME TO THE LIVE CURRENCY CONVERTER")
    print("============================================================")

    # ------------------------------------------------------------------------
    # STEP 2.2: Create an object of the CurrencyRates class from forex-python
    # ------------------------------------------------------------------------
    c = CurrencyRates()  # ▶ Class Instantiation: https://www.w3schools.com/python/python_classes.asp
    # This object lets us access real-time exchange rates and perform currency conversion

    # ------------------------------------------------------------------------
    # STEP 2.3: Begin an infinite loop to allow multiple conversions
    # ------------------------------------------------------------------------
    while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        # The user will remain in this loop until they choose to stop


        # ============================================================================================
        # STEP 3: GET USER INPUT FOR CURRENCIES AND AMOUNT
        # --------------------------------------------------------------------------------------------
        #     This section collects the base currency, target currency, and amount to convert.
        #     It includes input validation for each field to ensure correct formatting.
        # ============================================================================================

        # ------------------------------------------------------------------------
        # STEP 3.1: Get and validate BASE currency code (e.g., USD)
        # ------------------------------------------------------------------------
        while True:
            base_currency = input("\n🔹 Enter BASE currency code (e.g., USD): ").strip().upper()
            # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
            # ▶ .strip(): https://www.w3schools.com/python/ref_string_strip.asp
            # ▶ .upper(): https://www.w3schools.com/python/ref_string_upper.asp

            # Ensure it's a 3-letter alphabetic currency code
            if len(base_currency) != 3 or not base_currency.isalpha():  
                # ▶ isalpha(): https://www.w3schools.com/python/ref_string_isalpha.asp
                print("❌ Invalid input! Please enter a 3-letter alphabetic code like USD or INR.\n")
                continue
            break  # Valid input, exit the loop

        # ------------------------------------------------------------------------
        # STEP 3.2: Get and validate TARGET currency code (e.g., EUR)
        # ------------------------------------------------------------------------
        while True:
            target_currency = input("🔸 Enter TARGET currency code (e.g., EUR): ").strip().upper()

            if len(target_currency) != 3 or not target_currency.isalpha():
                print("❌ Invalid input! Please enter a 3-letter alphabetic code like EUR or JPY.\n")
                continue
            break  # Valid input, exit the loop

        # ------------------------------------------------------------------------
        # STEP 3.3: Get and validate amount to convert
        # ------------------------------------------------------------------------
        while True:
            try:
                amount = float(input("💰 Enter amount to convert: "))  
                # ▶ float(): https://www.w3schools.com/python/ref_func_float.asp

                if amount <= 0:
                    print("❌ Amount must be greater than zero.\n")
                    continue  # Reject zero or negative input
                break  # Valid amount, exit the loop

            except ValueError:
                # ▶ ValueError: https://www.w3schools.com/python/python_try_except.asp
                print("❌ Please enter a valid numeric amount like 100 or 250.50.\n")


        # ============================================================================================
        # STEP 4: Perform Currency Conversion and Display Result
        # --------------------------------------------------------------------------------------------
        #     This section performs the actual currency conversion using forex-python methods.
        #     It also handles exceptions like invalid currency codes or internet issues.
        # ============================================================================================

        try:
            # ------------------------------------------------------------------------
            # STEP 4.1: Get the live exchange rate using forex-python
            # ------------------------------------------------------------------------
            rate = c.get_rate(base_currency, target_currency)
            # This returns the live conversion rate from base to target
            # ▶ forex-python get_rate(): https://forex-python.readthedocs.io/en/latest/#forex_python.converter.CurrencyRates.get_rate

            # ------------------------------------------------------------------------
            # STEP 4.2: Convert the entered amount
            # ------------------------------------------------------------------------
            converted_amount = c.convert(base_currency, target_currency, amount)
            # This uses the same library to do the full conversion
            # ▶ forex-python convert(): https://forex-python.readthedocs.io/en/latest/#forex_python.converter.CurrencyRates.convert

            # ------------------------------------------------------------------------
            # STEP 4.3: Display the conversion result
            # ------------------------------------------------------------------------
            print("\n============================================================")
            print(f"🔁 Exchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")
            # ▶ f-string formatting: https://www.w3schools.com/python/ref_string_format.asp

            print(f"✅ Converted Amount: {amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")
            print("============================================================\n")

        except Exception as e:
            # ▶ Exception handling: https://www.w3schools.com/python/python_try_except.asp
            # Handles unexpected errors like:
            # - Typo in currency codes
            # - Internet issues
            # - API changes or unavailability

            print("❌ An error occurred while fetching conversion data.")
            print("🛠️  Possible causes:")
            print("   - Invalid currency codes not supported by forex-python")
            print("   - Internet connectivity issues")
            print(f"   - Error: {str(e)}\n")  # ▶ str(): https://www.w3schools.com/python/ref_func_str.asp


        # ============================================================================================
        # STEP 5: Ask If the User Wants to Perform Another Conversion
        # --------------------------------------------------------------------------------------------
        #     After completing one conversion, we give the user the option to perform another.
        #     Input is case-insensitive and flexible: accepts 'y', 'yes', 'n', 'no'.
        # ============================================================================================

        while True:  # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
            again = input("🔁 Would you like to convert another amount? (y/n): ").strip().lower()
            # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
            # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
            # ▶ lower(): https://www.w3schools.com/python/ref_string_lower.asp
            # This makes input lowercase and removes extra spaces so it works for 'Yes', ' YES ', etc.

            if again in ['y', 'yes']:
                # User wants to continue — break out of this inner loop and restart outer loop
                break

            elif again in ['n', 'no']:
                # User does not want to continue — print exit message and return from function
                print("\n👋 Thank you for using the Currency Converter. Goodbye!")
                return  # ▶ return: https://www.w3schools.com/python/ref_keyword_return.asp

            else:
                # Invalid input handling
                print("❌ Please enter 'y' for yes or 'n' for no.\n")


# ============================================================================================
# ▶ RUN PROGRAM
# ============================================================================================

currency_converter() # ▶ Function call to execute the currency converter logic


#====================
# --- CODE END --- #
#====================


# ============================================================================================
# 📌 SAMPLE OUTPUT
# --------------------------------------------------------------------------------------------
# 💱 WELCOME TO THE LIVE CURRENCY CONVERTER
#
# 🔹 Enter BASE currency code (e.g., USD): usd
# 🔸 Enter TARGET currency code (e.g., EUR): eur
# 💰 Enter amount to convert: 100
#
# 🔁 Exchange Rate: 1 USD = 0.9200 EUR
# ✅ Converted Amount: 100.00 USD = 92.00 EUR
#
# 🔁 Would you like to convert another amount? (y/n): n
# 👋 Thank you for using the Currency Converter. Goodbye!
# ============================================================================================

# ============================================================================================
# 📚 CONSOLIDATED W3SCHOOLS REFERENCES
# --------------------------------------------------------------------------------------------
# ▶ try/except:              https://www.w3schools.com/python/python_try_except.asp
# ▶ import:                  https://www.w3schools.com/python/ref_keyword_import.asp
# ▶ functions:               https://www.w3schools.com/python/python_functions.asp
# ▶ float():                 https://www.w3schools.com/python/ref_func_float.asp
# ▶ isalpha():               https://www.w3schools.com/python/ref_string_isalpha.asp
# ▶ string formatting:       https://www.w3schools.com/python/ref_string_format.asp
# ▶ while loop:              https://www.w3schools.com/python/python_while_loops.asp
# ▶ input():                 https://www.w3schools.com/python/python_user_input.asp
# ============================================================================================
