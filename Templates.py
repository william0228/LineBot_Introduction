# -*- coding: UTF-8 -*-

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *

def InitialTemplate():
  return(
    TemplateSendMessage(
      alt_text='Introdution',
      template=ButtonsTemplate(
        thumbnail_image_url='https://imgur.com/1WCRDsm.jpg',
        title='Introduction',
        text="Please click the botton",
        actions=[
          MessageTemplateAction(
            label="Brief Introduction",
            text="Start Introduction"
          ),
          MessageTemplateAction(
            label="Education",
            text="List Education"
          ),
          MessageTemplateAction(
            label="Project",
            text="List Project"
          ),
          MessageTemplateAction(
            label="Experience",
            text="List Professional & Extracurricular Experience"
          )
        ]
      )
    )
  )


def IntroductionTemplate():
  return(
    TemplateSendMessage(
      alt_text='Brief Introduction Template',
      template=CarouselTemplate(
        columns=[
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/G9EAmGu.png',
            title='Senior High',
            text='Graduated',
            actions=[
              PostbackTemplateAction(
                label='postback1',
                text='postback text1',
                data='action=buy&itemid=1'
              ),
              MessageTemplateAction(
                label='message1',
                text='message text1'
              ),
              URITemplateAction(
                label='uri1',
                uri='http://example.com/1'
              )
            ]
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/MRGiR1j.jpg',
            title='University',
            text='Specialize',
            actions=[
              PostbackTemplateAction(
                label='postback1',
                text='postback text1',
                data='action=buy&itemid=1'
              ),
              MessageTemplateAction(
                label='message1',
                text='message text1'
              ),
              URITemplateAction(
                label='uri1',
                uri='http://example.com/1'
              )
            ]
          )
        ]
      )
    )
  )