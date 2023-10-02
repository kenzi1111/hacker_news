# 課題E

# sleep関数
import time

# requests関数
import requests

# beautifulSoup関数
from bs4 import BeautifulSoup

# re関数
import re

# ハッカーニュースのデータ受け取り
response = requests.get("https://news.ycombinator.com/newest")

# 取得した情報からHTML要素の抽出
soup = BeautifulSoup(response.text, "html.parser")

# https://の関わる要素を抽出
elems = soup.find_all(href=re.compile("https://"))

# HPへの詳細
# print(elems[1])
# HPのタイトル
# print(elems[1].contents[0])
# HPへのURL
# print(elems[1].attrs["href"])

# 取得したハッカーニューズデータのtitleとurlを出力
for i in range(30):
    # for elem in elems:
    title = elems[i + 1].contents[0]
    URL = elems[i + 1].attrs["href"]
    print("{ 'title': '" + title + "' ,'link':'" + URL + "' }")
    time.sleep(1)
