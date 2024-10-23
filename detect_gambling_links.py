import re

def detect_gambling_links(tweets):
    gambling_keywords = [r"\b(bet|gamble|casino|poker|slots|lottery)\b"]
    gambling_count = 0

    for tweet in tweets:
        tweet_text = tweet.lower()
        for keyword in gambling_keywords:
            if re.search(keyword, tweet_text):
                gambling_count += 1
                break

    return gambling_count
