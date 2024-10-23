import tweepy
from tkinter import messagebox

def fetch_tweets(api, username, count=100):
    try:
        # ดึงข้อมูลผู้ใช้จาก username
        user = api.get_user(username=username)
        user_id = user.data.id

        # ดึงทวีตของผู้ใช้โดยใช้ API v2
        tweets = api.get_users_tweets(id=user_id, max_results=count, tweet_fields=['text'])

        # ตรวจสอบว่ามีข้อมูลทวีตหรือไม่ แล้วดึงเฉพาะข้อความจากทวีต
        return [tweet.text for tweet in tweets.data] if tweets and tweets.data else []
    except tweepy.TweepyException as e:
        messagebox.showerror("Error", f"Error fetching tweets: {e}")
        return []
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return []
