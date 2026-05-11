class FoodItem:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def calculate_daily_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0

    # Sum all nutrition data
    for item in food_list:
        total_cal += item.calories
        total_pro += item.protein
        total_carbs += item.carbs
        total_fat += item.fat

    # Display summary
    print("\nDAILY NUTRITION SUMMARY")
    print(f"Total Calories: {total_cal} kcal")
    print(f"Total Protein:  {total_pro} g")
    print(f"Total Carbs:    {total_carbs} g")
    print(f"Total Fat:      {total_fat} g")

    # Warning system
    warning_triggered = False
    if total_cal > 2500:
        print("WARNING: Calories exceed 2500 kcal limit!")
        warning_triggered = True
    if total_fat > 90:
        print("WARNING: Fat exceeds 90 g limit!")
        warning_triggered = True
    if not warning_triggered:
        print("STATUS: Nutrition within recommended limits.")

    return total_cal, total_pro, total_carbs, total_fat

# Example usage
if __name__ == "__main__":
    # Create food instances
    apple = FoodItem("Apple", 60, 0.3, 15, 0.5)
    rice = FoodItem("Rice", 130, 2.7, 28, 0.3)
    chicken = FoodItem("Chicken Breast", 165, 31, 0, 3.6)
    cake = FoodItem("Cake", 400, 4, 50, 20)

    # Daily food list
    daily_food = [apple, rice, chicken, cake, cake]  # Adding multiple cakes to trigger warnings

    # Run calculation
    calculate_daily_nutrition(daily_food)