from flask import Flask, jsonify
from fast_fuzzy_search import FastFuzzySearch
import os
app = Flask('Fast Fuzzy Search Demo', static_url_path='')
root = os.path.dirname(os.path.abspath(__file__))


ffs = FastFuzzySearch({'language': 'english'})


def setup():
    print('Beginning setup...')
    with open('cities.txt') as f:
        for i, city in enumerate(f):
            ffs.add_term(city.strip(), i)
    print('Setup complete')


@app.route('/search/<query>')
def search(query):
    return jsonify(ffs.search(query))


@app.route('/')
def root_index():
    with open('index.html') as f:
        return f.read()


if __name__ == '__main__':
    setup()
    app.run()
