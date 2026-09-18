"""
Student Record System
"""

# This approach is intended to enhance understanding and demonstrate a strong grasp of 
# the programming concepts applied throughout the code.

# ============================================================================================
# QUESTION 2: STUDENT RECORD SYSTEM (File Handling)
# --------------------------------------------------------------------------------------------
# Goal:
#   Create a student record manager using Python that allows users to:
#     ▪ Add new students
#     ▪ Update student marks
#     ▪ Delete student records
#     ▪ Search for a student
#
#   Data is stored and managed using a plain text file ("students.txt").
#
# This version is written in full tutorial-style with W3Schools references and detailed comments.
# ============================================================================================


#======================
# --- CODE START --- #
#======================


# ============================================================================================
# FUNCTION 1: add_student()
# --------------------------------------------------------------------------------------------
# Purpose:
#   This function is responsible for adding a new student record to a file named "students.txt".
#   It ensures the student ID is unique (no duplicate entries).
#   Data is saved in CSV format (ID, Name, Course, Marks) — one student per line.
#
# File operations used:
#   - File reading (to check for duplicates)
#   - File appending (to add new data)  
#
# Concepts used: input(), open(), strip(), startswith(), try/except, write()
# ============================================================================================

def add_student():

    # Section header for better output visibility
    print("\n============================================================")
    print("➕ ADD NEW STUDENT")
    print("------------------------------------------------------------")

    # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
    # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
    student_id = input("🆔 Enter Student ID (e.g., S1023): ").strip()
    # Prompt the user for a unique student ID
    # Use .strip() to clean accidental spaces from the input
    # Example input: " S1023 " → becomes "S1023"

    name = input("👤 Enter Student Name: ").strip()
    # Ask for the student's full name

    course = input("📘 Enter Course Name: ").strip()
    # Ask for the course the student is enrolled in

    marks = input("🎯 Enter Marks (0–100): ").strip()
    # Ask for the student's marks — string for now (can be validated later)
    
    if not marks.isdigit() or not (0 <= int(marks) <= 100):
     print("❌ Marks must be a number between 0 and 100.")
     return
    # Validate that marks is a digit and in 0–100 range

    # -----------------------------------------------------------------------------------------
    # Check for duplicate ID before saving new student
    # -----------------------------------------------------------------------------------------

    # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
    try:
        # ▶ open() in read mode: https://www.w3schools.com/python/ref_func_open.asp
        # ▶ with keyword: https://www.w3schools.com/python/ref_keyword_with.asp
        with open("students.txt", "r") as file:
            for line in file:
                # ▶ startswith(): https://www.w3schools.com/python/ref_string_startswith.asp
                if line.startswith(student_id + ","):
                    # If any line begins with the same student ID, it's a duplicate
                    print("\n----------------------------------------------------")
                    print("❌ Student ID already exists. Cannot add duplicate.")
                    print("----------------------------------------------------")
                    return  # Exit the function without adding anything

    except FileNotFoundError:
        # ▶ FileNotFoundError: https://www.w3schools.com/python/ref_exceptions.asp
        # This means the file doesn't exist yet (e.g., first time running the program)
        # We skip checking and allow the new student to be added

        pass  # Safe to proceed

    # -----------------------------------------------------------------------------------------
    # Append the new student record to the file
    # -----------------------------------------------------------------------------------------

    # ▶ open() in append mode: https://www.w3schools.com/python/ref_func_open.asp
    with open("students.txt", "a") as file:
        # ▶ write(): https://www.w3schools.com/python/ref_file_write.asp
        file.write(f"{student_id},{name},{course},{marks}\n")
        # Format: ID,Name,Course,Marks — separated by commas
        # Example line: S1023,Arjun,Data Analytics,87

        # Confirmation message
        print("\n-------------------------------")
        print("✅ Student added successfully.")
        print("-------------------------------")


# ============================================================================================
# FUNCTION 2: update_marks()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Updates the marks of an existing student based on ID.
#   Reads each line of the file, modifies the matching record, and rewrites the updated data.
#
# File operations used:
#   - File reading to find and edit records
#   - File writing to overwrite modified content
#
# Concepts used: input(), open(), strip(), split(), join(), list, startswith(), try/except
# ============================================================================================

