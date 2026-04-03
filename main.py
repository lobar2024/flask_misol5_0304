from flask import Flask, render_template

app = Flask(__name__)

@app.route('/grade')
def grade_page():
    students = [
        {"name": "Ali", "score": 95},
        {"name": "Vali", "score": 72},
        {"name": "Guli", "score": 58},
        {"name": "Zafar", "score": 88},
        {"name": "Nilufar", "score": 45},
    ]
    return render_template('grade.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
