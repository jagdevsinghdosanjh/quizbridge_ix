from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
import sys

# Set base path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Configure Flask with absolute paths
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, '..', 'templates'),
    static_folder=os.path.join(BASE_DIR, '..', 'static')
)

app.secret_key = 'quizbridgeix_secret_key'  # Use environment variable in production

# Load quiz from JSON file
def load_quiz(unit):
    try:
        quiz_path = os.path.join(BASE_DIR, '..', 'quizzes', f'{unit}.json')
        with open(quiz_path, encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not load quiz '{unit}': {e}", file=sys.stderr)
        return None

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz/<unit>', methods=['GET', 'POST'])
def quiz(unit):
    quiz_data = load_quiz(unit)
    if not quiz_data:
        return "Quiz not found", 404

    if request.method == 'POST':
        answers = request.form.to_dict()
        session['responses'] = answers
        return redirect(url_for('results', unit=unit))

    return render_template('quiz.html', quiz=quiz_data, unit=unit)

@app.route('/results/<unit>')
def results(unit):
    quiz_data = load_quiz(unit)
    user_answers = session.get('responses', {})
    score = 0
    total = len(quiz_data['quiz'])
    results = []

    for idx, question in enumerate(quiz_data['quiz']):
        q_key = f'q{idx}'
        correct = str(question['answer'][0])
        user_ans = user_answers.get(q_key)
        is_correct = user_ans == correct
        if is_correct:
            score += 1
        results.append({
            'question': question['question'],
            'selected': question['options'][int(user_ans)] if user_ans else "Not Answered",
            'correct': question['options'][int(correct)],
            'explanation': question['explanation'],
            'is_correct': is_correct
        })

    return render_template('results.html', results=results, score=score, total=total, unit=unit)

@app.route('/dashboard')
def dashboard():
    quiz_scores = [
        {"unit": "AI Reflection", "score": 12, "total": 15},
        {"unit": "Data Literacy", "score": 10, "total": 15},
        {"unit": "Math for AI", "score": 9, "total": 15},
        {"unit": "Generative AI", "score": 13, "total": 15},
        {"unit": "Intro to Python", "score": 14, "total": 15}
    ]

    labels = [q["unit"] for q in quiz_scores]
    scores = [q["score"] for q in quiz_scores]
    totals = [q["total"] for q in quiz_scores]

    return render_template("dashboard.html", labels=labels, scores=scores, totals=totals)

@app.errorhandler(Exception)
def handle_error(e):
    print(f"[SERVER ERROR] {e}", file=sys.stderr)
    return "Internal Server Error", 500
