from nltk.corpus import stopwords
from collections import defaultdict
import csv


# def generate_ngrams(text, n):
#     words = [word for word in text.split(' ') if word not in set(stopwords.words('english')) ]
#     # print(f'Sentence after removing stopwords: {words}')
#     temp=zip(*[words[i:] for i in range(0,n)])
#     ans=[' '.join(n) for n in temp]
#     return ans



stop_words = set(stopwords.words('english'))
def generate_ngrams(text, n):
    words = [word for word in text.split() if word not in stop_words ] 

    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)

    return ngrams


all_positive_words = ''
all_negative_words = ''
all_neutral_words = ''
with open('all-data.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        if row[0] == 'positive':
            all_positive_words += row[1]

        if row[0] == 'negative':
            all_negative_words += row[1]

        if row[0] == 'neutral':
            all_neutral_words += row[1]

    positive_unigram = generate_ngrams(all_positive_words, 1)
    negative_unigram = generate_ngrams(all_negative_words, 1)
    neutral_unigram = generate_ngrams(all_neutral_words, 1)

    print(positive_unigram[:20])
    print(negative_unigram[:20])
    print(neutral_unigram[:20])
    





        
