'''Primitive Quiz'''

# Simple Asian Capitals Quiz

# Dictionary of Asian countries and their capitals
quiz_questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Switzerland": "Bern"
}

# Loop through each question
for country, correct_capital in quiz_questions.items():
    # Ask the question
    user_answer = input(f"What is the capital of {country}? ")

    # Compare answers, ignoring capitalization and extra spaces
    if user_answer.strip().lower() == correct_capital.lower():
        print("✅ Correct!\n")
    else:
        print(f"❌ Wrong. The correct answer is {correct_capital}.\n")