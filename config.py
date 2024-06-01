import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    
    API_KEY = os.environ.get("GOOGLE_API_KEY", "")
