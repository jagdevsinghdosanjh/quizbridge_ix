import os

QUIZ_FOLDER = 'quizzes'
unit = 'unit1_reflection'
path = os.path.join(QUIZ_FOLDER, f'{unit}.json')

print("Absolute path:", os.path.abspath(path))
print("Exists:", os.path.exists(path))
