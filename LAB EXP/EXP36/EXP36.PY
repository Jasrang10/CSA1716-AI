import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
texts = ["I love this phone, it is amazing!",
         "This movie was terrible and boring.",
         "The food was okay."]

for t in texts:
    score = sia.polarity_scores(t)['compound']
    label = "Positive" if score >= 0.05 else "Negative" if score <= -0.05 else "Neutral"
    print(f"{t} -> {label} ({score})")
