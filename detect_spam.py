import re

def detect_spam(tweets):
    spam_keywords = ["win", "free", "click here", "subscribe", "buy now", "limited time"]
    spam_count = 0

    for tweet in tweets:
        tweet_text = tweet.lower()
        if any(keyword in tweet_text for keyword in spam_keywords):
            spam_count += 1

        if re.search(r'http[s]?://', tweet_text):
            spam_count += 1

    return spam_count
