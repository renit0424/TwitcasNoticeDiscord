# 【Twitcas】Twitcas Notice Discord
通称ツイキャス配信開始通知Bot君(適当)

[ツイキャス](https://twitcasting.tv/)で気になるあの子の配信開始通知をdiscordに投げてくれるプログラム。

言語はPythonで書いてます。

クッソ雑に作ってあるので手直ししたい人は勝手にしてください()
# 使い方
- [pytwitcasting](https://github.com/tamago324/PyTwitcasting)を使用するのでインストール
```
pip install pytwitcasting
```

- 自動更新のために[schedule](https://github.com/dbader/schedule)を使うのでインストール
```
pip install schedule
```
# ツイキャスアプリケーション登録ページでAPIを発行
  1.[アプリケーション登録ページ](https://apiv2-doc.twitcasting.tv/#introduction)で登録。
  
  2.のちのち使う`ClientID`,`ClientSecret`をメモしておくか設定のconfig.pyに記載しておく。
# discordのWebhookURLを発行する。
  [こっから](https://support.discord.com/hc/ja/articles/228383668-%E3%82%BF%E3%82%A4%E3%83%88%E3%83%AB-Webhooks%E3%81%B8%E3%81%AE%E5%BA%8F%E7%AB%A0)サイト見ながら発行する。
# 設定
  config.pyにさっき取得したものたちを記載する。
  ```
  client_id = '***'
  client_secret = '***'
  user_id = '***'
  webhookurl = '***'
  ```
あとはmain.pyを実行。
多分動く。
