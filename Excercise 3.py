'''Biography'''

# Get user's full name (can include first and last names)
name = input("Enter your full name: ")

# Get user's hometown (can include city, province, country)
hometown = input("Enter your hometown: ")

# Get user's age with validation
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)  # Try converting to an integer
        break
    except ValueError:
        print("Invalid input. Please enter a number for age.")

# Store information in a dictionary
bio = {
    "Name": name,
    "Hometown": hometown,
    "Age": age
}

# Print all values using a single print() statement, with newlines
print(f"\n--- Biography ---\nName: {bio['Name']}\nHometown: {bio['Hometown']}\nAge: {bio['Age']}")