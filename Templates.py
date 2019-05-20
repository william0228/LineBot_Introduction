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
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkl5qgGtBxZbBu921rynn7HN7C7JaD_Hbi5cMMV5gEgQu2mE-rIw',
                    title='Maso萬事屋百貨',
                    text='百萬種商品一站購足',
                    actions=[
                        MessageTemplateAction(
                            label='關於Maso百貨',
                            text='Maso萬事屋百貨是什麼呢？'
                        ),
                        URITemplateAction(
                            label='點我逛百貨',
                            uri='https://tw.shop.com/maso0310'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.youtaker.com/video2015/promo/images/promo-vip.png',
                    title='註冊成為會員',
                    text='免費獲得會員好康！',
                    actions=[
                        MessageTemplateAction(
                            label='會員優惠資訊',
                            text='我想瞭解註冊會員的好處是什麼'
                        ),
                        URITemplateAction(
                            label='點我註冊會員',
                            uri='https://tw.shop.com/nbts/create-myaccount.xhtml?returnurl=https%3A%2F%2Ftw.shop.com%2F'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/Images/11module/MABrands/opc3Chews_usa_32979_LogoTreatment_200x75.svg',
                    title='獨家商品',
                    text='百種優質獨家商品',
                    actions=[
                        MessageTemplateAction(
                            label='點我看產品目錄',
                            text='獨家商品有哪些？'
                        ),
                        URITemplateAction(
                            label='購買獨家品牌',
                            uri='https://tw.shop.com/info/our-brands'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/GOMAJI1551245496503.jpg',
                    title='優惠資訊',
                    text='隨時更新最新優惠',
                    actions=[
                        MessageTemplateAction(
                            label='抽一個優惠',
                            text='抽優惠資訊'
                        ),
                        URITemplateAction(
                            label='近期優惠資訊',
                            uri='https://tw.shop.com/hot-deals'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/featuredhotdeal/Carrefour1551245288925.jpg',
                    title='最新消息',
                    text='最新活動訊息',
                    actions=[
                        MessageTemplateAction(
                            label='點我看最新消息',
                            text='我想瞭解最新活動'
                        ),
                        URITemplateAction(
                            label='活動資訊頁面',
                            uri='https://tw.shop.com/hot-deals'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='http://img.technews.tw/wp-content/uploads/2014/05/TechNews-624x482.jpg',
                    title='每日新知',
                    text='定期更新相關資訊',
                    actions=[
                        MessageTemplateAction(
                            label='點我看每日新知',
                            text='抽一則每日新知'
                        ),
                        URITemplateAction(
                            label='更多更新內容',
                            uri='https://www.youtube.com/channel/UCpzVAEwEs9AwT2uAOZuxaRQ?view_as=subscriber'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.wecooperation.com/makemoney/%E7%9F%A5%E5%90%8D%E5%A4%A5%E4%BC%B4%E5%95%86%E5%BA%97.png',
                    title='好店分享',
                    text='優質商品介紹與分享',
                    actions=[
                        MessageTemplateAction(
                            label='夥伴商店推薦',
                            text='抽一家夥伴商店'
                        ),
                        URITemplateAction(
                            label='查詢夥伴商店',
                            uri='https://tw.shop.com/stores-a-z'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.shop.com/Image/Images/landingPages/ps-recruit/twn-ps-recruit-header.jpg',
                    title='招商說明',
                    text='與Shop.com合作',
                    actions=[
                        MessageTemplateAction(
                            label='招商資訊',
                            text='如何成為夥伴商店'
                        ),
                        URITemplateAction(
                            label='招商說明報名頁面',
                            uri='https://tw.shop.com/ps_recruit_intro-v.xhtml?tkr=180530162209'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://images.marketamerica.com/site/br/images/logos/awards/torch-award-ethics-2018.jpg',
                    title='微型創業資訊',
                    text='加入網路微型創業趨勢',
                    actions=[
                        MessageTemplateAction(
                            label='瞭解更多',
                            text='什麼是微型創業資訊'
                        ),
                        URITemplateAction(
                            label='公司簡介',
                            uri='https://www.marketamerica.com/?localeCode=zh-Hant&redirect=true'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent-sjc3-1.xx.fbcdn.net/v/t1.0-1/p320x320/50934385_2553136691368417_7766092240367124480_n.jpg?_nc_cat=109&_nc_ht=scontent-sjc3-1.xx&oh=c144a6b45450781ccaf258beb40bc53e&oe=5D228BF1',
                    title='聯繫Maso本人',
                    text='直接聯繫Maso',
                    actions=[
                        MessageTemplateAction(
                            label='誰是Maso?',
                            text='Maso是誰？想認識'
                        ),
                        URITemplateAction(
                            label='加我的LINE',
                            uri='https://line.me/ti/p/KeRocPY6PP'
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