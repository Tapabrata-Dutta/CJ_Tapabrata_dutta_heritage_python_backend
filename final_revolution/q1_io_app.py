"""
q1_io_app.py
A console-based mini-application containing two features:
1) BMI Calculator - Calculates BMI from height and weight and provides the category.
2) Age Finder - Calculates current age based on the birth year.
"""

import datetime

def get_float_input(prompt):
    """Prompt the user for a float value, validating the input recursively or iteratively."""
    while True:
        try:
            val_str = input(prompt).strip()
            if not val_str:
                print("Error: Input cannot be empty. Please enter a valid number.")
                continue
            val = float(val_str)
            if val <= 0:
                print("Error: Input must be a positive number. Please try again.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid decimal number.")

def get_int_input(prompt, min_val=1800, max_val=None):
    """Prompt the user for an integer value within a specific range, validating input."""
    if max_val is None:
        max_val = datetime.date.today().year
        
    while True:
        try:
            val_str = input(prompt).strip()
            if not val_str:
                print("Error: Input cannot be empty. Please enter a valid year.")
                continue
            val = int(val_str)
            if not (min_val <= val <= max_val):
                print(f"Error: Please enter a year between {min_val} and {max_val}.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer year.")

def calculate_bmi():
    """Calculates BMI and prints category (Underweight/Normal/Overweight/Obese)."""
    print("\n--- BMI Calculator ---")
    weight = get_float_input("Enter your weight in kg (e.g., 70): ")
    height = get_float_input("Enter your height in meters (e.g., 1.75): ")
    
    # BMI formula: weight / height^2
    bmi = weight / (height ** 2)
    
    # Category determination logic
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"
        
    # Formatted f-string output
    print(f"\n[Result] Your BMI is: {bmi:.2f}")
    print(f"[Category] {category}")

def find_age():
    """Calculates current age from birth year."""
    print("\n--- Age Finder ---")
    current_year = datetime.date.today().year
    birth_year = get_int_input(f"Enter your birth year (1800-{current_year}): ", min_val=1800, max_val=current_year)
    
    age = current_year - birth_year
    
    # Formatted f-string output
    print(f"\n[Result] Current Year: {current_year}")
    print(f"[Result] Your calculated age is: {age} years old.")

def main():
    """Main menu loop for the mini-application."""
    while True:
        print("\n==============================")
        print("    Console-Based Mini App    ")
        print("==============================")
        print("1. BMI Calculator")
        print("2. Age Finder")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            calculate_bmi()
        elif choice == '2':
            find_age()
        elif choice == '3':
            print("\nThank you for using the application! Goodbye.")
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()


"""""
tapabratadutta@TAPABRATAs-MacBook-Air Intern_program % python3 /Users/tapabratadutta/Intern_program/final_revolution/q1_io_app.py

==============================
    Console-Based Mini App    
==============================
1. BMI Calculator
2. Age Finder
3. Exit
Select an option (1-3): 1

--- BMI Calculator ---
Enter your weight in kg (e.g., 70): 65
Enter your height in meters (e.g., 1.75): 1.76

[Result] Your BMI is: 20.98
[Category] Normal

==============================
    Console-Based Mini App    
==============================
1. BMI Calculator
2. Age Finder
3. Exit
Select an option (1-3): 
"""