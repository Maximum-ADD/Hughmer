import datasets as dts
import pandas as pd
import collections as coll
import re
import nltk

nltk.download("stopwords")
STOP_WORDS = set(nltk.corpus.stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    words = text.split()
    # remove stopwords
    words = [word for word in words if word not in STOP_WORDS]
    return words

def find_probability_score(text, word_totals, total_words):
    words = clean_text(text)
    
    if not words:
        return 0
    # using laplace smoothing
    vocab = len(word_totals)
    total_probability = 0
    for word in words:
        word_freq = word_totals.get(word,0)
        probability = (word_freq + 1) / (total_words + vocab)
        total_probability +=  probability

    ave_probability = total_probability/ len(words)
    score = round(ave_probability*1000,2)
    return score

def score_joke(setup, punchline):
    setup_score = find_probability_score(setup, setup_word_totals, setup_total_words)
    punchline_score = find_probability_score(punchline, punchline_word_totals, punchline_total_words)
    # scored like this because a setup should usually be preditable 
    # while a puchline should be unpredictable . 
    # this is a reference to the benign violation theory of humor
    return round(setup_score - punchline_score, 2)


print("Loading dataset...")
dad_jokes_dataset  = dts.load_dataset("shuttie/dadjokes", split="train")
df = dad_jokes_dataset.to_pandas()

# print(f"Loaded {len(df)} jokes")
# print(df.head())

# word frequency for the punchlines below. will be used for probabilities later
punchline_all_words = []
for punchline in df["response"]:
    cleaned_response = clean_text(str(punchline))
    punchline_all_words.extend(cleaned_response)

punchline_word_totals = coll.Counter(punchline_all_words)
punchline_total_words = len(punchline_all_words)

# print(f"Vocab size: {len(word_totals)} unique words")
# print(f"total words: {total_words}")



# setup words frequency below.

setup_all_words = []
for setup in df["question"]:
    cleaned_question = clean_text(str(setup))
    setup_all_words.extend(cleaned_question)

setup_word_totals = coll.Counter(setup_all_words)
setup_total_words = len(setup_all_words)

# print(score_joke("Why did the chicken cross the road?", "to get to the other side!"))
# print(score_joke("Why did the quantum physicist dissolve in coffee?"," because he was a muon!"))

# while True:
#     setup = input("\nSetup: ")
#     punchline = input("Punchline: ")

#     setup_score = find_probability_score(
#         setup,
#         setup_word_totals,
#         setup_total_words
#     )

#     punchline_score = find_probability_score(
#         punchline,
#         punchline_word_totals,
#         punchline_total_words
#     )

#     final_score = score_joke(setup, punchline)

#     print("\nResults")
#     print("----------------------------")
#     print(f"Setup Score:      {setup_score}")
#     print(f"Punchline Score:  {punchline_score}")
#     print(f"Final Humor Score:{final_score}")
#     print("----------------------------")

#     if input("\nAnother joke? (y/n): ").lower() != "y":
#         break   