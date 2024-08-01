from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    from datetime import datetime
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', current_date=current_date)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implement your authentication logic here
        if username == "admin" and password == "password":  # Example check
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    department = request.form['department']
    keywords = request.form['keywords']
    number = int(request.form['number'])

    # Process the data (dummy data for this example)
    resumes = [{'Name': f'Resume {i+1}', 'Department': department, 'Keywords': keywords} for i in range(number)]

    # Create a DataFrame
    df = pd.DataFrame(resumes)

    # Save to CSV
    output_filename = 'shortlisted_resumes.csv'
    df.to_csv(output_filename, index=False)

    return render_template('results.html', filename=output_filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
