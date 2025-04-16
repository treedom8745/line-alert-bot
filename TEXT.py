from flask import Flask, request
import json
import requests
import os

app = Flask(__name__)

LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN", "")

@app.route("/")
def index():
    return "LINE Alert Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print(json.dumps(body, indent=4))
    return "OK"

    for event in body.get("events", []):
        if event["type"] == "message":
            reply_token = event["replyToken"]
            user_msg = event["message"]["text"]
            reply(reply_token, f"你說的是：{user_msg}")

    return "OK"

def reply(reply_token, text):
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": text}]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
