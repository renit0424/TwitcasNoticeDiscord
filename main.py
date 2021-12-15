import time
import datetime
import requests, json
import schedule
from pytwitcasting.auth import TwitcastingApplicationBasis
from pytwitcasting.api import API
from config import client_id , client_secret, user_id ,webhookurl ,calltime

b = ''
def job():
    global b
    app_basis = TwitcastingApplicationBasis(client_id=client_id,client_secret=client_secret)
    api = API(application_basis=app_basis)
    user = api.get_user_info(user_id)
    a = ''
    if user.is_live == True:
        live = vars(user.get_current_live()['movie'])
        print('ツイキャス配信中です')
        a = live.get('created')+datetime.timedelta(hours=9)
        if a == b:
            print('')
            return
        b = a
        starttime = live.get('created')+datetime.timedelta(hours=9)
        name = user.name
        title = live.get('title')
        subtitle = live.get('subtitle')
        link = live.get('link')
        print(name+'\n\tタイトル' + title +' '+ subtitle + '\n\t開始時間 ' +f'{starttime}')
        webhook_url = webhookurl
        main_content = {
            'username': '【ツイキャス配信通知】'+name,
            'avatar_url': user.image,
            'content': title+' '+subtitle+'\n開始時間 '+f'{starttime}' +'\n'+link
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(webhook_url, json.dumps(main_content), headers=headers)
    else:
        print('ツイキャス配信はありません。')
schedule.every(calltime).minutes.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
