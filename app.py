from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('+9rpd2oXUcgm3U9JiTomwNwaQPxJJ88D+uGsMPldakfgX1ekAzjNdHHMaMXVOcrLUGp46BKsYlOF6ot/I+WZQ/vk3BxdYlEMTEA2/vaPS6GDorKNX/f6d7rWME28N8kchJAxnSyTw0fQDfks7uauoAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('bae0967b1cab0dddc8fff78f53659c7d')

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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TemplateSendMessage(
        alt_text='這是按鈕訊息板塊',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/XEXfWvJ.jpg',
            title='購物選單',
            text="這是用來展示的板塊",
            actions=[
                DatetimePickerTemplateAction(
                    label="選擇時間",
                    data='data1',
                    mode='date',
                    initial='2019-02-24',
                    max='2019-12-31',
                    min='2019-01-01'
                ),
                MessageTemplateAction(
                    label="清空購物車",
                    text="GOGOGO"
                ),
                URITemplateAction(
                    label="馬上來逛逛",
                    uri="https://tw.shop.com/maso0310"
                )
            ]
        )
    )
    #event.message.text就是用戶傳來的文字訊息
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
