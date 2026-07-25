# used to show us a list of nltk stopwords so we can keep the ones we need
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
words = sorted(stopwords.words("english"))
print(words)

# Words removed from NLTK stop list (kept as meaningful for jokes):
# Negation:       'no', 'nor', 'not', 'ain'
# Question words: 'how', 'why', 'what', 'when', 'where', 'which', 'who', 'whom'
# Emphasis:       'very', 'too', 'only', 'just', 'once', 'further', 'again'
# Causation:      'because', 'so', 'if', 'while', 'until', 'after', 'before',
#                 'about', 'against', 'during', 'now', 'own'
# Modals:         'can', 'will', 'should', 'would', 'could', 'might', 'need',
#                 'shan', 'mustn', 'haven', 'hasn', 'hadn', 'wasn', 'weren',
#                 'won', 'wouldn', 'couldn', 'didn', 'doesn', 'don', 'isn',
#                 'aren', 'needn', 'mightn'
# Contractions:   "aren't", "couldn't", "didn't", "doesn't", "don't",
#                 "hadn't", "hasn't", "haven't", "isn't", "mightn't",
#                 "mustn't", "needn't", "shan't", "shouldn't", "wasn't",
#                 "weren't", "won't", "wouldn't", "should've", "that'll",
#                 "it'd", "it'll", "it's", "he'd", "he'll", "he's",
#                 "she'd", "she'll", "she's", "they'd", "they'll",
#                 "they're", "they've", "we'd", "we'll", "we're", "we've",
#                 "i'd", "i'll", "i'm", "i've", "you'd", "you'll",
#                 "you're", "you've"
# Quantity:       'all', 'any', 'few', 'more', 'most', 'some', 'many'
# Time/place:     'above', 'below', 'between', 'through', 'before',
#                 'after', 'again', 'up', 'down', 'off', 'out', 'over'