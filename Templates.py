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
            text='Affiliated Senior High of National Taiwan Normal University',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='HSNU details'
              )
            ]
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/MRGiR1j.jpg',
            title='University',
            text='National Chiao Tung University',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='NCTU details'
              )
            ]
          )
        ]
      )
    )
  )