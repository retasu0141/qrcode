from flask import Flask, request, abort,render_template
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
    cur.execute('SELECT * FROM db')
    date[ID] = {'point':0}
    '''
    with open('date.json','r') as f:
        date = json.load(f)
    '''

    for row in cur:
        if ID in row:
            try:
                setting_[ID]['text'] = row[1]
                setting_[ID]['dbID'] = row[0]
                print('01')
                print(setting_[ID]['text'])
                print(setting_[ID]['dbID'])
                return row[1]
            except:
                setting_[ID] = {}
                setting_[ID]['text'] = row[1]
                setting_[ID]['dbID'] = row[0]
                print('02')
                print(setting_[ID]['text'])
                print(setting_[ID]['dbID'])
                return row[1]

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
        cur.execute("insert into db values('{user_id}','{name}','{point}')".format(user_id=ID,name=name,point='0'))
        conn.commit()
        return name

    else:
        setting_[ID] = {}
        setting_[ID]['dbID'] = random_id
        setting_[ID]['text'] = name
        cur.execute("insert into db values('{user_id}','{name}','{point}')".format(user_id=ID,name=name,point='0'))
        conn.commit()
        return name

def idget():
    random_id = random.randint(1,999999)
    point = None
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("ROLLBACK")
    conn.commit()
    cur.execute('SELECT * FROM db')
    '''
    with open('date.json','r') as f:
        date = json.load(f)
    '''
    ID_list = []
    for row in cur:
        ID_list.append(row[0])
    return random.choice(ID_list)

def IDcheck(ID):
    random_id = random.randint(1,999999)
    point = None
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("ROLLBACK")
    conn.commit()
    cur.execute('SELECT * FROM db')
    '''
    with open('date.json','r') as f:
        date = json.load(f)
    '''

    for row in cur:
        if ID+'Ms' in row:
            return row[0]

def seve(ID,text):
    try:
        print('ok2')
        print(setting_[ID]['dbID'])
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("ROLLBACK")
        conn.commit()
        cur.execute('SELECT * FROM db')
        text = setting_[ID]['text']
        for row in cur:
            if ID in row:
                dbID = row[0]
                print('ok3')
                print(text)
                print(dbID)
                cur.execute("UPDATE db SET name = '{name}' WHERE user_id='{user_id}';".format(name=text,user_id=ID))
                conn.commit()
                print('ok3-2')
                return text
        cur.execute("UPDATE db SET name = '{name}' WHERE user_id='{user_id}';".format(name=text,user_id=ID))
        conn.commit()
        print('ok4')
    except Exception as e:
        print (str(e))
        return namecheck(user_id,text)
    '''


    with open('date.json','r') as f:
        date = json.load(f)
    date[ID][setting_[ID]['name']] = date[ID][setting_[ID]['name']] + setting_[ID]['point2']
    with open('date.json','w') as f:
        json.dump(date, f)
    '''

def seve2(ID,ID2):
    #ID=送られた側 ID2=送った側
    try:
        print('ok2')
        print(setting_[ID]['dbID'])
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("ROLLBACK")
        conn.commit()
        cur.execute('SELECT * FROM db')
        for row in cur:
            if ID+'Ms' in row:
                dbID = row[0]
                print('ok3')
                print(text)
                print(dbID)
                cur.execute("UPDATE db SET name = '{name}' WHERE user_id='{user_id}';".format(name=ID2,user_id=ID+'Ms'))
                conn.commit()
                print('ok3-2')
                return text
        cur.execute("UPDATE db SET name = '{name}' WHERE user_id='{user_id}';".format(name=ID2,user_id=ID+'Ms'))
        conn.commit()
        print('ok4')
        return
    except Exception as e:
        print (str(e))
        return


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
    return render_template('HITOKOTO.html',text=text)

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
        namecheck(user_id,'test')
        line_bot_api.reply_message(msg_from,TextSendMessage(text='表示したい文字を入力してね！'))
        setting_[user_id] = {'use':True,'name':'name','point':0,'time':0,'timepoint':0,'ID':'','point2':0,'dbID':0}
        setting_[user_id]['ID'] = user_id
        Time[user_id] = {'count':0,'pointcount_1':0,'pointcount_2':0,'pointcount2_1':0,'pointcount2_2':0}
        setting2[user_id] = {'setting1':False,'setting2':False,'setting3':False,'setting4':False,'setting5':False,'setting6':False,'setting7':False,'setting8':False,'setting9':False,'setting10':False,}
        set_ = 2
        setting2[user_id]['setting1'] = True
        return
    if 'メッセージ送信' in msg_text:
        #namecheck(user_id,'test')
        line_bot_api.reply_message(msg_from,TextSendMessage(text="送りたいメッセージ内容を送信してね！"))
        setting_[user_id] = {'use':True,'name':'name','point':0,'time':0,'timepoint':0,'ID':'','point2':0,'dbID':0}
        setting_[user_id]['ID'] = user_id
        Time[user_id] = {'count':0,'pointcount_1':0,'pointcount_2':0,'pointcount2_1':0,'pointcount2_2':0}
        setting2[user_id] = {'setting1':False,'setting2':False,'setting3':False,'setting4':False,'setting5':False,'setting6':False,'setting7':False,'setting8':False,'setting9':False,'setting10':False,}
        set_ = 2
        setting2[user_id]['setting2'] = True
        return

    if '返信送信' in msg_text:
        #namecheck(user_id,'test')
        line_bot_api.reply_message(msg_from,TextSendMessage(text="送りたいメッセージ内容を送信してね！"))
        setting_[user_id] = {'use':True,'name':'name','point':0,'time':0,'timepoint':0,'ID':'','point2':0,'dbID':0}
        setting_[user_id]['ID'] = user_id
        Time[user_id] = {'count':0,'pointcount_1':0,'pointcount_2':0,'pointcount2_1':0,'pointcount2_2':0}
        setting2[user_id] = {'setting1':False,'setting2':False,'setting3':False,'setting4':False,'setting5':False,'setting6':False,'setting7':False,'setting8':False,'setting9':False,'setting10':False,}
        set_ = 2
        setting2[user_id]['setting3'] = True
        return


