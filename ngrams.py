from nltk.corpus import stopwords
from collections import defaultdict
import csv


# def generate_ngrams(text, n):
#     words = [word for word in text.split(' ') if  word not in stop_words]
#     ngram_list = []
#     for i in range(len(words) - n + 1):
#         ngram = words[i: i+n]
#         print(i, i+n)
#         print(ngram)
#         ngram_list.extend(ngram)

#     return ngram_list



stop_words = set(stopwords.words('english'))

def generate_ngrams(text, n):
    words = [word for word in text.split(' ') if word not in stop_words ]
    # print(f'Sentence after removing stopwords: {words}')
    temp=zip(*[words[i:] for i in range(0,n)])
    ans=[' '.join(n) for n in temp]
    return ans


# positive_values = defaultdict(int)
# negative_values = defaultdict(int)
# neutral_values = defaultdict(int)



unigram = []
all_positive_words = ''
with open('all-data.csv', 'r') as file:
    reader = csv.reader(file)
    
    for row in reader:
        if row[0] == 'positive':
            all_positive_words += row[1]

    unigram = generate_ngrams(all_positive_words, 1)
    print(unigram[:20])
    

        
