import random
questions = 112

def generate_question():
    question_number = random.randint(1, questions)

    with open(f'questions/{question_number}.txt', 'r') as q:
        question = q.readline()
        answer = q.readline()
        print(question)
        print(answer)
    
    return question_number, question, answer