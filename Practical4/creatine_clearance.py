# Creatinine Clearance Calculator using Cockcroft-Gault Equation
# 1. Define variables: age, weight, gender, serum creatinine (Cr)
# 2. Validate input ranges:
#    - Age < 100 years
#    - Weight > 20kg and < 80kg
#    - Serum creatinine > 0 μmol/l and < 100 μmol/l
#    - Gender must be male or female (case-insensitive)
# 3. If any input is invalid, show error messages and skip calculation
# 4. If all inputs are valid, calculate CrCl using the formula:
#    CrCl = [(140 - age) × weight] / [72 × Cr]
#    For females: multiply result by 0.85
# 5. Display the final result

# Get user input
try:
    age = int(input("Enter age (years): "))
    weight = float(input("Enter weight (kg): "))
    gender = input("Enter gender (male/female): ")
    cr = float(input("Enter serum creatinine (μmol/l): "))
except ValueError:
    print("Error: Invalid input type! Age must be integer, weight and Cr must be numbers.")
    exit()

# Initialize validation flags
invalid = False
errors = ""

# Validate inputs
if age >= 100:
    invalid = True
    errors += "- Age must be less than 100\n"

if weight <= 20 or weight >= 80:
    invalid = True
    errors += "- Weight must be between 20 and 80 kg\n"

if cr <= 0 or cr >= 100:
    invalid = True
    errors += "- Creatinine must be between 0 and 100 μmol/l\n"

gender_lower = gender.lower()
if gender_lower not in ["male", "female"]:
    invalid = True
    errors += "- Gender must be male or female\n"

# Calculate or show errors
if invalid:
    print("\nInvalid inputs! Please correct the following:")
    print(errors)
else:
    # Calculate creatinine clearance
    crcl = ((140 - age) * weight) / (72 * cr)
    
    # Apply female correction
    if gender_lower == "female":
        crcl *= 0.85
    
    # Display result
    print(f"\nCreatinine Clearance (CrCl) = {crcl:.2f} ml/min")