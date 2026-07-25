import model

jokes = [
    # initial test
    ("Why did the chicken cross the road", "to get to the other side"),
    ("Why did the quantum physicist dissolve in coffee", "because he was a muon"),
    ("What do you call a fish without eyes", "a fsh"),
    ("Why don't scientists trust atoms", "because they make up everything"),
    ("What do you call a bear with no teeth", "a gummy bear"),

    # Should be FUNNY (predictable setup, unpredictable punchline)
    ("Why did the chicken cross the road", "to get to the other side"),
    ("Why don't scientists trust atoms", "because they make up everything"),
    ("What do you call a fish without eyes", "a fsh"),
    ("Why did the scarecrow win an award", "because he was outstanding in his field"),

    # Should be BORING (predictable setup, predictable punchline)
    ("What did the dog say", "woof"),
    ("Why did the cat sit", "because it was tired"),
    ("What is a cat", "an animal"),
    ("Why did the man walk", "to get somewhere"),

    # Should be ANTICLIMAX (unpredictable setup, predictable punchline)
    ("Why did the quantum physicist dissolve in coffee", "because he was wet"),
    ("What happens when a neurosurgeon eats a burrito on the moon", "he gets full"),
    ("Why did the existentialist refuse to cross the road", "yes"),
    ("What did nietzsche say to the thermodynamic anomaly", "nothing"),

    # Should be AVANT-GARDE (unpredictable setup, unpredictable punchline)
    ("Why did the quantum physicist dissolve in coffee", "because he was a muon"),
    ("What does a cryptographer eat for breakfast", "hashed eggs"),
    ("Why did the topologist cross the road", "she couldn't tell it from the donut"),
    ("What did the nihilist say to the sommelier", "burgundy"),
]

for setup, punchline in jokes:
    s = model.find_probability_score(setup, model.setup_word_totals, model.setup_total_words)
    p = model.find_probability_score(punchline, model.punchline_word_totals, model.punchline_total_words)
    print(f"Setup: {s:.5f} | Punchline: {p:.5f} | Gap: {round(s-p, 5)} | joke score: {model.score_joke(setup, punchline)} | {setup[:30]}")

print(model.find_probability_score("burgundy", model.punchline_word_totals, model.punchline_total_words))