def update_marks():

    # Print section heading for output clarity
    print("\n============================================================")
    print("✏️  UPDATE STUDENT MARKS")
    print("------------------------------------------------------------")

    # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
    # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
    student_id = input("🆔 Enter Student ID to update: ").strip()
    # Ask user which student’s marks to change
    # .strip() ensures no accidental space messes up the searcha

    new_marks = input("🎯 Enter New Marks (0–100): ").strip()
    # Ask the user for the updated mark

    if not new_marks.isdigit() or not (0 <= int(new_marks) <= 100):
        print("❌ Marks must be a number between 0 and 100.")
        return
    # Validate that marks is a digit and in 0–100 range    

    updated = False  # ▶ Boolean: https://www.w3schools.com/python/python_booleans.asp
    # Used to check if a matching student record was found

    records = []  # ▶ List: https://www.w3schools.com/python/python_lists.asp
    # Used to store all lines (records) temporarily while we modify one

    # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
    try:
        # ▶ open(): https://www.w3schools.com/python/ref_func_open.asp
        with open("students.txt", "r") as file:
            for line in file:
                # ▶ startswith(): https://www.w3schools.com/python/ref_string_startswith.asp
                if line.startswith(student_id + ","):
                    # Match found — student exists in file

                    parts = line.strip().split(",")  
                    # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
                    # ▶ split(): https://www.w3schools.com/python/ref_string_split.asp
                    # Strip newline and split into [ID, Name, Course, Marks]

                    parts[3] = new_marks  
                    # Replace the old marks with the new input (index 3 is marks)

                    records.append(",".join(parts) + "\n")  
                    # ▶ join(): https://www.w3schools.com/python/ref_string_join.asp
                    # Rebuild the updated record as a comma-separated string

                    updated = True  # Set flag to true as record was modified

                else:
                    records.append(line)
                    # Keep all other lines as-is

    except FileNotFoundError:
        # ▶ FileNotFoundError: https://www.w3schools.com/python/ref_exceptions.asp
        # Happens if the student file doesn't exist yet

        print("\n----------------------------")
        print("❌ Student file not found.")
        print("----------------------------")
        return  # Exit early as no update can happen

    # ▶ if/else: https://www.w3schools.com/python/python_conditions.asp
    if updated:
        # If a record was found and updated

        with open("students.txt", "w") as file:
            # ▶ writelines(): https://www.w3schools.com/python/ref_file_writelines.asp
            file.writelines(records)
            # Overwrite the file with the updated list of student records

        print("\n-------------------------------")
        print("✅ Marks updated successfully.")
        print("-------------------------------")

    else:
        # No matching student ID found
        print("\n--------------------------")
        print("❌ Student ID not found.")
        print("--------------------------")


# ============================================================================================
# FUNCTION 3: delete_student()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Deletes a student record by removing the matching line from the file.
#   Reads all lines into memory, excludes the target, then rewrites the updated list.
# ============================================================================================

def delete_student():
    print("\n============================================================")
    print("🗑️  DELETE STUDENT RECORD")  # 📢 Section header for user interaction
    print("------------------------------------------------------------")

    # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
    # Prompt the user to enter the student ID of the record to be deleted
    student_id = input("🆔 Enter Student ID to delete: ").strip()
    # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
    # .strip() is used to clean up any accidental spaces before or after the input

    # ▶ Boolean: https://www.w3schools.com/python/python_booleans.asp
    deleted = False  # A flag that becomes True if the record is found and removed

    # ▶ List: https://www.w3schools.com/python/python_lists.asp
    records = []  # Temporary list to hold student records that should be kept

    try:
        # ▶ open(): https://www.w3schools.com/python/ref_func_open.asp
        # Open the student file in read mode to check each line
        with open("students.txt", "r") as file:
            for line in file:
                # ▶ startswith(): https://www.w3schools.com/python/ref_string_startswith.asp
                # Check if the line starts with the entered student ID
                if not line.startswith(student_id + ","):
                    # If the ID does NOT match, keep the record
                    records.append(line)
                else:
                    # If the ID matches, we skip adding it (effectively deleting it)
                    deleted = True

    except FileNotFoundError:
        # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
        # If the file doesn't exist yet, display an error message and exit function
        print("\n----------------------------")
        print("❌ Student file not found.")
        print("----------------------------")
        return  # Exit the function early

    # If a deletion took place, rewrite the file without the deleted record
    if deleted:
        # ▶ open(): https://www.w3schools.com/python/ref_func_open.asp
        # Open the file in write mode to overwrite with the updated data
        with open("students.txt", "w") as file:
            # ▶ writelines(): https://www.w3schools.com/python/ref_file_writelines.asp
            file.writelines(records)  # 📝 Save all remaining records back to file

        print("\n-------------------------------")
        print("✅ Student deleted successfully.")
        print("-------------------------------")
    else:
        # If the student ID was not found in the file, notify the user
        print("\n-------------------------")
        print("❌ Student ID not found.")
        print("-------------------------")


# ============================================================================================
# FUNCTION 4: search_student()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Searches the file line by line for a student ID and displays their record.
#   Uses a simple sequential scan on the text file.
# ============================================================================================

