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


def EducationTemplate():
  return(
    TemplateSendMessage(
      alt_text='Education',
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


def ProjectTemplate():
  return(
    TemplateSendMessage(
      alt_text='Project',
      template=CarouselTemplate(
        columns=[
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/G9EAmGu.png',
            title='iSport',
            text='Tools: JavaScript, MySQL and NodeJS',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='iSport details'
              )
            ]
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/MRGiR1j.jpg',
            title='MLB Prediction',
            text='Tools: Python',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='MLB details'
              )
            ]
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/MRGiR1j.jpg',
            title='Selflection',
            text='Tools: Unity and C#',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Selflection details'
              )
            ]
          )
        ]
      )
    )
  )


def ExperienceTemplate():
  return(
    TemplateSendMessage(
      alt_text='Experience',
      template=CarouselTemplate(
        columns=[
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/G9EAmGu.png',
            title='Professional Experience',
            text='Experience that more academic',
            actions=[
              MessageTemplateAction(
                label='AmCAD .CORP',
                text='AmCAD .CORP details'
              ),
              MessageTemplateAction(
                label='NCTU+',
                text='NCTU+ Organization details'
              )
            ]
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/MRGiR1j.jpg',
            title='Other Experience',
            text='Experience of Club or Organization',
            actions=[
              MessageTemplateAction(
                label='Student',
                text='Student Association details'
              ),
              MessageTemplateAction(
                label='PDC',
                text='Pop Dance Club details'
              ),
              MessageTemplateAction(
                label='Area Alumni',
                text='Area Alumni Association details'
              )
            ]
          )
        ]
      )
    )
  )