"""
File: main.py

このスクリプトは、メインスクリプトとして、全体のワークフローを管理します。具体的には、データ取得、データ書き込み、スケジューリングなどの処理を呼び出します。
機能:
    1.全体のワークフローを管理
    2.各モジュールをインポートして実行
"""
from slack_data_fetcher import fetch_slack_data
from google_sheets_writer import write_to_google_sheets
from scheduler import schedule_jobs

def main():
    # Slackからデータを取得
    slack_data = fetch_slack_data()
    
    # データをGoogle Sheetsに書き込む
    write_to_google_sheets(slack_data)
    
    # スケジューリングの設定
    schedule_jobs()

if __name__ == "__main__":
    main()
