import random

# List of words with English to Spanish translations
words = [
    {"english": "the", "spanish": "el"},
    {"english": "of/from", "spanish": "de"},
    {"english": "that/which", "spanish": "que"},
    {"english": "and", "spanish": "y"},
    {"english": "to/at", "spanish": "a"},
    {"english": "in/on", "spanish": "en"},
    {"english": "a/an", "spanish": "un"},
    {"english": "to be", "spanish": "ser"},
    {"english": "oneself/itself", "spanish": "se"},
    {"english": "no/not", "spanish": "no"},
    {"english": "to have", "spanish": "haber"},
    {"english": "for/by", "spanish": "por"},
    {"english": "with", "spanish": "con"},
    {"english": "his/her/your/their", "spanish": "su"},
    {"english": "for/to", "spanish": "para"},
    {"english": "like/as", "spanish": "como"},
    {"english": "to be", "spanish": "estar"},
    {"english": "to have", "spanish": "tener"},
    {"english": "him/her/you", "spanish": "le"},
    {"english": "it/him/you", "spanish": "lo"},
]


def quiz_user(words):
    """Function to quiz the user with shuffled English-to-Spanish flashcards."""
    random.shuffle(
        words)  # Shuffle the list of words to randomize the quiz order
    score = 0  # Initialize user's score

    for word in words:
        # Ask the user for the Spanish translation of the given English word
        print(f"What is the Spanish translation of '{word['english']}'?")
        # Take user input and normalize it
        user_answer = input("Your answer: ").strip().lower()

        # Allow the user to exit the quiz early
        if user_answer == "exit":
            print("\nYou are now exiting the game.")
            break

        # Get the correct Spanish word
        correct_answer = word['spanish'].lower()

        # Check if the user's answer matches the correct translation
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1  # Increase score for correct answer
        else:
            print(f"Wrong! The correct answer is '{word['spanish']}'.\n")

    # Display final score after quiz ends
    print(f"\nQuiz complete! Your final score: {score}/{len(words)}")


def main():
    """Main function to start the flashcard quiz."""
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")  # Wait for the user to get ready
    quiz_user(words)  # Start the quiz


# Run the program only if this file is executed directly (not imported)
if __name__ == "__main__":
    main()
