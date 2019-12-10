
#used to defined send message function


import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage,PostbackTemplateAction,URITemplateAction,ButtonsTemplate,MessageTemplateAction,ImageSendMessage
from linebot.models import CarouselTemplate,CarouselColumn,MessageAction
from linebot.models import ButtonsTemplate
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_flex_message(reply_token):
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='韓導',
            text='發大財',
            thumbnail_image_url='https://i.imgur.com/uIbSv9c.png',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='發財之刃',
                    uri='https://www.youtube.com/watch?v=V79zSSDweUA'
                ),
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='postback1'
                )
            ]
        )
    )
    line_bot_api = LineBotApi(channel_access_token) 
    line_bot_api.reply_message(reply_token,buttons_template)

    return "OK"

def send_image_url(reply_token, img_url):

    line_bot_api = LineBotApi(channel_access_token) 
    line_bot_api.reply_message(reply_token,ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))

    return "OK"

def send_carousel_message(reply_token):
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns = [
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/3xZtdeP.png',
                    title='對著貓吼的女人',
                    text='使用時機: 貓很可愛><',
                    actions=[
                        MessageAction(
                            label='選擇',
                            text='對著貓吼的女人'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/ZhetHU2.png',
                    title='以前到現在',
                    text='使用時機: 自己想法的轉變',
                    actions=[
                        MessageAction(
                            label='選擇',
                            text='以前到現在'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/RnlLIcm.png',
                    title='女人與沙發女人',
                    text='使用時機: 當你解釋時別人聽不懂在講三小',
                    actions=[
                        MessageAction(
                            label='選擇',
                            text='女人與沙發女人'
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api = LineBotApi(channel_access_token) 
    line_bot_api.reply_message(reply_token,carousel_template_message)
    
    return "OK"

def send_button_message(reply_token):
    buttons_template_message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/8TQDeIq.jpg',
        title='歡迎使用貓貓梗圖產生器',
        text='所有功能',
        actions=[
            
            MessageAction(
                label='選擇梗圖',
                text='選擇梗圖'
            ),
            MessageAction(
                label='fsm',
                text='fsm'
            ),
            MessageAction(
                label='隨機給梗圖',
                text='隨機給梗圖'
            )
        ]
    )
    )
    line_bot_api = LineBotApi(channel_access_token) 
    line_bot_api.reply_message(reply_token,buttons_template_message)

    return "OK"

