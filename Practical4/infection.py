# 1. Initialize variables:
#    - total_students = 91 (total class size)
#    - infected = initial number of infected students
#    - growth_rate = rate of infection spread (as decimal)
#    - day = 1 (counter for days)
# 2. Display initial infected count for day 1
# 3. While infected < total_students:
#    - Calculate new infections = infected * growth_rate
#    - Update infected = infected + new infections
#    - Increment day counter
#    - Display infected count for current day
# 4. Display total days taken to infect all students

# Initialize variables
total_students = 91  # Total number of students in IBI1 class
infected = 5         # Initial number of infected students (starting point)
growth_rate = 0.4    # 40% growth rate (as decimal: 40/100 = 0.4)
day = 1            # Day counter starting at day 1

# Display initial infection status
print(f"Day {day}: {infected} students infected")

# Loop until all students are infected
while infected < total_students:
    # Calculate new infections for the next day
    # New infections = current infected * growth rate
    new_infections = infected * growth_rate
    
    # Update total infected count
    infected = infected + new_infections
    
    # Move to next day
    day = day + 1
    
    # Display current day's infection count
    # Note: Python may show decimal values like 7.0 - this is normal at this stage
    print(f"Day {day}: {int(infected)} students infected")

# After loop ends, display summary
print(f"\nIt took {day} days to infect all {total_students} students in the IBI1 class.")