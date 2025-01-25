from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response

@app.route('/students')
def get_students():
    results = []
    pref = request.args.get('pref')
    if pref:
        for student in data:
            if student['pref'] == pref:
                results.append(student)
        return jsonify(results)
    return jsonify(data)



@app.route('/students/<id>')
def get_student(id):
  for student in data: 
    if student['id'] == id: 
      return jsonify(student)

# Exercise 1
@app.route('/stats')
def get_stats():
    results = {'Chicken': 0, 
               'Computer Science (Major)': 0, 
               'Computer Science (Special)': 0, 
               'Fish': 0, 
               'Information Technology (Major)':0,
               'Information Technology (Special)': 0,
               'Vegetable': 0,}
    
    # pref = request.args.get('pref')
    
    for students in data:
        if students['pref'] == "Chicken":
            results['Chicken'] += 1
        
        if students['programme'] == 'Computer Science (Major)':
            results['Computer Science (Major)'] += 1
            
        if students['programme'] == 'Computer Science (Special)':
            results['Computer Science (Special)'] += 1
            
        if students['pref'] == "Fish":
            results['Fish'] += 1
            
        if students['programme'] == 'Information Technology (Major)':
            results['Information Technology (Major)'] += 1
            
        if students['programme'] == 'Information Technology (Special)':
            results['Information Technology (Special)'] += 1
            
        if students['pref'] == 'Vegetable':
            results['Vegetable'] += 1
            

   
    return results


# Exercise 2

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))
       

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    return str(int(a) - int(b))
        
@app.route('/multiply/<a>/<b>')
def mult(a, b):
    return str(int(a) * int(b))

@app.route('/divide/<a>/<b>')
def divide(a, b):
    return str(int(a) / int(b))
    
app.run(host='0.0.0.0', port=8080, debug=True)


