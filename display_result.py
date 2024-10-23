from tkinter import messagebox

def display_result(username, bot_count, spam_count, gambling_count, phishing_count):
    result = f"Analysis for user {username}:\n"
    result += f"Number of posts with bot-like behavior: {bot_count}\n"
    result += f"Number of posts containing spam: {spam_count}\n"
    result += f"Number of posts containing gambling-related links: {gambling_count}\n"
    result += f"Number of posts containing phishing-related links: {phishing_count}\n"
    messagebox.showinfo("Analysis Result", result)
