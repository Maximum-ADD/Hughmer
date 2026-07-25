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
    setup_score = model.find_probability_score(setup, model.setup_word_totals, model.setup_total_words)
    punchline_score = model.find_probability_score(punchline, model.punchline_word_totals, model.punchline_total_words)
    result = model.score_joke(setup, punchline)
    return flask.jsonify({
        'score' : result,
        'setup_score' : setup_score,
        'punchline_score' : punchline_score
                          })

# @app.route('/<name>')
# def print_name(name):
#     return "Hello,  {}. Did you really think I wouldn't find out you were FAT!".format(name)
# hi

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
