from flask import Flask, json, jsonify, request
import flask, json
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

todos = [
    {"label":"My first task", "done": False},
    {"label":"My second task", "done": False}
    ]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    convert_to_dict = json.loads(request_body)
    todos.append(convert_to_dict)
    print("Incoming request with the following body", convert_to_dict)
    return flask.jsonify(todos)
    
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[1]
    print("This is the position to delete: ",position)
    return flask.jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)