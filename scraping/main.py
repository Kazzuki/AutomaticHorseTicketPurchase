#モジュールのインポート
import time
import datetime
import json
from bs4 import BeautifulSoup
# import settings as settings
from selenium import webdriver


# ブラウザ起動
driver = webdriver.Chrome(executable_path = "/Users/kazuki/chromedriver")
driver.maximize_window()

# アクセスするURL
TARGET_URL = "https://race.netkeiba.com/odds/index.html?race_id=202206020111"

# 対象サイトへアクセス 
driver.get(TARGET_URL)
time.sleep(2)

html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# １番人気
f_name = soup.select("#name-1_1")[0].get_text()
print(soup.select("#name-1_1")[0].get_text())
f_odds = soup.select("#odds-1_1")[0].get_text()
print(soup.select("#odds-1_1")[0].get_text())
# 2番人気
s_name = soup.select("#name-1_2")[0].get_text()
print(soup.select("#name-1_2")[0].get_text())
s_odds = soup.select("#odds-1_2")[0].get_text()
print(soup.select("#odds-1_2")[0].get_text())


Horse_dict = dict()
Horse_dict['popularHorse'] = [
    {"no": 1, "name": f_name, "odds":f_odds},
    {"no": 2, "name": s_name, "odds":s_odds}
]

t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
d = now.strftime('%Y%m%d%H%M')
Horse_dict['timestamp'] = d
print("++++++++++")
print(json.dumps(Horse_dict, ensure_ascii=False, indent=2))


