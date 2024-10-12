# Sentiment-Analysis-on-Tweets
This project allows you to perform sentiment analysis on tweets by fetching them from the Twitter API using specific keywords or hashtags. The analysis determines whether the tweets have a positive, negative, or neutral sentiment. It uses Python libraries such as Tweepy for fetching tweets, TextBlob for sentiment analysis, and Matplotlib for visualizing the results.

----

Im giving another go to Data Science!
The libraries I will learn in this project are:
  - Libraries:
      - tweepy
      - nltk
      - pandas
      - textblob

The keyskills I will learn in this project are:
  - Key Skills:
    - Natural language processing
    - data visualization


## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
  - [Step 1: Set up Twitter API credentials](#step-1-set-up-twitter-api-credentials)
  - [Step 2: Authenticate to Twitter](#step-2-authenticate-to-twitter)
  - [Step 3: Fetch Tweets](#step-3-fetch-tweets)
  - [Step 4: Analyze Sentiment](#step-4-analyze-sentiment)
  - [Step 5: Visualize Sentiment](#step-5-visualize-sentiment)
- [Example](#example)


## Features
- Fetch tweets based on keywords or hashtags.
- Perform sentiment analysis using `TextBlob`.
- Visualize the sentiment distribution using a histogram.

## Prerequisites
- Python 3.x
- A Twitter Developer account for API keys.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/twitter-sentiment-analysis.git
   cd twitter-sentiment-analysis
   ```

2. Install the required Python libraries:
   ```
   pip install tweepy pandas textblob matplotlib
   ```
3. Set up a Twitter Developer account and create an application to get your Twitter API credentials:
   
   [Twitter Developer Portal](https://developer.x.com/en/apps)

4. Replace the placeholders in the script (`API_KEY`, `API_SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`) with your Twitter API credentials.

## Usage
1. Run the script:
   ```
   python sentiment_analysis.py
   ```
2. Enter a keyword or hashtag when prompted:

   ```
   Enter a keyword or hashtag to search: #YourHashtag
   ```
3. Enter the number of tweets to fetch:

   ```
   Enter the number of tweets to fetch: 100
   ```

4. The script will fetch tweets, analyze their sentiment, and display a table showing the tweet text and corresponding sentiment score. It will also display a histogram of the sentiment distribution.

## How It Works

### Step 1: Set up Twitter API credentials

In the script, the Twitter API credentials (`API_KEY`, `API_SECRET_KEY`, `ACCESS_TOKEN`, `ACCESS_TOKEN_SECRET`) are used to authenticate the app to the Twitter API. These credentials are required to access Twitter’s data.

```py
API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'
```

### Step 2: Authenticate to Twitter
The script uses Tweepy's `OAuthHandler` to authenticate the app using the API credentials. The authentication object (auth) is then passed to create an API object for communicating with Twitter.

```py
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
```

### Step 3: Fetch Tweets
The `fetch_tweets` function searches for tweets using a specified keyword or hashtag. It retrieves the full text of each tweet along with its creation time and the username of the person who posted it. The tweets are returned as a Pandas DataFrame for easier manipulation.

```py
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
```

### Step 4: Analyze Sentiment

The `analyze_sentiment` function uses `TextBlob` to analyze the sentiment of each tweet. `TextBlob` assigns a polarity score to each tweet, where:
  - Positive sentiment has a polarity score greater than 0.
  - Negative sentiment has a polarity score less than 0.
  - Neutral sentiment has a polarity score of 0.
  - The function adds the sentiment score to the DataFrame.

  ```py
  def analyze_sentiment(tweets):
    sentiments = []
    
    for tweet in tweets['text']:
        analysis = TextBlob(tweet)
        sentiments.append(analysis.sentiment.polarity)  # Get polarity score

    tweets['sentiment'] = sentiments
    return tweets
  ```

### Step 5: Visualize Sentiment
The `visualize_sentiment` function creates a histogram showing the distribution of tweet sentiments. The x-axis represents sentiment polarity, and the y-axis represents the number of tweets. Tweets with positive sentiment are on the right, negative sentiment on the left, and neutral sentiment around 0.

```py
def visualize_sentiment(tweets):
    plt.figure(figsize=(10, 6))
    plt.hist(tweets['sentiment'], bins=30, color='blue', alpha=0.7)
    plt.title('Sentiment Analysis of Tweets')
    plt.xlabel('Sentiment Polarity')
    plt.ylabel('Number of Tweets')
    plt.axvline(0, color='red', linestyle='dashed', linewidth=1)
    plt.show()
```

## Example
Here's an example of how the results might look after running the script:

```cmd
Enter a keyword or hashtag to search: #Python
Enter the number of tweets to fetch: 50
```
