import re

def detect_phishing_links(tweets):
    phishing_keywords = ["facebook.com", "google.com", "paypal.com"]
    phishing_count = 0

    for tweet in tweets:
        urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/?.*', tweet)
        for url in urls:
            if any(keyword in url for keyword in phishing_keywords):
                phishing_count += 1

    return phishing_count
