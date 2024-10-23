from tkinter import simpledialog, messagebox

def get_api_credentials():
    api_key = simpledialog.askstring("API Key", "Enter your API Key:")
    api_secret = simpledialog.askstring("API Secret", "Enter your API Secret:")
    access_token = simpledialog.askstring("Access Token", "Enter your Access Token:")
    access_secret = simpledialog.askstring("Access Secret", "Enter your Access Secret:")

    if not api_key or not api_secret or not access_token or not access_secret:
        messagebox.showerror("Error", "All API credentials must be provided.")
        return None
    return api_key, api_secret, access_token, access_secret
