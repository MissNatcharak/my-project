import requests


class DiscordAPI:
    def __init__(self, bot_token):
        self.bot_token = bot_token

    def fetch_messages(self, channel_id, count=100):
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={count}"
        headers = {
            'Authorization': f'Bot {self.bot_token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            messages = response.json()
            return [message.get('content', '') for message in messages]
        else:
            return []
