import pywmapi as wm
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def authenticate():
    try:
        sess = wm.auth.signin(EMAIL, PASSWORD)
        return sess
    except:
        print(f"Authentication failed.")