def search_student():
    print("\n============================================================")
    print("🔎 SEARCH STUDENT RECORD")  # Title Header
    print("------------------------------------------------------------")

    # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
    student_id = input("🆔 Enter Student ID to search: ").strip()  
    # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
    # Removes spaces before/after input for consistency

    # ▶ Boolean: https://www.w3schools.com/python/python_booleans.asp
    found = False  # Flag to track whether student is found

    try:
        # ▶ open(): https://www.w3schools.com/python/ref_func_open.asp
        with open("students.txt", "r") as file:
            for line in file:
                # ▶ startswith(): https://www.w3schools.com/python/ref_string_startswith.asp
                if line.startswith(student_id + ","):
                    # ▶ split(): https://www.w3schools.com/python/ref_string_split.asp
                    parts = line.strip().split(",")  # Split record into fields

                    # Nicely formatted, labeled output for better clarity
                    print("\n------------------------------------")
                    print("✅ Student Found:")
                    print("------------------------------------")
                    print("   🆔 ID      :", parts[0])
                    print("   👤 Name    :", parts[1])
                    print("   📘 Course  :", parts[2])
                    print("   🎯 Marks   :", parts[3])
                    print("------------------------------------")
                    found = True
                    break  # No need to continue scanning file

    except FileNotFoundError:
        # ▶ try/except: https://www.w3schools.com/python/python_try_except.asp
        print("\n-----------------------------")
        print("❌ Student file not found.")
        print("-----------------------------")
        return  # Exit function early if file does not exist

    if not found:
        # Display message if no matching student was located
        print("\n---------------------------")
        print("❌ Student ID not found.")
        print("---------------------------")


# ============================================================================================
# MAIN FUNCTION 5: student_system()
# --------------------------------------------------------------------------------------------
# Purpose:
#   Displays the menu interface and lets the user perform various operations.
#   Repeats indefinitely until the user chooses to quit.
# ============================================================================================

def student_system():
    while True:  
        # ▶ while loop: https://www.w3schools.com/python/python_while_loops.asp
        # The loop allows users to perform multiple operations without restarting the program

        print("\n============================================================")
        print("📚 STUDENT RECORD SYSTEM")  # 📢 Main system header
        print("============================================================")
        print("1. ➕ Add Student")         # Option 1: Add a new record
        print("2. ✏️  Update Marks")       # Option 2: Modify existing record
        print("3. 🗑️  Delete Student")      # Option 3: Remove a record
        print("4. 🔎 Search Student")      # Option 4: Find a record
        print("5. ❌ Quit")               # Option 5: Exit the program
        print("------------------------------------------------------------")

        # ▶ input(): https://www.w3schools.com/python/python_user_input.asp
        # ▶ strip(): https://www.w3schools.com/python/ref_string_strip.asp
        choice = input("🔷 Enter your choice (1–5): ").strip()
        # Prompt user for input, strip() ensures clean formatting

        # ▶ if/elif/else: https://www.w3schools.com/python/python_conditions.asp
        # Route the user's input to the corresponding function
        if choice == "1":
            add_student()         # Call function to add a new student
        elif choice == "2":
            update_marks()        # Call function to update marks
        elif choice == "3":
            delete_student()      # Call function to delete record
        elif choice == "4":
            search_student()      # Call function to search by student ID
        elif choice == "5":
            print("\n👋 Exiting the Student Record System. Thank you!\n")
            break  # ▶ break: https://www.w3schools.com/python/ref_keyword_break.asp
            # Exit the loop and terminate the program
        else:
            # If the input is not between 1–5, show error
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

        # Message printed after each operation to allow continued use
        print("\n---------------------------------------------")
        print("💡 You can now perform another action below.")
        print("---------------------------------------------")


# ============================================================================================
# ▶ RUN PROGRAM
# ============================================================================================

student_system() # ▶ Function call


#====================
# --- CODE END --- #
#====================


# ============================================================================================
# 📚 CONSOLIDATED W3SCHOOLS REFERENCES
# --------------------------------------------------------------------------------------------
# ▶ input():                        https://www.w3schools.com/python/python_user_input.asp
# ▶ open(), write(), writelines(): https://www.w3schools.com/python/python_file_handling.asp
# ▶ strip():                        https://www.w3schools.com/python/ref_string_strip.asp
# ▶ split():                        https://www.w3schools.com/python/ref_string_split.asp
# ▶ join():                         https://www.w3schools.com/python/ref_string_join.asp
# ▶ if/elif/else:                   https://www.w3schools.com/python/python_conditions.asp
# ▶ while loop:                     https://www.w3schools.com/python/python_while_loops.asp
# ▶ Lists:                          https://www.w3schools.com/python/python_lists.asp
# ▶ break keyword:                  https://www.w3schools.com/python/ref_keyword_break.asp
# ============================================================================================
