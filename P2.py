# Simple Quiz App


quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["1. Paris", "2. Berlin", "3. Rome", "4. Madrid"],
        "answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
        "answer": 2
    },
    {
        "question": "What is 5 + 3?",
        "options": ["1. 5", "2. 8", "3. 10", "4. 15"],
        "answer": 2
    }
]

def show_menu():
    print("\n--- Quiz App Menu ---")
    print("1. Start Quiz")
    print("2. Exit")


def start_quiz():
    print("\n--- Starting the Quiz ---")
    score = 0
    total_questions = len(quiz_questions)

    for i, question in enumerate(quiz_questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        try:
            user_answer = int(input("Enter your choice (1-4): "))
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Wrong! The correct answer is:", question['options'][question['answer'] - 1])
        except ValueError:
            print("Invalid input! Skipping this question.")

    print("\n--- Quiz Completed ---")
    print(f"Your score: {score}/{total_questions}")
    print("Thank you for playing!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-2): ")
        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Exiting the Quiz App. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
