import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

MONGO_URL = os.getenv("MONGO_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

#MONGODB_URL="mongodb://127.0.0.1:27017/meditrack"
