# 忘年会幹事AIエージェント (Bonenkai Party Organizer AI Agent)

年末のパーティー企画をサポートするAIエージェントです。

## 機能

- 👥 **参加者管理**: 参加者の追加・削除・一覧表示
- 🏢 **会場提案**: 居酒屋、レストラン、宴会場の提案
- 💰 **予算計算**: 一人あたりの予算設定と総予算の自動計算
- 📅 **日程提案**: 最適な日程候補の提案
- 🍽️ **メニュー提案**: 予算に応じたメニューの提案
- 📋 **企画サマリー**: 忘年会の企画内容の一覧表示

## 使い方

### インタラクティブモード

```bash
python3 bonenkai_agent.py
```

メニューから選択して対話的に忘年会を企画できます。

### プログラムから使用

```python
from bonenkai_agent import BonenkaiAgent

# エージェントを初期化
agent = BonenkaiAgent()

# 参加者を追加
agent.add_participant("田中太郎")
agent.add_participant("佐藤花子")
agent.add_participant("鈴木一郎")

# 予算を設定
agent.set_budget_per_person(5000)

# 会場を提案
venues = agent.suggest_venues("居酒屋")
for venue in venues:
    print(venue)

# 会場を設定
agent.set_venue("居酒屋「和楽」")

# 日程を提案
dates = agent.suggest_dates()
for date in dates:
    print(date)

# 日程を設定
agent.set_date("2024年12月20日（金）")

# メニューを提案
menus = agent.suggest_menu("中")
for menu in menus:
    print(menu)

# サマリーを表示
print(agent.create_summary())
```

## 出力例

```
==================================================
🎉 忘年会企画サマリー
==================================================

📅 日程: 2024年12月20日（金）
📍 会場: 居酒屋「和楽」
👥 参加者数: 3名

参加者:
  1. 田中太郎
  2. 佐藤花子
  3. 鈴木一郎

💰 予算:
  一人あたり: 5,000円
  総予算: 15,000円

==================================================
```

## API リファレンス

### BonenkaiAgent クラス

#### メソッド

- `add_participant(name: str) -> str`: 参加者を追加
- `remove_participant(name: str) -> str`: 参加者を削除
- `list_participants() -> str`: 参加者リストを表示
- `suggest_venues(party_type: str = "居酒屋") -> List[str]`: 会場を提案
- `set_venue(venue: str) -> str`: 会場を設定
- `calculate_budget() -> Dict[str, int]`: 予算を計算
- `set_budget_per_person(amount: int) -> str`: 一人あたりの予算を設定
- `suggest_dates(num_suggestions: int = 3) -> List[str]`: 日程候補を提案
- `set_date(date_str: str) -> str`: 日程を設定
- `suggest_menu(budget_level: str = "中") -> List[str]`: メニューを提案
- `create_summary() -> str`: 企画サマリーを作成
- `get_greeting() -> str`: 挨拶メッセージを取得

## 要件

- Python 3.6以上

## ライセンス

MIT License
