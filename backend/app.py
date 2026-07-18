import flask
import flask_cors
import model
app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/dad-joke-score', methods = ['POST'])
def score():
    data = flask.request.get_json()
    setup = data.get('setup', '')
    punchline = data.get('punchline', '')
    result = model.score_joke(setup, punchline)
    return flask.jsonify({'score' : result})

# @app.route('/<name>')
# def print_name(name):
#     return "Hello,  {}. Did you really think I wouldn't find out you were FAT!".format(name)
# hi

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
