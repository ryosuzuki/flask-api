from gensim.models import doc2vec
from flask import Flask, request, jsonify
import json
import os.path


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
  return 'Hello World :)'

@app.route('/<key>', methods=['GET'])
def get(key):
  try:
    model = doc2vec.Doc2Vec.load('documents.model')
    data = model.most_similar_words(key)
    data = model.most_similar_labels(key)

    data = [
      { "id": "4e9fca2d", "message": "Hoge", "code": "def foo\n  return true\nend" },
      { "id": "359fc02c", "message": "Fuga", "code": "hoge hoge" },
      { "id": "5e32c32a", "message": "Feof", "code": "def bar\n  return false\nend" },
    ]
    return jsonify({ "data": data })
  except IOError as err:
    return err

if __name__ == "__main__":
  app.run(port=3000, debug=True)


# $ pip install -U https://github.com/satomacoto/gensim/archive/doc2vec-mostSimilarWordsAndLabels.zip
# http://satomacoto.blogspot.com/2015/02/doc2vec.html
