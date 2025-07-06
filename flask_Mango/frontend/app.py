from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests

BACKEND_URL = 'http://127.0.0.1:5000'  # URL of the backend service

app = Flask(__name__)
@app.route('/')
def home():
    day_of_week = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', dayis=day_of_week, CurrentTime=current_time)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL +'/submit', json=form_data)
    # print(form_data)  # Print the form data to the console for debugging


    return "submitted successfully! for form data " 

if __name__ == '__main__':
        app.run(host='127.0.0.1',port=4000,debug=True)

