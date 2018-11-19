import re


def bigrams(text):
    words = text.split()
    return zip(words, words[1:])

def trigrams(text):
    words = text.split()
    return zip(words, words[1:], words[2:])


def ngram_probs(filename='raw_sentences.txt'):
    file = open(filename, 'r')
    sentence = file.read()
    text = re.sub('\W', ' ', sentence.lower())
    words = text.split()
    def bigram_probs(compare):
        num = 0
        for i in zip(words, words[1:]):
            if i == list:
                num = num + 1
        return num
    def trigram_probs(compare):
        num = 0
        for i in zip(words, words[1:], words[2:]):
            if i == list:
                num = num + 1
        return num
    return bigram_probs, trigram_probs


a, b = ngram_probs()

print(a([('we', 'are')]))
