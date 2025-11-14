#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
忘年会幹事AIエージェント (Bonenkai Party Organizer AI Agent)
年末のパーティー企画をサポートするAIエージェントです。
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random


class BonenkaiAgent:
    """忘年会を企画・運営するためのAIエージェント"""
    
    def __init__(self):
        self.participants = []
        self.venue = None
        self.date = None
        self.budget_per_person = 5000  # デフォルト予算（円）
        self.selected_menu = []
        
    def add_participant(self, name: str) -> str:
        """参加者を追加"""
        if name in self.participants:
            return f"❌ {name}さんは既に参加者リストに登録されています。"
        self.participants.append(name)
        return f"✅ {name}さんを参加者リストに追加しました。現在の参加者数: {len(self.participants)}名"
    
    def remove_participant(self, name: str) -> str:
        """参加者を削除"""
        if name not in self.participants:
            return f"❌ {name}さんは参加者リストに見つかりません。"
        self.participants.remove(name)
        return f"✅ {name}さんを参加者リストから削除しました。現在の参加者数: {len(self.participants)}名"
    
    def list_participants(self) -> str:
        """参加者リストを表示"""
        if not self.participants:
            return "📝 参加者はまだいません。"
        return f"📝 参加者リスト ({len(self.participants)}名):\n" + "\n".join(f"  {i+1}. {name}" for i, name in enumerate(self.participants))
    
    def suggest_venues(self, party_type: str = "居酒屋") -> List[str]:
        """会場を提案"""
        venue_suggestions = {
            "居酒屋": [
                "🍶 居酒屋「和楽」- アットホームな雰囲気、飲み放題プランあり",
                "🍺 大衆居酒屋「まる」- コスパ良好、個室完備",
                "🍻 海鮮居酒屋「魚河岸」- 新鮮な魚料理が自慢",
            ],
            "レストラン": [
                "🍽️ イタリアンレストラン「ベラヴィータ」- おしゃれな空間",
                "🥘 和食レストラン「四季」- 高級感のある会場",
                "🍖 ステーキハウス「プライム」- 肉料理が充実",
            ],
            "宴会場": [
                "🏢 ホテル宴会場「グランドホール」- 大人数対応可能",
                "🎪 パーティールーム「フェスタ」- カラオケ・ゲーム設備あり",
                "🌟 貸切スペース「ギャザリング」- プライベート感重視",
            ]
        }
        return venue_suggestions.get(party_type, venue_suggestions["居酒屋"])
    
    def set_venue(self, venue: str) -> str:
        """会場を設定"""
        self.venue = venue
        return f"✅ 会場を「{venue}」に設定しました。"
    
    def calculate_budget(self) -> Dict[str, int]:
        """予算を計算"""
        num_participants = len(self.participants)
        if num_participants == 0:
            return {
                "一人あたり": self.budget_per_person,
                "総予算": 0,
                "参加者数": 0
            }
        total_budget = self.budget_per_person * num_participants
        return {
            "一人あたり": self.budget_per_person,
            "総予算": total_budget,
            "参加者数": num_participants
        }
    
    def set_budget_per_person(self, amount: int) -> str:
        """一人あたりの予算を設定"""
        if amount < 0:
            return "❌ 予算は0円以上で設定してください。"
        self.budget_per_person = amount
        budget_info = self.calculate_budget()
        return f"✅ 一人あたりの予算を{amount}円に設定しました。\n総予算: {budget_info['総予算']:,}円 ({budget_info['参加者数']}名)"
    
    def suggest_dates(self, num_suggestions: int = 3) -> List[str]:
        """日程候補を提案"""
        today = datetime.now()
        # 12月の金曜日を提案
        suggestions = []
        current_date = today
        
        while len(suggestions) < num_suggestions:
            current_date += timedelta(days=1)
            # 12月の金曜日を優先
            if current_date.month == 12 and current_date.weekday() == 4:  # 金曜日
                suggestions.append(current_date.strftime("%Y年%m月%d日（金）"))
            elif len(suggestions) < num_suggestions and current_date.weekday() == 4:
                suggestions.append(current_date.strftime("%Y年%m月%d日（金）"))
        
        return suggestions
    
    def set_date(self, date_str: str) -> str:
        """日程を設定"""
        self.date = date_str
        return f"✅ 日程を「{date_str}」に設定しました。"
    
    def suggest_menu(self, budget_level: str = "中") -> List[str]:
        """メニューを提案"""
        menu_suggestions = {
            "低": [
                "🍗 唐揚げ盛り合わせ",
                "🥗 シーザーサラダ",
                "🍕 マルゲリータピザ",
                "🍜 〆のラーメン",
            ],
            "中": [
                "🐟 刺身盛り合わせ",
                "🍖 焼き鳥盛り合わせ",
                "🍲 もつ鍋",
                "🍣 寿司盛り合わせ",
                "🥘 天ぷら盛り合わせ",
            ],
            "高": [
                "🦞 伊勢海老の鬼殻焼き",
                "🥩 A5和牛ステーキ",
                "🦀 活け蟹の刺身",
                "🍾 シャンパン",
                "🍱 特選握り寿司",
            ]
        }
        return menu_suggestions.get(budget_level, menu_suggestions["中"])
    
    def create_summary(self) -> str:
        """企画サマリーを作成"""
        summary = "=" * 50 + "\n"
        summary += "🎉 忘年会企画サマリー\n"
        summary += "=" * 50 + "\n\n"
        
        summary += f"📅 日程: {self.date if self.date else '未定'}\n"
        summary += f"📍 会場: {self.venue if self.venue else '未定'}\n"
        summary += f"👥 参加者数: {len(self.participants)}名\n"
        
        if self.participants:
            summary += "\n参加者:\n"
            for i, name in enumerate(self.participants, 1):
                summary += f"  {i}. {name}\n"
        
        budget_info = self.calculate_budget()
        summary += f"\n💰 予算:\n"
        summary += f"  一人あたり: {budget_info['一人あたり']:,}円\n"
        summary += f"  総予算: {budget_info['総予算']:,}円\n"
        
        summary += "\n" + "=" * 50 + "\n"
        
        return summary
    
    def get_greeting(self) -> str:
        """挨拶メッセージを返す"""
        greetings = [
            "🎊 こんにちは！忘年会の幹事AIエージェントです。素敵な忘年会を企画しましょう！",
            "🎉 いらっしゃいませ！最高の忘年会を一緒に作り上げましょう！",
            "🌟 ようこそ！忘年会の企画をお手伝いします！",
        ]
        return random.choice(greetings)


