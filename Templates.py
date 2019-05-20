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
            thumbnail_image_url='https://imgur.com/MpzVFr4.png',
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
            thumbnail_image_url='https://imgur.com/sUZSMl2.jpeg',
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
            thumbnail_image_url='https://imgur.com/M3qiFAB.png',
            title='Selflection',
            text='Tools: Unity and C#',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Selflection details'
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
          ),
          MessageTemplateAction(
            label='Go Back',
            text='help'
          )
        ]
      )
    )
  )


def ProfessionalExperienceTemplate():
  return(
    TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='顯示在開頭的大圖片網址',
                title='this is menu1',
                text='description1',
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
                        uri='https://ithelp.ithome.com.tw/articles/10195640?sc=iThomeR'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='顯示在開頭的大圖片網址',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='連結2',
                        uri='https://ithelp.ithome.com.tw/articles/10195640?sc=iThomeR'
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
            title='Pop Dance Club',
            text='Public Relation Chair',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Pop Dance Club details'
              )
            ]
          ),
          CarouselColumn(
            title='Area Alumni Association',
            text='Event Planning Chair',
            actions=[
              MessageTemplateAction(
                label='More details',
                text='Area Alumni Association details'
              )
            ]
          ),
          CarouselColumn(
            #thumbnail_image_url='https://imgur.com/Dcca5IM.png',
            title='Back to previous',
            text='Back to previous step',
            actions=[
              MessageTemplateAction(
                label='go back right now',
                text='List Experience'
              )
            ]
          )
        ]
      )
    )
  )