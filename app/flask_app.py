from flask import Flask, render_template, request

from app.word import Words
from app.word_loader import load_words
from app.word_sorter import sort_words_from_text


def setup_app():
    storage = Words()
    load_words(storage)
    return storage


word_storage = setup_app()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def sort_words():
    if request.method == "POST" and request.form['raw_text']:
        raw_text = request.form['raw_text']
        output = sort_words_from_text(raw_text, word_storage)
    else:
        output = None
    return render_template("result.html", output=output)


# @app.errorhandler(Exception)
# def handle_exception(error):
#     response = {'error': type(error).__name__, 'message': str(error)}
#     return jsonify(response)
