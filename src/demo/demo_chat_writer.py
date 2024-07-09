"""
File: demo_chat_writer.py
このスクリプトは、デモ用のチャットを書き込むスクリプトです。
機能:
    1.サンプルチャットデータを読み込み、Slackに投稿
"""
import os
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

def post_chat(channel, text):
    try:
        response = client.chat_postMessage(channel=channel, text=text)
        return response
    except SlackApiError as e:
        print(f"Error posting message: {e.response['error']}")
        return None

def main():
    with open('src/demo/demo_data/sample_chats.json', 'r') as file:
        chats = json.load(file)
    
    for chat in chats:
        channel = chat['channel']
        text = chat['text']
        post_chat(channel, text)

if __name__ == "__main__":
    main()