def main():
    """メイン処理 - インタラクティブなCLI"""
    agent = BonenkaiAgent()
    print(agent.get_greeting())
    print()
    
    while True:
        print("\n" + "=" * 50)
        print("📋 メニュー:")
        print("1. 参加者を追加")
        print("2. 参加者を削除")
        print("3. 参加者リストを表示")
        print("4. 会場を提案")
        print("5. 会場を設定")
        print("6. 予算を設定")
        print("7. 日程を提案")
        print("8. 日程を設定")
        print("9. メニューを提案")
        print("10. 企画サマリーを表示")
        print("0. 終了")
        print("=" * 50)
        
        try:
            choice = input("\n選択してください (0-10): ").strip()
            
            if choice == "0":
                print("\n👋 ありがとうございました。素敵な忘年会になりますように！")
                break
            
            elif choice == "1":
                name = input("参加者の名前を入力してください: ").strip()
                if name:
                    print(agent.add_participant(name))
            
            elif choice == "2":
                name = input("削除する参加者の名前を入力してください: ").strip()
                if name:
                    print(agent.remove_participant(name))
            
            elif choice == "3":
                print(agent.list_participants())
            
            elif choice == "4":
                print("\n会場タイプを選択してください:")
                print("1. 居酒屋")
                print("2. レストラン")
                print("3. 宴会場")
                venue_type = input("選択 (1-3): ").strip()
                type_map = {"1": "居酒屋", "2": "レストラン", "3": "宴会場"}
                selected_type = type_map.get(venue_type, "居酒屋")
                venues = agent.suggest_venues(selected_type)
                print(f"\n🏢 {selected_type}の提案:")
                for venue in venues:
                    print(f"  • {venue}")
            
            elif choice == "5":
                venue = input("会場名を入力してください: ").strip()
                if venue:
                    print(agent.set_venue(venue))
            
            elif choice == "6":
                try:
                    amount = int(input("一人あたりの予算を入力してください（円）: ").strip())
                    print(agent.set_budget_per_person(amount))
                except ValueError:
                    print("❌ 有効な数値を入力してください。")
            
            elif choice == "7":
                dates = agent.suggest_dates()
                print("\n📅 日程候補:")
                for i, date in enumerate(dates, 1):
                    print(f"  {i}. {date}")
            
            elif choice == "8":
                date = input("日程を入力してください（例: 2024年12月20日）: ").strip()
                if date:
                    print(agent.set_date(date))
            
            elif choice == "9":
                print("\n予算レベルを選択してください:")
                print("1. 低（3000円前後）")
                print("2. 中（5000円前後）")
                print("3. 高（10000円以上）")
                level = input("選択 (1-3): ").strip()
                level_map = {"1": "低", "2": "中", "3": "高"}
                selected_level = level_map.get(level, "中")
                menus = agent.suggest_menu(selected_level)
                print(f"\n🍽️ メニュー提案（{selected_level}）:")
                for menu in menus:
                    print(f"  • {menu}")
            
            elif choice == "10":
                print("\n" + agent.create_summary())
            
            else:
                print("❌ 無効な選択です。0-10の数字を入力してください。")
        
        except KeyboardInterrupt:
            print("\n\n👋 中断されました。ありがとうございました。")
            break
        except Exception as e:
            print(f"❌ エラーが発生しました: {e}")


if __name__ == "__main__":
    main()
