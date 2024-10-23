# main.py
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from twitter_connection import connect_to_twitter, get_user_id, fetch_home_timeline
from fetch_tweets import fetch_tweets  # หากใช้ฟังก์ชันนี้ในการดึงข้อมูลเพิ่มเติม
from detect_bot import detect_bot
from detect_spam import detect_spam
from detect_gambling_links import detect_gambling_links
from detect_phishing_links import detect_phishing_links
from display_result import display_result
from facebook_api import FacebookAPI
from tiktok_api import TikTokAPI
from discord_api import DiscordAPI
from line_api import LineAPI
from pinterest_api import PinterestAPI


class SocialMediaAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Safety Analyzer")
        self.root.geometry("600x450")
        self.root.configure(bg="#2c3e50")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="#3498db", foreground="#ecf0f1", font=("Helvetica", 10, "bold"))
        style.map("TButton", background=[("active", "#2980b9")])
        style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1", font=("Helvetica", 12))
        style.configure("TCombobox", foreground="#2c3e50", font=("Helvetica", 10))

        self.create_widgets()
        self.api_key = None
        self.selected_platform = None

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=(20, 10))
        main_frame.pack(fill="both", expand=True)

        self.header_label = ttk.Label(
            main_frame, text="Social Media Safety Analyzer", font=("Helvetica", 18, "bold")
        )
        self.header_label.pack(pady=(10, 20))

        self.platform_label = ttk.Label(main_frame, text="Select Platform:")
        self.platform_label.pack(pady=(5, 5))

        self.platform_combobox = ttk.Combobox(
            main_frame, values=["Twitter", "Facebook", "TikTok", "Discord", "LINE", "Pinterest"], state="readonly"
        )
        self.platform_combobox.pack(pady=(0, 20))
        self.platform_combobox.bind("<<ComboboxSelected>>", self.on_platform_selected)

        self.api_button = ttk.Button(main_frame, text="Set API Key or Token", command=self.get_api_key)
        self.api_button.pack(pady=10, fill="x")

        self.analyze_button = ttk.Button(main_frame, text="Analyze User", command=self.analyze_social)
        self.analyze_button.pack(pady=10, fill="x")

        self.exit_button = ttk.Button(main_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=(20, 0), fill="x")

        self.footer_label = ttk.Label(
            main_frame, text="Developed for Safe Social Media Analysis", font=("Helvetica", 10)
        )
        self.footer_label.pack(side="bottom", pady=10)

    def on_platform_selected(self, event):
        self.selected_platform = self.platform_combobox.get()
        messagebox.showinfo("Platform Selected", f"You selected {self.selected_platform}.")

    def get_api_key(self):
        if not self.selected_platform:
            messagebox.showerror("Error", "Please select a platform first.")
            return

        if self.selected_platform == "Twitter":
            self.api_key = simpledialog.askstring("Bearer Token", "Enter your Twitter Bearer Token:")
        elif self.selected_platform == "Facebook":
            self.api_key = simpledialog.askstring("Access Token", "Enter your Facebook Access Token:")
        elif self.selected_platform == "TikTok":
            self.api_key = simpledialog.askstring("API Key", "Enter your TikTok API Key:")
        elif self.selected_platform == "Discord":
            self.api_key = simpledialog.askstring("Bot Token", "Enter your Discord Bot Token:")
        elif self.selected_platform == "LINE":
            self.api_key = simpledialog.askstring("Channel Access Token", "Enter your LINE Channel Access Token:")
        elif self.selected_platform == "Pinterest":
            self.api_key = simpledialog.askstring("Access Token", "Enter your Pinterest Access Token:")

        if self.api_key:
            messagebox.showinfo("Success", "API Key/Token has been set!")

    def analyze_social(self):
        if not self.selected_platform or not self.api_key:
            messagebox.showerror("Error", "Please select a platform and set API Key/Token.")
            return

        if self.selected_platform.lower() == 'twitter':
            api = connect_to_twitter(self.api_key)
            if api:
                username = simpledialog.askstring("Twitter Username", "Enter the Twitter username:")
                if username:
                    user_id = get_user_id(api, username)
                    if user_id:
                        posts = fetch_home_timeline(api, user_id, count=100)
                    else:
                        messagebox.showerror("Error", "Could not retrieve user ID.")
                        return
                else:
                    messagebox.showerror("Error", "Username must be provided.")
                    return
            else:
                return
        elif self.selected_platform.lower() == 'facebook':
            api = FacebookAPI(self.api_key)
            api.connect()
            fetch_function = api.fetch_posts
        elif self.selected_platform.lower() == 'tiktok':
            api = TikTokAPI(self.api_key)
            fetch_function = api.fetch_posts
        elif self.selected_platform.lower() == 'discord':
            api = DiscordAPI(self.api_key)
            fetch_function = api.fetch_messages
        elif self.selected_platform.lower() == 'line':
            api = LineAPI(self.api_key)
            fetch_function = api.fetch_messages
        elif self.selected_platform.lower() == 'pinterest':
            api = PinterestAPI(self.api_key)
            fetch_function = api.fetch_pins
        else:
            messagebox.showerror("Error", "Unsupported platform.")
            return

        user_id = simpledialog.askstring("User ID", f"Enter the user ID for {self.selected_platform}:")
        if not user_id:
            messagebox.showerror("Error", "User ID must be provided.")
            return

        posts = fetch_function(api, user_id, count=100)

        if posts:
            bot_count = detect_bot(posts)
            spam_count = detect_spam(posts)
            gambling_count = detect_gambling_links(posts)
            phishing_count = detect_phishing_links(posts)
            display_result(user_id, bot_count, spam_count, gambling_count, phishing_count)
        else:
            messagebox.showinfo("Info", f"No posts found for user {user_id} on {self.selected_platform}.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SocialMediaAnalyzerApp(root)
    root.mainloop()
