def detect_bot(tweets):
    bot_count = 0
    time_threshold = 60
    content_count = {}

    for i in range(1, len(tweets)):
        tweet_content = tweets[i].lower()
        if tweet_content in content_count:
            content_count[tweet_content] += 1
        else:
            content_count[tweet_content] = 1

        if content_count[tweet_content] > 2:
            bot_count += 1

    return bot_count
