"""
取得したデータをGoogle Sheetsに書き込むスクリプトです。
機能:
Google Sheets APIを使用してデータを書き込む
データの整形とシートへの書き込み処理
"""
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def write_to_google_sheets(data):
    # Google Sheets APIの認証
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
    client = gspread.authorize(creds)
    
    sheet = client.open("Slack Data").sheet1
    
    # データの書き込み
    for entry in data:
        row = [entry['ts'], entry['channel'], entry['user'], entry['text'], len(entry['reactions'])]
        sheet.append_row(row)

if __name__ == "__main__":
    sample_data = [
        {'ts': '2024-07-01', 'channel': 'general', 'user': 'U12345', 'text': 'こんにちは', 'reactions': []}
    ]
    write_to_google_sheets(sample_data)
