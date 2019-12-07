from transitions.extensions import GraphMachine

from utils import send_text_message,send_flex_message,send_image_url,send_carousel_message,send_button_message
from upload import upload_graph,draw_graph1_and_upload,draw_graph2_and_upload,draw_graph3_and_upload
from crawler import crawl_img
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    
    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "選擇梗圖"

    def is_going_to_state5(self, event):
        text = event.message.text
        return text.lower() != "選擇梗圖" and text.lower() != "fsm" and text.lower() != "隨機給梗圖"

    def is_going_to_state13(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_state14(self, event):
        text = event.message.text
        return text.lower() == "隨機給梗圖"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "對著貓吼的女人"

    def is_going_to_state7(self, event):
        text = event.message.text
        return text.lower() == "以前到現在"

    def is_going_to_state10(self, event):
        text = event.message.text
        return text.lower() == "女人與沙發女人"

    def is_going_to_state6(self, event):
        text = event.message.text
        return text.lower() != "對著貓吼的女人" and text.lower() != "以前到現在" and text.lower() !="女人與沙發女人"
    
    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "fsm"


    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_carousel_message(reply_token)

    def on_exit_state1(self,event):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "成功選擇圖片，請輸入文字(女人:最大輸入10個字，可多行)")


    def on_exit_state2(self,event):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入文字(貓咪:最大輸入10個字，可多行)")

    def on_enter_state4(self, event,str1):
        print("I'm entering state4")

        reply_token = event.reply_token
        img_url = draw_graph1_and_upload(str1,event.message.text.lower())
        send_image_url(reply_token, img_url)
        
        self.go_back_user() #back to user state

    def on_enter_state5(self, event):
        reply_token = event.reply_token
        send_button_message(reply_token)
        #send_text_message(reply_token, "輸入錯誤")

        self.go_back_user()

    def on_exit_state5(self):
        print("Leaving state5")

    def on_enter_state6(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入錯誤")

        self.go_back_state1()

    def on_exit_state6(self):
        print("Leaving state4")

    def on_enter_state7(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "成功選擇圖片，請輸入文字(以前的我:最大輸入9個字，可多行)")


    def on_exit_state7(self,event):
        print("Leaving state7")  

    def on_enter_state8(self, event):
        print("I'm entering state7")

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入文字(現在的我:最大輸入9個字，可多行)")


    def on_enter_state9(self, event, str1):
        print("I'm entering state3")

        reply_token = event.reply_token
        img_url = draw_graph2_and_upload(str1,event.message.text.lower())
        send_image_url(reply_token, img_url)
        
        self.go_back_user() #back to user state

    def on_exit_state9(self):
        print("Leaving state9")


    def on_enter_state10(self, event):

        reply_token = event.reply_token
        send_text_message(reply_token, "成功選擇圖片，請輸入文字(解釋的女人:最大輸入10個字，可多行)")


    def on_enter_state11(self, event):

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入文字(沙發女人:最大輸入10個字，可多行)")

    def on_enter_state12(self, event,str1):

        reply_token = event.reply_token
        img_url = draw_graph3_and_upload(str1,event.message.text.lower())
        send_image_url(reply_token, img_url)
        
        self.go_back_user() #back to user state

    def on_enter_state13(self, event):

        reply_token = event.reply_token
        send_image_url(event.reply_token, "https://i.imgur.com/KXkGrza.png") 
        self.go_back_user()

    def on_enter_state14(self, event):
        reply_token = event.reply_token

        send_image_url(event.reply_token, crawl_img()) 
        self.go_back_user()

  

    
