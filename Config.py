import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5855431153:AAFiuvCcjhbhkOEQqh3Y0z_-cIMvoYBrANA")


    API_ID = int(os.environ.get("API_ID", "17631893"))


    API_HASH = os.environ.get("API_HASH", "dc04058d98e72212c2830ca092e01b09")
