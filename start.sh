if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/c2bot/Write-Him-At-Book-in-Telegram-Bot.git /Write-Him-At-Book-in-Telegram-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Write-Him-At-Book-in-Telegram-Bot
fi
cd /Write-Him-At-Book-in-Telegram-Bot
pip3 install -U -r requirements.txt
echo "𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜...."
python3 bot.py
