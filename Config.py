import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5855431153:AAFiuvCcjhbhkOEQqh3Y0z_-cIMvoYBrANA")


    API_ID = int(os.environ.get("API_ID", ""))


    API_HASH = os.environ.get("API_HASH", "")
