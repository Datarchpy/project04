"""
File: slack_data_fetcher.py
このスクリプトは、Slack APIからデータを取得するスクリプトです。
機能:
    1.Slack APIを使用してメッセージとリアクションのデータを取得
    2.必要なデータ形式に整形
"""
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def fetch_slack_data():
    slack_token = os.getenv("SLACK_BOT_TOKEN")
    client = WebClient(token=slack_token)
    
    try:
        # チャンネルリストを取得
        channels = client.conversations_list()
        
        data = []
        for channel in channels['channels']:
            # 各チャンネルのメッセージを取得
            messages = client.conversations_history(channel=channel['id'])
            
            for message in messages['messages']:
                # メッセージとリアクションのデータを抽出
                data.append({
                    'channel': channel['name'],
                    'user': message.get('user'),
                    'text': message.get('text'),
                    'ts': message.get('ts'),
                    'reactions': message.get('reactions', [])
                })
                
        return data
    except SlackApiError as e:
        print(f"Error fetching data from Slack: {e.response['error']}")
        return []

if __name__ == "__main__":
    data = fetch_slack_data()
    print(data)
