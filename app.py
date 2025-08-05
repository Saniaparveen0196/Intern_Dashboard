from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_data():
    with open("data.json") as file:
        return json.load(file)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    data = load_data()
    # Dummy recent donation history
    donations = [
        {"date": "2025-08-01", "amount": 2500},
        {"date": "2025-07-28", "amount": 3000},
        {"date": "2025-07-25", "amount": 2000}
    ]
    return render_template('dashboard.html', data=data, donations=donations)

@app.route('/profile')
def profile():
    data = load_data()
    return render_template('profile.html', data=data)

@app.route('/leaderboard')
def leaderboard():
    leaderboard_data = [
        {"name": "Sania", "donations": 12500},
        {"name": "Amit", "donations": 11500},
        {"name": "Neha", "donations": 10800},
        {"name": "Ravi", "donations": 9900}
    ]
    return render_template('leaderboard.html', leaderboard=leaderboard_data)

@app.route('/api/data')
def api_data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(debug=True)

