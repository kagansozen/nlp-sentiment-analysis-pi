import random
import pandas as pd

themes = [
    "raw emotions of post-war Italy",
    "gritty portrayal of poverty",
    "unsentimental realism",
    "political themes and class struggle",
    "authentic Italian cityscapes",
    "social issues through everyday lives",
    "non-professional actors",
    "humanistic storytelling"
]

# positive and negative sentiments
positive_words = ["brilliant", "powerful", "touching", "authentic", "moving", "gripping"]
negative_words = ["disappointing", "shallow", "boring", "unsatisfactory", "poor", "predictable"]
neutral_words = ["interesting", "average", "decent", "okay", "neutral", "balanced"]

def generate_reviews(num_reviews):
    reviews = []
    for _ in range(num_reviews):
        sentiment = random.choice(["positive", "negative", "neutral"])
        theme = random.choice(themes)
        
        if sentiment == "positive":
            review = f"The film presents a {theme} in a {random.choice(positive_words)} manner."
        elif sentiment == "negative":
            review = f"The portrayal of {theme} was {random.choice(negative_words)}."
        else:
            review = f"The film explores {theme} in a {random.choice(neutral_words)} way."
        
        reviews.append({
            "review": review,
            "sentiment": sentiment
        })
    
    return pd.DataFrame(reviews)

# 1000 synthetic reviews
df_reviews = generate_reviews(1000)
df_reviews.to_csv('data/synthetic_reviews.csv', index=False)

