import pandas as pd
from src.text_preprocessing import clean_text
from src.sentiment_analysis import analyze_sentiment
from src.topic_modeling import lda_topic_modeling

data = pd.read_csv('data/synthetic_reviews.csv')

print("Columns in dataset:", data.columns)

data['cleaned_text'] = data['review'].apply(clean_text) 

data['sentiment'] = data['cleaned_text'].apply(analyze_sentiment)


print(data[['review', 'cleaned_text', 'sentiment']])  

data.to_csv('sentiment_analysis_results.csv', index=False)

import matplotlib.pyplot as plt

sentiment_counts = data['sentiment'].value_counts()

sentiment_counts.plot(kind='bar', color=['red', 'green'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.show()
