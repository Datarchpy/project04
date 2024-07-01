"""
共通で使用するユーティリティ関数を定義します。
機能:
共通処理の関数化
"""
def format_message(message):
    # メッセージのフォーマットを行うユーティリティ関数
    return f"User: {message['user']} - {message['text']}"

def calculate_reactions(reactions):
    # リアクションの数を計算するユーティリティ関数
    return sum(reaction['count'] for reaction in reactions)
