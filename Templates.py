# -*- coding: UTF-8 -*-

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *

def InitialTemplate():
  return  TemplateSendMessage(
            alt_text='Introdution template',
            template=ButtonsTemplate(
              thumbnail_image_url='https://imgur.com/1WCRDsm.jpg',
              title='Introduction',
              text="Please click the botton",
              actions=[
                MessageTemplateAction(
                  label="看抽獎品項",
                  text="有哪些抽獎品項呢？"
                )
              ]
            )
          )