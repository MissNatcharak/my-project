import requests
from tkinter import messagebox

class PinterestAPI:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = "https://api.pinterest.com/v1"
        self.headers = {
            'Authorization': f'Bearer {self.access_token}'
        }

    def fetch_pins(self, user_id, count=100):
        try:
            url = f"{self.base_url}/users/{user_id}/pins/"
            params = {
                'limit': count,
            }
            response = requests.get(url, headers=self.headers, params=params)
            if response.status_code == 200:
                pins = response.json().get('data', [])
                return [pin.get('note', '') for pin in pins]
            else:
                raise Exception(response.json().get('message', 'Unknown error'))
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching pins from Pinterest: {e}")
            return []
