from flask import Flask, render_template, request
from question import generate_question

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/suggest')
def suggest():
    return render_template('suggest.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    number, question, answer = generate_question()
    print(question, answer)
    return render_template('question.html', number=number, question=question, answer=answer)

@app.route('/result', methods=['POST'])
def check_question():
    if request.method == 'POST':
        question = request.form.get('question')
        user_answer = request.form.get('user_answer')
        answer = request.form.get('answer')
        if user_answer.lower() == answer.lower():
            return render_template('result.html', user_answer=user_answer, answer=answer, correct=True)
        else:
            return render_template('result.html', question=question, user_answer=user_answer, answer=answer, correct=False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)