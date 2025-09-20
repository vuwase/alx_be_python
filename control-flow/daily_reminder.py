# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case to handle priority
match priority:
    case "high":
        base_text = f"'{task}' is a high priority task"
    case "medium":
        base_text = f"'{task}' is a medium priority task"
    case "low":
        base_text = f"'{task}' is a low priority task"
    case _:
        base_text = f"'{task}' has an unspecified priority"

# Check if task is time-bound and print directly
if time_bound == "yes":
    print(f"Reminder: {base_text} that requires immediate attention today!")
else:
    print(f"Note: {base_text}. Consider completing it when you have free time.")

