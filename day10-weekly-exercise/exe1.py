def ask_question(q, choices, correct_letter):
    print(q)
    for choice in choices:
        print(choice)
    while True:
        answer = input("Your answer (A, B, or C): ").strip().upper()
        if answer in ['A', 'B', 'C']:
            break
        else:
            print("Invalid input. Please enter A, B, or C.")
    if answer == correct_letter:
        print("Correct!\n")
        return True
    else:
        # Show the correct answer and its text
        idx = ['A', 'B', 'C'].index(correct_letter)
        print(f"The correct answer is {correct_letter}. {choices[idx]}\n")
        return False

def main():
    questions = [
        "Which piece is worth the most in chess?",
        "What is the only move in chess where two pieces move at once?",
        "Which color moves first in chess?",
        "What is it called when the king cannot escape capture?",
        "How many squares are there on a chessboard?"
    ]

    choices = [
        ["A. Queen", "B. Rook", "C. Bishop"],
        ["A. En passant", "B. Castling", "C. Promotion"],
        ["A. Black", "B. White", "C. Either"],
        ["A. Check", "B. Checkmate", "C. Stalemate"],
        ["A. 64", "B. 32", "C. 100"]
    ]

    correct_answers = ['A', 'B', 'B', 'B', 'A']

    num_correct = 0
    num_incorrect = 0

    for i in range(len(questions)):
        if ask_question(f"Q{i+1}: {questions[i]}", choices[i], correct_answers[i]):
            num_correct += 1
        else:
            num_incorrect += 1

    print(f"You got {num_correct} correct and {num_incorrect} incorrect answers.")

if __name__ == "__main__":
    main()