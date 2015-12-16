# $ pip install -U https://github.com/satomacoto/gensim/archive/doc2vec-mostSimilarWordsAndLabels.zip
# http://satomacoto.blogspot.com/2015/02/doc2vec.html

from gensim.models import word2vec
from gensim.models import doc2vec
import json
import sys

with open('documents.json') as file:
  docs = json.load(file)

i = 0
sentences = []
for doc in docs:
  sentence = doc2vec.LabeledSentence(words=doc, labels=['SENT_%s' % i])
  i = i + 1
  sentences.append(sentence)
labeledSentences = doc2vec.LabeledListSentence(docs)

model = doc2vec.Doc2Vec(sentences)
model.most_similar_words('d3')
print model.most_similar_labels('SENT_30')

print sys.argv


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
