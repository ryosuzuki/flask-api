# $ pip install -U https://github.com/satomacoto/gensim/archive/doc2vec-mostSimilarWordsAndLabels.zip
# http://satomacoto.blogspot.com/2015/02/doc2vec.html

from gensim.models import word2vec
from gensim.models import doc2vec
import json
import sys

def init():
  with open('documents.json') as file:
    commits = json.load(file)
  i, sentences = 0, []
  for id in commits:
    commit = commits[id]
    sentence = doc2vec.LabeledSentence(words=commit['words'], labels=[commit['id']])
    i = i + 1
    sentences.append(sentence)
  model = doc2vec.Doc2Vec(sentences)
  model.save('documents.model')
  return model

init()

# words = ['a', 'b', 'c']

# sentences = word2vec.Text8Corpus('hoge.txt')
# model = word2vec.Word2vec(sentences)

# model.save('hoge.model')
# model.most_similar(positive=['woman'])

# model = word2vec.Word2Vec.load('hoge.model')
#
# model.save_word2vec_format('hoge.model.bin', binary=True)
# model = word2vec.Word2Vec.load_word2vec_format('hoge.model.bin', binary=True)
#
# model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
# > [('queen', 0.5359965)]
