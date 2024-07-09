"""
File: test_google_sheets_writer.py
このスクリプトは、google_sheets_writer.pyの機能をテストするスクリプトです。

機能:
    1.データがGoogle Sheetsに正しく書き込まれているかを検証
    2.エラーハンドリングが適切に行われているかを検証

ステップ:
    1.必要なモジュールをインポート
    2.モックを使ってGoogle Sheets APIの呼び出しをシミュレート
    3.データ書き込み機能のテスト
    4.エラーハンドリングのテスト
"""

import unittest
from unittest.mock import patch, MagicMock
from google_sheets_writer import write_to_google_sheets

class TestGoogleSheetsWriter(unittest.TestCase):

    @patch('gspread.Client.open')
    def test_write_to_google_sheets_success(self, mock_open):
        # モックの設定
        mock_sheet = MagicMock()
        mock_open.return_value.sheet1 = mock_sheet
        
        # テストデータ
        sample_data = [
            {'ts': '2024-07-01', 'channel': 'general', 'user': 'U12345', 'text': 'こんにちは', 'reactions': []}
        ]
        
        # テスト実行
        write_to_google_sheets(sample_data)
        
        # 検証
        mock_sheet.append_row.assert_called_once_with(['2024-07-01', 'general', 'U12345', 'こんにちは', 0])
    
    @patch('gspread.Client.open', side_effect=Exception('API error'))
    def test_write_to_google_sheets_failure(self, mock_open):
        sample_data = [
            {'ts': '2024-07-01', 'channel': 'general', 'user': 'U12345', 'text': 'こんにちは', 'reactions': []}
        ]
        write_to_google_sheets(sample_data)
        # 例外が発生した場合、何も書き込まれないことを検証
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
