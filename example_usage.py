#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
忘年会幹事AIエージェント - 使用例
"""

from bonenkai_agent import BonenkaiAgent


def example_usage():
    """使用例のデモンストレーション"""
    
    print("=" * 60)
    print("🎉 忘年会幹事AIエージェント - 使用例デモ")
    print("=" * 60)
    print()
    
    # エージェントを初期化
    agent = BonenkaiAgent()
    print(agent.get_greeting())
    print()
    
    # 参加者を追加
    print("📝 参加者を追加しています...")
    print(agent.add_participant("田中太郎"))
    print(agent.add_participant("佐藤花子"))
    print(agent.add_participant("鈴木一郎"))
    print(agent.add_participant("高橋美咲"))
    print(agent.add_participant("渡辺健太"))
    print()
    
    # 参加者リストを表示
    print(agent.list_participants())
    print()
    
    # 予算を設定
    print("💰 予算を設定しています...")
    print(agent.set_budget_per_person(6000))
    print()
    
    # 会場を提案
    print("🏢 会場を提案します（居酒屋）:")
    venues = agent.suggest_venues("居酒屋")
    for venue in venues:
        print(f"  • {venue}")
    print()
    
    # 会場を設定
    print(agent.set_venue("居酒屋「和楽」"))
    print()
    
    # 日程を提案
    print("📅 日程候補を提案します:")
    dates = agent.suggest_dates(3)
    for i, date in enumerate(dates, 1):
        print(f"  {i}. {date}")
    print()
    
    # 日程を設定
    print(agent.set_date("2024年12月20日（金）19:00"))
    print()
    
    # メニューを提案
    print("🍽️ メニューを提案します（中予算）:")
    menus = agent.suggest_menu("中")
    for menu in menus:
        print(f"  • {menu}")
    print()
    
    # 企画サマリーを表示
    print(agent.create_summary())
    
    # 予算詳細を表示
    budget_info = agent.calculate_budget()
    print("💡 予算詳細:")
    print(f"  参加者数: {budget_info['参加者数']}名")
    print(f"  一人あたり: {budget_info['一人あたり']:,}円")
    print(f"  総予算: {budget_info['総予算']:,}円")
    print()
    
    print("=" * 60)
    print("✨ デモ完了！素敵な忘年会になりますように！")
    print("=" * 60)


if __name__ == "__main__":
    example_usage()
