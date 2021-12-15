# TwitcasNoticeDiscord
Twitcastingで気になるあの子の配信開始通知をdiscordに投げてくれるプログラム。
#使い方
- [pytwitcasting](https://github.com/tamago324/PyTwitcasting)を使用するのでインストール
```
pip install pytwitcasting
```

- 自動更新のために[schedule](https://github.com/dbader/schedule)を使うのでインストール
```
pip install schedule
```

- 設定
  - config.pyにClientID,ClientSecret,UserID,discordのwebhookURLを記載する。
  - config.py
  
  ```#ClientID
client_id = '***'
#ClientSecret
client_secret = '***'
#UserID
user_id = '***'
#discord_webhookURL
webhookurl = '***'
```
- あとはtwitcasting.pyを実行。
多分動く。
