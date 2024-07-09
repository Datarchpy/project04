"""
File: config.py
このスクリプトは、設定ファイルとして、APIキーやトークンなどの設定を管理します。
機能:
    1.APIキーやトークンの読み込みと管理
"""
import os
from dotenv import load_dotenv

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
