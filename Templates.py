# -*- coding: UTF-8 -*-

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import *

def InitialTemplate():
  return(
    TemplateSendMessage(
      alt_text='Introdution template',
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
            label="Project have done",
            text="List Project"
          ),
          MessageTemplateAction(
            label="Experience",
            text="List Professional & Extracurricular Experience"
          ),
          MessageTemplateAction(
            label="Skill",
            text="List Skill"
          )
        ]
      )
    )
  )