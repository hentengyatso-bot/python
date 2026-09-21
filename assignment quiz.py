# Simple Football Quiz Game using Dictionary

# Dictionary to store questions and their answers
football_quiz = {
    "Who won the FIFA World Cup in 2018?": "France",
    "Which player has won the most Ballon d'Or awards?": "Lionel Messi",
    "What is the home stadium of Real Madrid?": "Santiago Bernabeu",
    "Which country hosted the FIFA World Cup in 2014?": "Brazil",
    "Who is known as the 'King of Football'?": "Pelé"
}

# Function to run the quiz
def run_football_quiz():
    score = 0
    for question, answer in football_quiz.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("right!")
            score += 1
        else:
            print(f"incorrect! The correct answer is {answer}.")
    
    print(f"\nYour final score is {score} out of {len(football_quiz)}.")

# Start the quiz
run_football_quiz()
