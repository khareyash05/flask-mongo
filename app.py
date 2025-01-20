from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import collections.abc


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['studentsdb']
students_collection = db['students']

@app.route('/students', methods=['GET'])
def get_students():
    students = list(students_collection.find({}, {'_id': 0}))
    return jsonify(students)

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    student = students_collection.find_one({'student_id': student_id}, {'_id': 0})
    return jsonify(student)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
