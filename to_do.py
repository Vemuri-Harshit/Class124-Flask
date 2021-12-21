from flask import Flask,jsonify, request;

tasks = [
    {
        'id': 1,
        'title': 'Read',
        'description': 'Complete your portion before exams',
        'completed': False,
    },

    {
        'id': 2,
        'title': 'PLay Games',
        'description': 'Try to play for 3 hours',
        'completed': False,
    }    
];

app = Flask('__name__');

@app.route('/')
def getTask():
    return jsonify({
        'data': tasks
    });

@app.route('/addata', methods=['POST'])
def addData():
    if not request.json:
        return jsonify({'status': 'error'});  
    
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'completed': False
   }
    tasks.append(task);

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run();