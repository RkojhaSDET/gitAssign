from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os   
import pymongo  # Assuming you want to use pymongo for MongoDB operations

load_dotenv()  # Load environment variables from .env file

mongo_uri = os.getenv('MONGO_URI')
if not mongo_uri:
    raise ValueError("MONGO_URI not found in environment variables. Please check your .env file.")

try:
    client = pymongo.MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Force connection on a request as the connect=True parameter of MongoClient seems to be useless here
except Exception as e:
    raise ConnectionError(f"Could not connect to MongoDB: {e}")

db = client.test_db  # database name
collection = db.test_collection  #  collection name


app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.get_json()
    collection.insert_one(form_data)
    # print(form_data)  # Print the form data to the console for debugging
    return "submitted successfully! for form data "

@app.route('/api')
def view():
    data = collection.find()
    data = list(data)  # Convert cursor to list for easier manipulation
    for item in data:
        print(item)
        del item['_id']  # Remove the MongoDB ObjectId from the output
    data = [dict(item) for item in data]  # Convert each item to a dictionary
    return data

if __name__ == '__main__':
        app.run(host='127.0.0.1',port=5000,debug=True)

