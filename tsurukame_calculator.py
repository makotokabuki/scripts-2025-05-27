#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
鶴亀算を解くPythonスクリプト

鶴と亀が合計で何匹いて、足の総数が何本かわかっている時に、
鶴と亀がそれぞれ何匹いるかを計算します。

鶴：足2本
亀：足4本
"""

def tsurukame_calculator(total_animals, total_legs):
    """
    鶴亀算を計算する関数
    
    Args:
        total_animals (int): 鶴と亀の総数
        total_legs (int): 足の総数
    
    Returns:
        tuple: (鶴の数, 亀の数) または None（解なしの場合）
    """
    
    # 方程式を解く
    # 鶴をx匹、亀をy匹とすると
    # x + y = total_animals  ... (1)
    # 2x + 4y = total_legs   ... (2)
    
    # (1)からx = total_animals - y
    # これを(2)に代入すると
    # 2(total_animals - y) + 4y = total_legs
    # 2*total_animals - 2y + 4y = total_legs
    # 2*total_animals + 2y = total_legs
    # 2y = total_legs - 2*total_animals
    # y = (total_legs - 2*total_animals) / 2
    
    # 亀の数を計算
    kame_count = (total_legs - 2 * total_animals) / 2
    
    # 鶴の数を計算
    tsuru_count = total_animals - kame_count
    
    # 計算結果が正の整数かチェック
    if (kame_count >= 0 and tsuru_count >= 0 and 
        kame_count.is_integer() and tsuru_count.is_integer()):
        return int(tsuru_count), int(kame_count)
    else:
        return None

def main():
    """メイン関数"""
    print("=== 鶴亀算計算機 ===")
    print()
    
    # サンプル問題1
    print("【サンプル問題1】")
    total_animals = 5
    total_legs = 14
    print(f"鶴と亀が合わせて{total_animals}匹、足が合わせて{total_legs}本の場合")
    
    result = tsurukame_calculator(total_animals, total_legs)
    if result:
        tsuru, kame = result
        print(f"答え：鶴 {tsuru}羽、亀 {kame}匹")
        # 検算
        print(f"検算：{tsuru} + {kame} = {tsuru + kame}匹")
        print(f"      {tsuru}×2 + {kame}×4 = {tsuru*2 + kame*4}本")
    else:
        print("解なし（条件を満たす組み合わせがありません）")
    
    print()
    
    # サンプル問題2
    print("【サンプル問題2】")
    total_animals = 10
    total_legs = 28
    print(f"鶴と亀が合わせて{total_animals}匹、足が合わせて{total_legs}本の場合")
    
    result = tsurukame_calculator(total_animals, total_legs)
    if result:
        tsuru, kame = result
        print(f"答え：鶴 {tsuru}羽、亀 {kame}匹")
        # 検算
        print(f"検算：{tsuru} + {kame} = {tsuru + kame}匹")
        print(f"      {tsuru}×2 + {kame}×4 = {tsuru*2 + kame*4}本")
    else:
        print("解なし（条件を満たす組み合わせがありません）")
    
    print()
    
    # ユーザー入力モード
    print("【自分で問題を入力してみましょう】")
    try:
        animals = int(input("鶴と亀の合計数を入力してください: "))
        legs = int(input("足の合計数を入力してください: "))
        
        result = tsurukame_calculator(animals, legs)
        if result:
            tsuru, kame = result
            print(f"\n答え：鶴 {tsuru}羽、亀 {kame}匹")
            # 検算
            print(f"検算：{tsuru} + {kame} = {tsuru + kame}匹")
            print(f"      {tsuru}×2 + {kame}×4 = {tsuru*2 + kame*4}本")
        else:
            print("\n解なし（条件を満たす組み合わせがありません）")
            
    except ValueError:
        print("数値を正しく入力してください。")
    except KeyboardInterrupt:
        print("\n終了します。")

if __name__ == "__main__":
    main()
