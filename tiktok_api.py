import requests


class TikTokAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_posts(self, user_id, count=100):
        # TikTok API อาจต้องการการยืนยันตัวตนที่ซับซ้อน
        # โปรดตรวจสอบ TikTok Developer Portal สำหรับข้อมูลล่าสุด
        url = f"https://api.tiktok.com/v1/users/{user_id}/videos"
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            videos = response.json().get('data', [])
            return [video.get('description', '') for video in videos[:count]]
        else:
            return []
