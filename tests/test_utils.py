"""
File: test_utils.py
このスクリプトは、utils.pyのユーティリティ関数をテストするスクリプトです。

機能:
    1.各ユーティリティ関数の出力が正しいかを検証

ステップ:
    1.必要なモジュールをインポート
    2.各ユーティリティ関数のテスト
"""

import unittest
from utils import format_message, calculate_reactions

class TestUtils(unittest.TestCase):

    def test_format_message(self):
        message = {'user': 'U12345', 'text': 'Hello'}
        formatted = format_message(message)
        self.assertEqual(formatted, 'User: U12345 - Hello')
    
    def test_calculate_reactions(self):
        reactions = [{'count': 2}, {'count': 3}]
        total = calculate_reactions(reactions)
        self.assertEqual(total, 5)

if __name__ == '__main__':
    unittest.main()
