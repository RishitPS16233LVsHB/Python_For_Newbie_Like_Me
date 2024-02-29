import random

def gk_quiz():
    questions = [
        "What is the capital of France?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the chemical symbol for water?",
        "Who painted the Mona Lisa?",
        "What is the largest mammal in the world?"
    ]
    random.shuffle(questions)
    score = 0
    for q in questions:
        print(q)
        answer = input("Your answer: ")
        if answer.strip().lower() == "paris":
            score += 1
    return score

def remark(score):
    if score == 5:
        return "Outstanding"
    elif score == 4:
        return "Excellent"
    elif score == 3:
        return "Good"
    elif score == 2:
        return "Read more to score more"
    elif score == 1:
        return "Needs to take interest"
    else:
        return "General knowledge will always help you. Take it seriously."

score = gk_quiz()
print("Score:", score)
print("Remarks:", remark(score))
