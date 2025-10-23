'''Days of the Month'''

# Dictionary mapping month numbers to number of days
month_days = {
    1: 31,
    2: 28,  # February will be updated if it's a leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask user for the month number
try:
    month = int(input("Enter the month number (1-12): "))

    if month < 1 or month > 12:
        print("❌ Invalid month. Please enter a number from 1 to 12.")
    else:
        # If month is February, check for leap year
        if month == 2:
            leap_input = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_input == "yes":
                days = 29
            else:
                days = 28
        else:
            days = month_days[month]
        
        print(f"✅ The number of days in month {month} is: {days}")
except ValueError:
    print("❌ Invalid input. Please enter a number.")