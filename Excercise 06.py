'''Brute Force Attack'''

# Password loop with a maximum of 5 attempts (correct password: 12345)

correct_password = "lilyofthevalley"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")
    attempts += 1

    if password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Access Denied.")
        