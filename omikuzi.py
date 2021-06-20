#-*- coding: utf-8 -*-

import random

fortunes = {1:'凶', 2:'末吉', 3:'小吉', 4:'中吉', 5:'吉', 6:'大吉'}

# おみくじの番号(1~6)をランダムに決定
number = random.randint(1,6)

# 辞書fortunesから番号に対応する運勢を取得する
fortune = fortunes[number]

# 読み込みファイル名を作成
file_name = 'input/fortune_' + str(number) + '.txt'

# ファイルを読み込んで、その中からランダムな1行メッセージとして取得する
with open(file_name, encoding='utf-8') as f:
    messages = f.readline()
    message = random.choice(messages)
print('あなたの運勢は...')

# 運勢を表示
print(fortune)

#メッセージを表示
print(message)