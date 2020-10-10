from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, TemplateSendMessage,ButtonsTemplate,URIAction,QuickReplyButton,QuickReply
)

import time
import math
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

import psycopg2
import random

from datetime import datetime as dt

def get_connection():
    dsn = os.environ.get('DATABASE_URL')
    return psycopg2.connect(dsn)

'''

conn = get_connection()

cur = conn.cursor()


sql = "insert into retasudb values('user_id','Aくん','100')"

cur.execute("insert into botdb values({id},'{user_id}','{name}','{point}')".format(id=2,user_id='user_id2'+'Aくん2',name='Aくん',point='200'))

cur.execute("UPDATE botdb SET point = '200' WHERE id='2';")

cur.execute("UPDATE botdb SET point = '200' WHERE id='6039';")

cur.execute('SELECT * FROM botdb')



cur = connection.cursor()
cur.execute("ROLLBACK")
conn.commit()

cur.execute('SELECT * FROM botdb')

row_ = []

for row in cur:
    if 'user_id2Aくん' in row:
        ok = row[3]
    else:
        pass
    row_.append(row)

print(ok)

print(row_)


cur.execute("UPDATE botdb SET point = '{point}' WHERE id='{dbID}';".format(point='250',dbID='6039'))


'''


set_ = 2

app = Flask(__name__)

stoptime = 0

stoppoint = 0

setting_ = {}
'''
setting_ = {
    user_id:{
        'use':True,
        'name':'name',
        'point':0,
    	'time':0,
    	'timepoint':0,
        'ID':'',
    }
}
'''
setting2 = {
	'setting1':False,
	'setting2':False,
	'setting3':False,
	'setting4':False,
	'setting5':False,
	'setting6':False,
	'setting7':False,
	'setting8':False,
	'setting9':False,
	'setting10':False,
}



Time = {
    'count':0,
    'pointcount_1':0,
    'pointcount_2':0,
    'pointcount2_1':0,
    'pointcount2_2':0,
}
'''
Time = {
    user_id:{
        'count':0,
        'pointcount_1':0,
        'pointcount_2':0,
        'pointcount2_1':0,
        'pointcount2_2':0
        }
}


date = {
    'ID':{'point':0}
}
'''
date = {}

pdate = {
    'save': True,
    'date': '',
    'point':0
    }
def namecheck(ID,name):
    random_id = random.randint(1,999999)
    point = None
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("ROLLBACK")
    conn.commit()
    cur.execute('SELECT * FROM botdb')
    date[ID] = {'point':0}
    '''
    with open('date.json','r') as f:
        date = json.load(f)
    '''
    for row in cur:
        if ID+name in row:
            setting_[ID]['text'] = row[2]
            setting_[ID]['dbID'] = row[0]
            return row[2]
    '''
    if ID in date:
        if name in date[ID]:
            point = date[ID][name]
            return point
    '''
    if point == None:
        setting_[ID] = {}
        setting_[ID]['dbID'] = random_id
        setting_[ID]['text'] = name
        cur.execute("insert into botdb values({id},'{user_id}','{name}','{point}')".format(id=random_id,user_id=ID,name=name,point='0'))
        conn.commit()
        return name

    else:
        setting_[ID] = {}
        setting_[ID]['dbID'] = random_id
        setting_[ID]['text'] = name
        cur.execute("insert into botdb values({id},'{user_id}','{name}','{point}')".format(id=random_id,user_id=ID,name=name,point='0'))
        conn.commit()
        return name

def seve(ID):
    try:
        print('ok2')
        print(setting_[ID]['dbID'])
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("ROLLBACK")
        conn.commit()
        cur.execute('SELECT * FROM botdb')
        text = setting_[ID]['text']
        for row in cur:
            if ID in row:
                dbID = row[0]
                print('ok3')
                cur.execute("UPDATE botdb SET name = '{name}' WHERE id='{dbID}';".format(name=text,dbID=dbID))
                conn.commit()
                print('ok3-2')
                return
        cur.execute("UPDATE botdb SET name = '{name}' WHERE id='{dbID}';".format(name=text,dbID=setting_[ID]['dbID']))
        conn.commit()
        print('ok4')
    except Exception as e:
        print (str(e))
    '''


    with open('date.json','r') as f:
        date = json.load(f)
    date[ID][setting_[ID]['name']] = date[ID][setting_[ID]['name']] + setting_[ID]['point2']
    with open('date.json','w') as f:
        json.dump(date, f)
    '''




