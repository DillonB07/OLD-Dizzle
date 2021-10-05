from question import questions

number = 0
with open('question_log.txt', 'w') as l:
    for question in range(questions):
        number += 1
        print(number)

        with open(f'questions/{number}.txt', 'r') as q:
            question = q.readline()
            answer = q.readline()
            print(question)
            l.write(question)
            print(answer)
            l.write(answer + '\n')
