# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user to enter a number of days and calculates
    the future date after adding those days to current_date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date(current_date)

