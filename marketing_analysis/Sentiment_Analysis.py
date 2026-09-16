import psycopg2
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
nltk.download('vader_lexicon')
sia=SentimentIntensityAnalyzer()

conn=psycopg2.connect(
    database="mark_a",
    user="postgres",
    host="localhost",
    port=5432,
    password="codex_dbms"
)

query='''
Select * from customer_reviews
'''
df=pd.read_sql(query,con=conn)

def calculate_sentiment(review):
    sentiment=sia.polarity_scores(review)
    return float(sentiment["compound"])

def categorize_sentiment(score,rating):
    if score >  0.05: #! Positive sentiment
        if rating>=4: #! High Rating & Positive Sentiment
            return 'positive'
        elif rating ==3: #! Neutral Rating But Positive Sentiment
            return 'Mixed Positive'
        else:
            return 'Mixed Negative' #! Low Rating But Positive Sentiment
    elif score< -0.05: #! Negative Sentiment
        if rating<=2: #! Low Rating & Negative Sentiment
            return 'positive'
        elif rating ==3: #! Neutral Rating But Negative Sentiment
            return 'Mixed Negative'
        else:
            return 'Mixed Positive' #! Low Rating But Negative Sentiment
    else:#! Neutral Sentiments
        if rating>=4: #! High Rating Neutral Sentiment
            return 'positive'
        elif rating <=2:#! Low Rating Neutral Sentiment
            return 'Negative'
        else:
            return 'Neutral' #! Low Rating Neutral Sentiment
def sentiment_bucket(score):
    if score >= 0.5:
        return'0.5 to 1.0'
    elif 0.0<=score<0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score <0.0:
        return '-0.5 to 0.0'
    else:
        return '-1.0 to -0.5'
        
# score=df["reviewtext"].apply(calculate_sentiment)
# print(type(float(score)))
df['sentiment_score']=df['reviewtext'].apply(calculate_sentiment)
print(type(df['sentiment_score']))
df['sentiment_category']=df.apply(lambda row : categorize_sentiment(row['sentiment_score'],row['rating']),axis=1)
df['sentiment_bucket']=df['sentiment_score'].apply(sentiment_bucket)
df.to_csv('customer_review_with_sentiment.csv',index=False)