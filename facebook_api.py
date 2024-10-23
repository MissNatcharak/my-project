import requests
from tkinter import messagebox

class FacebookAPI:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        self.base_url = "https://graph.facebook.com/v12.0"
        self.headers = {
            'Authorization': f'Bearer {self.bearer_token}'
        }

    def connect(self):
        try:
            # ตรวจสอบการเชื่อมต่อเบื้องต้นโดยดึงข้อมูลผู้ใช้
            response = requests.get(f"{self.base_url}/me", headers=self.headers)
            if response.status_code == 200:
                messagebox.showinfo("Success", "Successfully connected to Facebook using Bearer Token.")
            else:
                raise Exception(response.json().get('error', {}).get('message', 'Unknown error'))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to Facebook: {e}")

    def fetch_posts(self, user_id, count=100):
        try:
            url = f"{self.base_url}/{user_id}/posts"
            params = {
                'limit': count,
            }
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                posts = response.json().get('data', [])
                return [post.get('message', '') for post in posts if 'message' in post]
            else:
                raise Exception(response.json().get('error', {}).get('message', 'Unknown error'))
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching posts from Facebook: {e}")
            return []
