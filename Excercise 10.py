'''Is it even?'''

def check_even_odd(number):
    """Determine if a number is even or odd."""
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."


def main():
    """Main function to get user input and display result."""
    try:
        num = int(input("Enter an integer: "))
        result = check_even_odd(num)
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Run the program
if __name__ == "__main__":
    main()