#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = 'kqe9SOh5ObwW7tmUHww+OawdLD90POBr6QYXWxYyJ2zkezVMIfVVO8aS0yW9kFPI+9QH/YCqpOZXrqjUuqn1WnrOgxM7H0L96CT0rL8XxFQF3qp21u6Yy2OVj+DJVkC4jhkdP39yvGV3Yh1YqbyLJAdB04t89/1O/w1cDnyilFU='
#os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = 'effff0387a14d1def1aca27b6df82e89'
#os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/qr/<ID>")
def qrcode(ID):
    text = namecheck(ID,'はじめまして(デフォルト)')
    return text

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global set_
    global stoptime
    global stoppoint
    msg_from = event.reply_token
    msg_text = event.message.text
    user_id = event.source.user_id
    '''if msg_text == '設定する':
        items = {'items': [{'type': 'action','action': {'type': 'message','label': '貯める','text': '貯める'}},{'type': 'action','action': {'type': 'message','label': '使う','text': '使う'}}]}
        line_bot_api.reply_message(msg_from,TextSendMessage(text='まずは貯めるのか使うのかを教えてね！',quick_reply=items))
        setting_[user_id] = {'use':True,'name':'name','point':0,'time':0,'timepoint':0,'ID':'','point2':0,'dbID':0}
        setting_[user_id]['ID'] = user_id
        Time[user_id] = {'count':0,'pointcount_1':0,'pointcount_2':0,'pointcount2_1':0,'pointcount2_2':0}
        setting2[user_id] = {'setting1':False,'setting2':False,'setting3':False,'setting4':False,'setting5':False,'setting6':False,'setting7':False,'setting8':False,'setting9':False,'setting10':False,}
        set_ = 2
'''
    if msg_text == '設定する':
        line_bot_api.reply_message(msg_from,TextSendMessage(text='表示したい文字を入力してね！'))
        setting_[user_id] = {'use':True,'name':'name','point':0,'time':0,'timepoint':0,'ID':'','point2':0,'dbID':0}
        setting_[user_id]['ID'] = user_id
        Time[user_id] = {'count':0,'pointcount_1':0,'pointcount_2':0,'pointcount2_1':0,'pointcount2_2':0}
        setting2[user_id] = {'setting1':False,'setting2':False,'setting3':False,'setting4':False,'setting5':False,'setting6':False,'setting7':False,'setting8':False,'setting9':False,'setting10':False,}
        set_ = 2
        setting2[user_id]['setting1'] = True


    else:
        try:
            if setting2[user_id]['setting1'] == True and user_id == setting_[user_id]['ID']:
                try:
                    print('ok')
                    setting2[user_id]['setting1'] = False
                    setting2[user_id]['setting2'] = True
                    text = msg_text
                    setting_[user_id]['text'] = text
                    text_ = namecheck(user_id,text)
                    setting_[user_id]['point'] = point
                    line_bot_api.reply_message(msg_from,TextSendMessage(text='表示する文字を"{}"に変更したよ！'.format(text_)))
                    line_bot_api.reply_message(msg_from,TextSendMessage(text='あなたのURLは"https://retasu-qr-code.herokuapp.com/qr/{}"だよ！！'.format(user_id)))
                except Exception as e:
                    print (str(e))
        except:
            pass
        else:
            items = {'items': [{'type': 'action','action': {'type': 'message','label': '設定する','text': '設定する'}}]}
            line_bot_api.reply_message(msg_from,TextSendMessage(text='表示する文字を設定したいときは\n「設定する」\nと送信してね！\n\n下のボタンからも送信できるよ！',quick_reply=items))





if __name__ == "__main__":
#    app.run()
    port =  int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
