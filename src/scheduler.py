"""
スケジューリング用のスクリプトです。Cronジョブなどで定期的に実行するための設定を行います。
機能:
スケジュールジョブの設定と管理
"""
import schedule
import time
from slack_data_fetcher import fetch_slack_data
from google_sheets_writer import write_to_google_sheets

def job():
    slack_data = fetch_slack_data()
    write_to_google_sheets(slack_data)

def schedule_jobs():
    schedule.every().day.at("00:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_jobs()
