# -*- coding: UTF-8 -*-

#Python module requirement: line-bot-sdk, flask
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *
import os
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


# listen Post Request from /callback
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

	msg = event.message.text
	UserId = line_bot_api.get_profile(event.source.user_id).user_id

	# Start Section
	if msg == "help":
		Message1 = InitialTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
	# Introduction Section
	elif msg == "Start Introduction":
		line_bot_api.reply_message(event.reply_token, TextSendMessage(text="IIIII!!"))
	# Education Section
	elif msg == "List Education":
		Message1 = EducationTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
	elif msg == "HSNU details":
		Message = TextSendMessage(text='-Graduated from Mathematic and Science Gifted class\n\n-Team leader of Science Fair in Mathematic')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, EducationTemplate())
	elif msg == "NCTU details":
		Message = TextSendMessage(text='-Specialize in Network and Multimedia Engineering Program\n\n-Coursework: Machine Learning, Computer Network\n\n-Expected Date of Graduation: June 2020')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, EducationTemplate())
	# Project Section
	elif msg == "List Project":
		Message1 = ProjectTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
	elif msg == "iSport details":
		Message = TextSendMessage(text='Built a Full-Stack online register/team-up/sign-up platform for National Chiao Tung University Office of Physical Education to help digitalize and improve the signup process')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, ProjectTemplate())
	elif msg == "MLB details":
		Message = TextSendMessage(text='Analyzed the data in MLB official website and designed a machine learning models to predict the salary of player and MLB fame of hall')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, ProjectTemplate())
	elif msg == "Selflection details":
		Message = TextSendMessage(text='Designed and developed 2D platform Action Adventure Game with features of player movement and special role changing skills')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, ProjectTemplate())
	# Experience Section
	elif msg == "List Experience":
		Message1 = ExperienceTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
		# Professional Experience Section
	elif msg == "List Professional Experience":
		Message1 = ProfessionalExperienceTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
	elif msg == "AmCAD .CORP details":
		Message = TextSendMessage(text='-Intern in 2018/7 ~ 2018/9\n\n-Added \"Area Selecting Feature\" and \"Parameter Calculating Feature\" in Tumor Detective Instrument\n\n-Changed its stand-alone version into website version and successfully launched and improved user experience flow')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, ProfessionalExperienceTemplate())
	elif msg == "NCTU+ Organization details":
		Message = TextSendMessage(text='-FrontEnd designer\n\n-Developed all the pages in NCTU plus into Responsive Web Design pages\n\n-Designed Home page and Navber of NCTU plus website by using React JS')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, ProfessionalExperienceTemplate())
		# Other Experience Section
	elif msg == "List Other Experience":
		Message1 = OtherExperienceTemplate()
		line_bot_api.reply_message(event.reply_token, Message1)
	elif msg == "Student Association details":
		Message = TextSendMessage(text='-Information department\n\n-Website maintenance, Database Management, photography\n\n-Hosted NTU. NTHU. NCTU joint Program competition')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, OtherExperienceTemplate())
	elif msg == "Pop Dance Club details":
		Message = TextSendMessage(text='-Public relation chair\n\n-Proposal writing and Copywriting\n\n-Solicit sponsorship from companies such as Red bull')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, OtherExperienceTemplate())
	elif msg == "Area Alumni Association details":
		Message = TextSendMessage(text='-Event planning chair\n\n-Presided over the activities, Event arrangement\n\n-Organize events such as 3-day freshman orientation and winter camp for computer study club')
		line_bot_api.reply_message(event.reply_token, Message)
		line_bot_api.push_message(UserId, OtherExperienceTemplate())
	# Defualt Section
	else:
		Message = TextSendMessage(text='Without command \"' + msg + '\"\nPlease enter \"help\" to continue')
		line_bot_api.reply_message(event.reply_token, Message)


if __name__ == "__main__":

	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
