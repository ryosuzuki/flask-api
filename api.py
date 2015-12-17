from gensim.models import doc2vec
from flask import Flask, request, jsonify
import json
import os.path


app = Flask(__name__)
with open('documents.json') as file:
  data = json.load(file)

@app.route('/', methods=['GET'])
def hello():
  return 'Hello World :)'

@app.route('/<key>', methods=['GET'])
def get(key):
  try:
    res = {}
    model = doc2vec.Doc2Vec.load('documents.model')
    # data = model.most_similar_words(key)
    labels = model.most_similar_labels(key)
    res['_similarity'] = labels
    commits = []
    for label in labels:
      id = label[0]
      commit = data[id]
      commit.pop('words', None)
      commits.append(commit)
    res['commits'] = commits
    return jsonify(res)
  except IOError as err:
    return err

if __name__ == "__main__":
  app.run(port=3000, debug=True)


# $ pip install -U https://github.com/satomacoto/gensim/archive/doc2vec-mostSimilarWordsAndLabels.zip
# http://satomacoto.blogspot.com/2015/02/doc2vec.html
