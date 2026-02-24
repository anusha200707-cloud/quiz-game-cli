quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A"
    },
    {
        "question": "Who is the current Prime Minister of India?",
        "options": ["A) Narendra Modi", "B) Rahul Gandhi", "C) Amit Shah", "D) Arvind Kejriwal"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Saturn", "C) Jupiter", "D) Uranus"],
        "answer": "C"
    },
    {
        "question": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["A) J.K. Rowling", "B) Harper Lee", "C) Jane Austen", "D) Charles Dickens"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Ag", "B) Au", "C) Hg", "D) Pb"],
        "answer": "B"
    }
]

def run_quiz():
    score = 0
    for i, q in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
    print(f"\nQuiz finished! Your final score is {score}/{len(quiz_questions)}")

def main():
    while True:
        print("\nWelcome to the Quiz System!")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            run_quiz()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()