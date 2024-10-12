import tweepy
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Step 1: Set up Twitter API credentials
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Step 2: Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Step 3: Define a function to fetch tweets
def fetch_tweets(keyword, count):
    tweets = api.search(q=keyword, count=count, tweet_mode='extended', lang='en')
    tweet_data = []
    
    for tweet in tweets:
        tweet_data.append({
            'text': tweet.full_text,
            'created_at': tweet.created_at,
            'user': tweet.user.screen_name
        })
    
    return pd.DataFrame(tweet_data)

# Step 4: Define a function to analyze sentiment
def analyze_sentiment(tweets):
    sentiments = []
    
    for tweet in tweets['text']:
        analysis = TextBlob(tweet)
        sentiments.append(analysis.sentiment.polarity)  # Get polarity score

    tweets['sentiment'] = sentiments
    return tweets

# Step 5: Visualize the sentiment
def visualize_sentiment(tweets):
    plt.figure(figsize=(10, 6))
    plt.hist(tweets['sentiment'], bins=30, color='blue', alpha=0.7)
    plt.title('Sentiment Analysis of Tweets')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Number of Tweets')
    plt.axvline(0, color='red', linestyle='dashed', linewidth=1)
    plt.show()

# Step 6: Main function to execute the analysis
def main():
    keyword = input("Enter a keyword or hashtag to search: ")
    count = int(input("Enter the number of tweets to fetch: "))
    
    # Fetch and analyze tweets
    tweets = fetch_tweets(keyword, count)
    tweets = analyze_sentiment(tweets)
    
    # Print out the sentiment analysis results
    print(tweets[['text', 'sentiment']])
    
    # Visualize sentiment distribution
    visualize_sentiment(tweets)

if __name__ == "__main__":
    main()
