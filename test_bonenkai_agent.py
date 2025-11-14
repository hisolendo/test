#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
忘年会幹事AIエージェントのテストスクリプト
"""

from bonenkai_agent import BonenkaiAgent


def test_participant_management():
    """参加者管理機能のテスト"""
    print("🧪 参加者管理機能のテスト...")
    agent = BonenkaiAgent()
    
    # 参加者追加
    result = agent.add_participant("田中太郎")
    assert "田中太郎" in result
    assert "追加" in result
    
    result = agent.add_participant("佐藤花子")
    assert "佐藤花子" in result
    
    # 重複追加のテスト
    result = agent.add_participant("田中太郎")
    assert "既に" in result
    
    # 参加者数の確認
    assert len(agent.participants) == 2
    
    # 参加者削除
    result = agent.remove_participant("田中太郎")
    assert "削除" in result
    assert len(agent.participants) == 1
    
    # 存在しない参加者の削除
    result = agent.remove_participant("存在しない人")
    assert "見つかりません" in result
    
    print("✅ 参加者管理機能のテスト完了")


def test_budget_calculation():
    """予算計算機能のテスト"""
    print("🧪 予算計算機能のテスト...")
    agent = BonenkaiAgent()
    
    # デフォルト予算の確認
    assert agent.budget_per_person == 5000
    
    # 参加者なしの予算計算
    budget = agent.calculate_budget()
    assert budget["総予算"] == 0
    assert budget["参加者数"] == 0
    
    # 参加者ありの予算計算
    agent.add_participant("田中太郎")
    agent.add_participant("佐藤花子")
    agent.add_participant("鈴木一郎")
    
    budget = agent.calculate_budget()
    assert budget["総予算"] == 15000  # 5000 * 3
    assert budget["参加者数"] == 3
    
    # 予算変更
    agent.set_budget_per_person(8000)
    budget = agent.calculate_budget()
    assert budget["総予算"] == 24000  # 8000 * 3
    
    print("✅ 予算計算機能のテスト完了")


def test_venue_suggestion():
    """会場提案機能のテスト"""
    print("🧪 会場提案機能のテスト...")
    agent = BonenkaiAgent()
    
    # 居酒屋の提案
    venues = agent.suggest_venues("居酒屋")
    assert len(venues) > 0
    assert any("居酒屋" in v for v in venues)
    
    # レストランの提案
    venues = agent.suggest_venues("レストラン")
    assert len(venues) > 0
    assert any("レストラン" in v for v in venues)
    
    # 宴会場の提案
    venues = agent.suggest_venues("宴会場")
    assert len(venues) > 0
    
    # 会場設定
    result = agent.set_venue("テスト会場")
    assert agent.venue == "テスト会場"
    
    print("✅ 会場提案機能のテスト完了")


def test_date_suggestion():
    """日程提案機能のテスト"""
    print("🧪 日程提案機能のテスト...")
    agent = BonenkaiAgent()
    
    # 日程提案
    dates = agent.suggest_dates(3)
    assert len(dates) == 3
    
    # 日程設定
    result = agent.set_date("2024年12月20日")
    assert agent.date == "2024年12月20日"
    
    print("✅ 日程提案機能のテスト完了")


def test_menu_suggestion():
    """メニュー提案機能のテスト"""
    print("🧪 メニュー提案機能のテスト...")
    agent = BonenkaiAgent()
    
    # 低予算メニュー
    menus = agent.suggest_menu("低")
    assert len(menus) > 0
    
    # 中予算メニュー
    menus = agent.suggest_menu("中")
    assert len(menus) > 0
    
    # 高予算メニュー
    menus = agent.suggest_menu("高")
    assert len(menus) > 0
    
    print("✅ メニュー提案機能のテスト完了")


def test_summary_creation():
    """サマリー作成機能のテスト"""
    print("🧪 サマリー作成機能のテスト...")
    agent = BonenkaiAgent()
    
    # 基本サマリー
    summary = agent.create_summary()
    assert "忘年会企画サマリー" in summary
    assert "未定" in summary
    
    # データ追加後のサマリー
    agent.add_participant("田中太郎")
    agent.add_participant("佐藤花子")
    agent.set_venue("テスト会場")
    agent.set_date("2024年12月20日")
    agent.set_budget_per_person(5000)
    
    summary = agent.create_summary()
    assert "田中太郎" in summary
    assert "佐藤花子" in summary
    assert "テスト会場" in summary
    assert "2024年12月20日" in summary
    assert "5,000" in summary
    
    print("✅ サマリー作成機能のテスト完了")


def test_greeting():
    """挨拶機能のテスト"""
    print("🧪 挨拶機能のテスト...")
    agent = BonenkaiAgent()
    
    greeting = agent.get_greeting()
    assert len(greeting) > 0
    assert "忘年会" in greeting or "幹事" in greeting or "AI" in greeting
    
    print("✅ 挨拶機能のテスト完了")


def run_all_tests():
    """全テストを実行"""
    print("\n" + "=" * 60)
    print("🎯 忘年会幹事AIエージェント - テスト開始")
    print("=" * 60 + "\n")
    
    try:
        test_participant_management()
        test_budget_calculation()
        test_venue_suggestion()
        test_date_suggestion()
        test_menu_suggestion()
        test_summary_creation()
        test_greeting()
        
        print("\n" + "=" * 60)
        print("✨ すべてのテストが成功しました！")
        print("=" * 60 + "\n")
        return True
        
    except AssertionError as e:
        print(f"\n❌ テスト失敗: {e}")
        return False
    except Exception as e:
        print(f"\n❌ エラー発生: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
