# -*- coding: UTF-8 -*-

#Python module requirement: line-bot-sdk, flask
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *
from Templates import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('+9rpd2oXUcgm3U9JiTomwNwaQPxJJ88D+uGsMPldakfgX1ekAzjNdHHMaMXVOcrLUGp46BKsYlOF6ot/I+WZQ/vk3BxdYlEMTEA2/vaPS6GDorKNX/f6d7rWME28N8kchJAxnSyTw0fQDfks7uauoAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('bae0967b1cab0dddc8fff78f53659c7d')


# UserID handler
def loadUserId():
	try:
		idFile = open('idfile', 'r')
		idList = idFile.readlines()
		idFile.close()
		idList = idList[0].split(';')
		idList.pop()
		return idList
	except Exception as e:
		print(e)
		return None


def saveUserId(userId):
	idFile = open('idfile', 'a')
	idFile.write(userId+';')
	idFile.close()

# Message handler function
def MsgHandle(msg, event):
	if msg == "help":
		line_bot_api.reply_message(event.reply_token, InitialTemplate)
	elif msg == "Start Introduction":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="IIIII!!"))
	elif msg == "List Experience":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="EEEEEEX!!!"))
	elif msg == "List Project":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="PPPPPPP!!!"))
	elif msg == "List Professional & Extracurricular Experience":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="PEE!!!!"))
	elif msg == "List Skill" :
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="SSSSSS!!!"))
	else:
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Without this command: Please enter \"help\""))
	
	return

# 監聽所有來自 /callback 的 Post Request
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


# message handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

	Message = InitialTemplate()
	message = event.message.text
	#event.message.text就是用戶傳來的文字訊息
	if msg == "help":
		line_bot_api.reply_message(event.reply_token, Message)
	elif msg == "Start Introduction":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="IIIII!!"))
	elif msg == "List Experience":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="EEEEEEX!!!"))
	elif msg == "List Project":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="PPPPPPP!!!"))
	elif msg == "List Professional & Extracurricular Experience":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="PEE!!!!"))
	elif msg == "List Skill":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="SSSSSS!!!"))
	else:
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Without this command: Please enter \"help\""))
	
	userId = event.source.user_id
	if not userId in user_id_set:
		user_id_set.add(userId)
		saveUserId(userId)

import os
if __name__ == "__main__":
	
	idList = loadUserId()
	if idList: user_id_set = set(idList)

	try:
		for userId in user_id_set:
			line_bot_api.push_message(userId, TextSendMessage(text='LineBot is ready for you.'))  # Push API example
	except Exception as e:
		print(e)

	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