#    if 'メッセージ:' in msg_text:
#        #namecheck(user_id,'test')
#        msg_text_ = msg_text.replace("メッセージ:","")
#        line_bot_api.reply_message(msg_from,TextSendMessage(text='送信したよ！'))
#        line_bot_api.reply_message("U76d18383a9b659b9ab3d0e43d06c1e78",TextSendMessage(text=msg_text_))


    else:
        try:
            if setting2[user_id]['setting1'] == True and user_id == setting_[user_id]['ID']:
                try:
                    print('ok')
                    setting2[user_id]['setting1'] = False
                    text = msg_text
                    setting_[user_id]['text'] = text
                    text_ = seve(user_id,text)
                    line_bot_api.reply_message(msg_from,TextSendMessage(text='表示する文字を"{text}"に変更したよ！\nあなたのURLは"https://retasu-qr-code.herokuapp.com/qr/{user_id}"だよ！！'.format(text=text_,user_id=user_id)))
                except Exception as e:
                    print (str(e))
        except Exception as e:
                    print (str(e))
                    items = {'items': [{'type': 'action','action': {'type': 'message','label': '設定する','text': '設定する'}}]}
                    line_bot_api.reply_message(msg_from,TextSendMessage(text='表示する文字を設定したいときは\n「設定する」\nと送信してね！\n\n下のボタンからも送信できるよ！',quick_reply=items))
        if setting2[user_id]['setting2'] == True and user_id == setting_[user_id]['ID']:
            try:
                print('ok-12')
                setting2[user_id]['setting2'] = False
                ID_ = "U76d18383a9b659b9ab3d0e43d06c1e78"#idget()
                seve2(ID_,user_id)
                items = {'items': [{'type': 'action','action': {'type': 'message','label': '返信する','text': '返信送信'}}]}
                line_bot_api.multicast([ID_],TextSendMessage(text='【メッセージが届いたよ！】\n\n' + msg_text,quick_reply=items))
                line_bot_api.reply_message(msg_from,TextSendMessage(text='送信できたよ！'))
            except Exception as e:
                line_bot_api.reply_message(msg_from,TextSendMessage(text='送信失敗！'))
                print (str(e))
        if setting2[user_id]['setting3'] == True and user_id == setting_[user_id]['ID']:
            try:
                print('ok-13')
                setting2[user_id]['setting3'] = False
                ID_ = IDcheck(user_id)
                print(ID_)
                line_bot_api.multicast([ID_],TextSendMessage(text='【返信が届いたよ！】\n\n' + msg_text))
                line_bot_api.reply_message(msg_from,TextSendMessage(text='送信できたよ！'))
            except Exception as e:
                line_bot_api.reply_message(msg_from,TextSendMessage(text='送信失敗！'))
                print (str(e))
        else:
            items = {'items': [{'type': 'action','action': {'type': 'message','label': '設定する','text': '設定する'}}]}
            line_bot_api.reply_message(msg_from,TextSendMessage(text='表示する文字を設定したいときは\n「設定する」\nと送信してね！\n\n下のボタンからも送信できるよ！',quick_reply=items))





if __name__ == "__main__":
#    app.run()
    port =  int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
