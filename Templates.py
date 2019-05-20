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
            text="List Experience"
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
          ),
          CarouselColumn(
            thumbnail_image_url='https://imgur.com/Dcca5IM.png',
            title='Back to previous',
            text='Back to previous step',
            actions=[
              MessageTemplateAction(
                label='go back right now',
                text='help'
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
      template=ButtonsTemplate(
        title='Experience',
        text="Please click the botton",
        actions=[
          MessageTemplateAction(
            label="Professional",
            text="List Professional Experience"
          ),
          MessageTemplateAction(
            label="Other",
            text="List Other Experience"
          )
        ]
      )
    )
  )


def ProfessionalExperienceTemplate():
  return(
    TemplateSendMessage(
      alt_text='Professional Experience',
      template=CarouselTemplate(
        columns=[
          CarouselColumn(
            title='AmCAD .CORP',
            text='Intern',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='AmCAD .CORP details'
              )
            ]
          ),
          CarouselColumn(
            title='NCTU+',
            text='Web Development',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='NCTU+ Organization details'
              )
            ]
          )
        ]
      )
    )
  )


def OtherExperienceTemplate():
  return(
    TemplateSendMessage(
      alt_text='Other Experience',
      template=CarouselTemplate(
        columns=[
          CarouselColumn(
            title='Student Association',
            text='Information Department',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Student Association details'
              )
            ]
          ),
          CarouselColumn(
            title='Pop Dance Club+',
            text='Public Relation Chair',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Pop Dance Club details'
              )
            ]
          ),
          CarouselColumn(
            title='Area Alumni Association+',
            text='Event Planning Chair',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Area Alumni Association details'
              )
            ]
          )
        ]
      )
    )
  )