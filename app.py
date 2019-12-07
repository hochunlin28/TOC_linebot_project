import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message,send_image_url
from upload import upload_graph,draw_graph1_and_upload,draw_graph2_and_upload

load_dotenv()

str1 = ''
str2 = ''

machine = TocMachine(
    states=["user", "state1", "state2", "state3","state4","state5","state6","state7","state8","state9","state10","state11","state12","state13","state14"],
    transitions=[
        {
            "trigger": "choose",
            "source": "user",
            "dest": "state1",
            "conditions" : "is_going_to_state1"
        },
        {
            "trigger": "choose",
            "source": "user",
            "dest": "state5",
            "conditions" : "is_going_to_state5"
        },
        {
            "trigger": "choose",
            "source": "user",
            "dest": "state13",
            "conditions" : "is_going_to_state13"
        },
        {
            "trigger": "choose",
            "source": "user",
            "dest": "state14",
            "conditions" : "is_going_to_state14"
        },
        {
            "trigger": "enterword",
            "source": "state1",
            "dest": "state2",
            "conditions" : "is_going_to_state2"
        },
        {
            "trigger": "enterword",
            "source": "state1",
            "dest": "state6",
            "conditions" : "is_going_to_state6"
        },
        {
            "trigger": "meme1word",
            "source": "state2",
            "dest": "state3",
        },
        {
            "trigger": "returnpic",
            "source": "state3",
            "dest": "state4",
        },
        {
            "trigger": "enterword",
            "source": "state1",
            "dest": "state7",
            "conditions" : "is_going_to_state7"
        },
        {
            "trigger": "meme2word",
            "source": "state7",
            "dest": "state8",
        },
        {
            "trigger": "returnpic2",
            "source": "state8",
            "dest": "state9",
        },
        {
            "trigger": "enterword",
            "source": "state1",
            "dest": "state10",
            "conditions" : "is_going_to_state10"
        },
        {
            "trigger": "meme3word",
            "source": "state10",
            "dest": "state11",
        },
        {
            "trigger": "returnpic3",
            "source": "state11",
            "dest": "state12",
        },
        {"trigger": "go_back_user", "source": ["state4","state5","state9","state12","state13","state14"], "dest": "user"},
        {"trigger": "go_back_state1", "source": "state6", "dest": "state1"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


#callback url can activate this function
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    global str1
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        if machine.state == 'user':            
                response = machine.choose(event)
        elif machine.state == 'state1':
            response = machine.enterword(event)
        elif machine.state == 'state2':
            str1 = event.message.text
            response = machine.meme1word(event)
        elif machine.state == 'state3':
            response = machine.returnpic(event,str1)
        elif machine.state == 'state7':
            str1 = event.message.text
            response = machine.meme2word(event)
        elif machine.state == 'state8':
            response = machine.returnpic2(event,str1)
        elif machine.state == 'state10':
            str1 = event.message.text
            response = machine.meme3word(event)
        elif machine.state == 'state11':
            response = machine.returnpic3(event,str1)

        """    
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")
        """    
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    #machine.get_graph().draw("fsm.png", prog="dot", format="png")
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
    
