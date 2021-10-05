import os
number = int(input('How many questions are there CURRENTLY?: '))

def clear():
  # Check if Operating System is Mac and Linux or Windows
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # Else Operating System is Windows (os.name = nt)
    _ = os.system('cls')

while True:
    clear()
    number += 1
    print(f'Question {number}')
    question = input('Question: ')
    answer = input('Answer: ')

    with open(f'questions/{number}.txt', 'w') as q:
        q.write(f'{question}\n{answer}')
