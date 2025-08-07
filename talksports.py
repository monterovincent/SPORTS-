
def ask_question(question, options, correct_answer):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if answer < 1 or answer > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    if options[answer - 1].lower() == correct_answer.lower():
        print("✅ Correct!") 
        
        return 1
    else:
        print(f"❌ Incorrect! The correct answer is: {correct_answer}")
        return 0


def run_quiz():
    print("🎯 Welcome to the World Sports Quiz!\n")
    score = 0

    questions = [
        {
            "question": "Which country has won the most FIFA World Cups?",
            "options": ["Germany", "Argentina", "Brazil", "Italy"],
            "answer": "Brazil"
        },
        {
            "question": "Who holds the record for the most Olympic gold medals?",
            "options": ["Usain Bolt", "Michael Phelps", "Simone Biles", "Carl Lewis"],
            "answer": "Michael Phelps"
        },
        {
            "question": "In which sport is the Davis Cup awarded?",
            "options": ["Tennis", "Cricket", "Hockey", "Golf"],
            "answer": "Tennis"
        },
        {
            "question": "Which country hosts the Tour de France?",
            "options": ["Italy", "USA", "France", "Spain"],
            "answer": "France"
        },
        {
            "question": "What is the national sport of Japan?",
            "options": ["Karate", "Baseball", "Sumo Wrestling", "Judo"],
            "answer": "Sumo Wrestling"
        }
    ]

    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])

    print("\n🎉 Quiz Completed!")
    print(f"Your final score: {score} out of {len(questions)}")
    if score == len(questions):
        print("🏆 Excellent! You're a sports genius!")
    elif score >= 3:
        print("👏 Good job!")
    else:
        print("💡 Keep learning about sports!")

# Start the quiz
if __name__ == "__main__":
    run_quiz()