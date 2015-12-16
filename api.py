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
    model = get_model()
    json = model.most_similar_words(key)
    return jsonify(json)
  except IOError as err:
    return err


def get_model():
  if not os.pth.exists('hoge.model'):
    i = 0
    with open('documents.json') as file:
      docs = json.load(file)
    sentences = []
    for doc in docs:
      sentence = doc2vec.LabeledSentence(words=doc, labels=['DOC_%s' % i])
      i = i + 1
      sentences.append(sentence)
    model = doc2vec.Doc2Vec(sentences)
    model.save('hoge.model')

  model = doc2vec.Doc2Vec.load('hoge.model')
  return model



if __name__ == "__main__":
  app.run(debug=True)



# $ pip install -U https://github.com/satomacoto/gensim/archive/doc2vec-mostSimilarWordsAndLabels.zip
# http://satomacoto.blogspot.com/2015/02/doc2vec.html
