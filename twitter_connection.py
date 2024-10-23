# twitter_connection.py
import tweepy
from tkinter import messagebox

def connect_to_twitter(bearer_token):
    try:
        client = tweepy.Client(bearer_token=bearer_token)
        messagebox.showinfo("Success", "Successfully connected to Twitter using Bearer Token.")
        return client
    except tweepy.TweepyException as e:
        messagebox.showerror("Error", f"Failed to connect to Twitter: {e}")
        return None

def get_user_id(client, username):
    try:
        user = client.get_user(username=username)
        return user.data.id
    except tweepy.TweepyException as e:
        messagebox.showerror("Error", f"Error fetching user ID: {e}")
        return None

def fetch_home_timeline(client, user_id, count=10):
    try:
        response = client.get_users_tweets(id=user_id, max_results=count)
        if response.data:
            tweets = [tweet.text for tweet in response.data]
            return tweets
        else:
            messagebox.showinfo("Info", "No tweets found in the timeline.")
            return []
    except tweepy.TweepyException as e:
        messagebox.showerror("Error", f"Error fetching tweets: {e}")
        return []
