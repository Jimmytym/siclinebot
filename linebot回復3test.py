from flask import Flask
app = Flask(__name__)

from flask import request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, PostbackEvent, TextSendMessage, LocationSendMessage,TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, PostbackTemplateAction, URITemplateAction, CarouselTemplate, CarouselColumn, ImageCarouselTemplate, ImageCarouselColumn
from urllib.parse import parse_qsl

line_bot_api = LineBotApi('SY5EUzI2X0fRfX9jo2t1hL6bEnuTun3bp9oZ43l1itN7CpP2tO2xcNbHagDKh2pGT5B5JffujaV6MnLo2LWY+R4fch2hAvc76IDJjtyjlQi+Lso1+leEFhSBvLZ6RtYJURbENKQntOlxYBnNJ1O/tWVdBgDKh2pGT5B5D')
handler = WebhookHandler('f18653df6728922e6c2f7ceb3adb89d4')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '@加入社群':
        sendButton(event)
    # elif mtext == '洽詢管道':
    #     try:
    #         message = [  #串列
                
    #             TextSendMessage(  #傳送文字
    #                 text = "如果有其他的問題，歡迎洽詢以下管道喔"
    #             ),
                
    #               TextSendMessage(  #傳送文字
    #                 text = "運傳系系辦電話：（04）22213108*6131"
    #             ),
                
    #             #  TextSendMessage(  #傳送文字
    #             #     text = "運傳系官網網址：https://sic.ntus.edu.tw/"
    #             # )
    #         #       LocationSendMessage(
    #         #     title='台灣體育運動大學',
    #         #     address='台中市北區雙十路一段16號',
    #         #     latitude=24.1490451,  #緯度
    #         #     longitude=120.6852107  #經度
    #         # )
                  
    #         ]
    #         line_bot_api.reply_message(event.reply_token,message)
    #     except:
    #         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

    # elif mtext == '@確認樣板':
    #     sendConfirm(event)

    # elif mtext == '@轉盤樣板':
    #     sendCarousel(event)

    # elif mtext == '@圖片轉盤':
    #     sendImgCarousel(event)

    # elif mtext == '@購買披薩':
    #     sendPizza(event)

    # elif mtext == '@yes':
    #     sendYes(event)
        

@handler.add(PostbackEvent)  #PostbackTemplateAction觸發此事件
# def handle_postback(event):
#     backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
#     if backdata.get('action') == 'buy':
#         sendBack_buy(event, backdata)
#     elif backdata.get('action') == 'sell':
#         sendBack_sell(event, backdata)

def sendButton(event):  #按鈕樣版
    try:
        message = TemplateSendMessage(
            alt_text='加入社群',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',  #顯示的圖片
                title='想了解我們的最新消息與活動嗎?歡迎追蹤與加入',  #主標題
                text='以下是我們的官方社群帳號：',  #副標題
                actions=[
                    URITemplateAction(  #開啟網頁
                        label='運傳系系辦臉書社團',
                        uri='https://www.facebook.com/groups/440958489250085'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='運傳系學會粉絲團',
                        uri='https://www.facebook.com/search/top?q=%E8%87%BA%E9%AB%94%E9%81%8B%E5%82%B3%E7%B3%BB%E5%AD%B8%E6%9C%83'
                    ),
                    URITemplateAction(  #開啟網頁
                        label='運傳系系學會IG',
                        uri='https://www.instagram.com/ntus.sic/'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendConfirm(event):  #確認樣板
#     try:
#         message = TemplateSendMessage(
#             alt_text='確認樣板',
#             template=ConfirmTemplate(
#                 text='你確定要購買這項商品嗎？',
#                 actions=[
#                     MessageTemplateAction(  #按鈕選項
#                         label='是',
#                         text='@yes'
#                     ),
#                     MessageTemplateAction(
#                         label='否',
#                         text='@no'
#                     )
#                 ]
#             )
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendCarousel(event):  #轉盤樣板
#     try:
#         message = TemplateSendMessage(
#             alt_text='轉盤樣板',
#             template=CarouselTemplate(
#                 columns=[
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
#                         title='這是樣板一',
#                         text='第一個轉盤樣板',
#                         actions=[
#                             MessageTemplateAction(
#                                 label='文字訊息一',
#                                 text='賣披薩'
#                             ),
#                             URITemplateAction(
#                                 label='連結文淵閣網頁',
#                                 uri='http://www.e-happy.com.tw'
#                             ),
#                             PostbackTemplateAction(
#                                 label='回傳訊息一',
#                                 data='action=sell&item=披薩'
#                             ),
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/qaAdBkR.png',
#                         title='這是樣板二',
#                         text='第二個轉盤樣板',
#                         actions=[
#                             MessageTemplateAction(
#                                 label='文字訊息二',
#                                 text='賣飲料'
#                             ),
#                             URITemplateAction(
#                                 label='連結台大網頁',
#                                 uri='http://www.ntu.edu.tw'
#                             ),
#                             PostbackTemplateAction(
#                                 label='回傳訊息二',
#                                 data='action=sell&item=飲料'
#                             ),
#                         ]
#                     )
#                 ]
#             )
#         )
#         line_bot_api.reply_message(event.reply_token,message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendImgCarousel(event):  #圖片轉盤
#     try:
#         message = TemplateSendMessage(
#             alt_text='圖片轉盤樣板',
#             template=ImageCarouselTemplate(
#                 columns=[
#                     ImageCarouselColumn(
#                         image_url='https://i.imgur.com/4QfKuz1.png',
#                         action=MessageTemplateAction(
#                             label='文字訊息',
#                             text='賣披薩'
#                         )
#                     ),
#                     ImageCarouselColumn(
#                         image_url='https://i.imgur.com/qaAdBkR.png',
#                         action=PostbackTemplateAction(
#                             label='回傳訊息',
#                             data='action=sell&item=飲料'
#                         )
#                     )
#                 ]
#             )
#         )
#         line_bot_api.reply_message(event.reply_token,message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendPizza(event):
#     try:
#         message = TextSendMessage(
#             text = '感謝您購買披薩，我們將盡快為您製作。'
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendYes(event):
#     try:
#         message = TextSendMessage(
#             text='感謝您的購買，\n我們將盡快寄出商品。',
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendBack_buy(event, backdata):  #處理Postback
#     try:
#         text1 = '感謝您購買披薩，我們將盡快為您製作。\n(action 的值為 ' + backdata.get('action') + ')'
#         text1 += '\n(可將處理程式寫在此處。)'
#         message = TextSendMessage(  #傳送文字
#             text = text1
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

# def sendBack_sell(event, backdata):  #處理Postback
#     try:
#         message = TextSendMessage(  #傳送文字
#             text = '點選的是賣 ' + backdata.get('item')
#         )
#         line_bot_api.reply_message(event.reply_token, message)
#     except:
#         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

if __name__ == '__main__':
    app.run()
