calories_per_minute = 4.2
for minutes in range (10,31,5):
    calories_burned = minutes * calories_per_minute
    print(f"Calories burned after {minutes} minutes: {calories_burned:.4f}")