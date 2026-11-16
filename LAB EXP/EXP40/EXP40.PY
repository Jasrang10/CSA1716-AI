import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.DataFrame({
    'Movie1': [5, 4, 1, 0],
    'Movie2': [3, 0, 1, 2],
    'Movie3': [4, 5, 0, 1],
    'Movie4': [0, 3, 5, 4],
    'Movie5': [1, 0, 4, 5],
}, index=['Alice', 'Bob', 'Carol', 'Dave'])      # 0 = not rated

sim = pd.DataFrame(cosine_similarity(ratings),
                   index=ratings.index, columns=ratings.index)

def recommend(user, n=2):
    scores = {}
    for movie in ratings.columns[ratings.loc[user] == 0]:
        others = ratings.index[(ratings.index != user) & (ratings[movie] > 0)]
        if len(others) == 0: continue
        w = sim.loc[user, others]
        scores[movie] = (w * ratings.loc[others, movie]).sum() / w.sum()
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)[:n]

print("Recommendations for Alice:", recommend('Alice'))
