import requests
from tkinter import messagebox

class LineAPI:
    def __init__(self, channel_access_token):
        self.channel_access_token = channel_access_token
        self.base_url = "https://api.line.me/v2/bot/message"
        self.headers = {
            'Authorization': f'Bearer {self.channel_access_token}',
            'Content-Type': 'application/json'
        }

    def fetch_messages(self, user_id, count=100):
        try:
            # ดึงข้อมูลจากไลน์ (LINE Messaging API อาจไม่รองรับการดึงข้อความแบบนี้โดยตรง)
            url = f"{self.base_url}/user/{user_id}/content"
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                messages = response.json().get('messages', [])
                return [message.get('text', '') for message in messages[:count]]
            else:
                raise Exception(response.json().get('message', 'Unknown error'))
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching messages from LINE: {e}")
            return []
