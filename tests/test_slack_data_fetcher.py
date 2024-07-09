"""
File: test_slack_data_fetcher.py
このスクリプトは、slack_data_fetcher.pyの機能をテストするスクリプトです。

機能:
    1.Slack APIからのデータ取得が正しく行われているかを検証
    2.エラーハンドリングが適切に行われているかを検証
ステップ:
    1.必要なモジュールをインポート
    2.モックを使ってSlack APIの呼び出しをシミュレート
    3.データ取得機能のテスト
    4.エラーハンドリングのテスト
"""

import unittest
from unittest.mock import patch, MagicMock
from slack_data_fetcher import fetch_slack_data

class TestSlackDataFetcher(unittest.TestCase):

    @patch('slack_sdk.WebClient.conversations_list')
    @patch('slack_sdk.WebClient.conversations_history')
    def test_fetch_slack_data_success(self, mock_history, mock_list):
        # モックの設定
        mock_list.return_value = {'channels': [{'id': 'C12345', 'name': 'general'}]}
        mock_history.return_value = {'messages': [{'user': 'U12345', 'text': 'Hello', 'ts': '12345', 'reactions': []}]}
        
        # テスト実行
        data = fetch_slack_data()
        
        # 検証
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['channel'], 'general')
        self.assertEqual(data[0]['user'], 'U12345')
    
    @patch('slack_sdk.WebClient.conversations_list', side_effect=Exception('API error'))
    def test_fetch_slack_data_failure(self, mock_list):
        data = fetch_slack_data()
        self.assertEqual(data, [])

if __name__ == '__main__':
    unittest.main()
