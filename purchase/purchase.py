#モジュールのインポート
import time
import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# ブラウザ起動
driver = webdriver.Chrome(executable_path = settings.EXECUTABLE_PATH)
driver.maximize_window()

# アクセスするURL
TARGET_URL = "https://www.ipat.jra.go.jp/"

# 対象サイトへアクセス 
driver.get(TARGET_URL)
time.sleep(2)


# #ログイン
driver.find_element_by_name("inetid").send_keys(settings.INET_ID)
driver.find_element_by_xpath('//*[@title="ログイン"]').click()
time.sleep(2)

# #加入者情報の入力
driver.find_element_by_name("i").send_keys(settings.USER_ID)
driver.find_element_by_name("p").send_keys(settings.PASSWORD)
driver.find_element_by_name("r").send_keys(settings.P_ARS)
driver.find_element_by_xpath('//*[@title="ネット投票メニューへ"]').click()
time.sleep(5)

# try:
#  #マウスオーバーで「OK」ボタンをクリックする
#  actions = ActionChains(driver)
#  actions.move_to_element(driver.find_element_by_xpath("//*[text()='%s']" % "OK")).click().perform()
#  time.sleep(2)
# except:
#  print("お知らせ無し")

#「通常購入」ボタンをクリック
driver.find_element_by_xpath('//*[@title="出馬表から馬を選択する方式です。"]').click()
time.sleep(1)

#競馬場（0, 1, 2, 3）
place_index = 0

#競馬場の選択
elements = driver.find_elements_by_css_selector(".places .btn-block")
elements[place_index].click()
time.sleep(1)

# #レース番号
# RaceNum = 12

# #レース番号の選択
# elements = driver.find_elements_by_css_selector(".races .btn-block")
# elements[ int(RaceNum) - 1 ].click()
# time.sleep(1)

# i = 6

# #単勝馬の選択
# try:
#  elements = driver.find_elements_by_css_selector(".racer-first")
#  elements[i].click()
# except:
#  time.sleep(5)
#  elements = driver.find_elements_by_css_selector(".racer-first")
#  elements[i].click()

# time.sleep(2)

# #馬券の額を入力（単位：100円）
# bet = 1

# try:
#  driver.find_element_by_xpath('//*[@aria-labelledby="select-list-amount-unit"]').send_keys(str( bet ))
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@aria-labelledby="select-list-amount-unit"]').send_keys(str( bet ))

# time.sleep(1)

# #「セット」ボタンをクリック
# try:
#  driver.find_element_by_xpath('//*[@ng-click="vm.onSet()"]').click()
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@ng-click="vm.onSet()"]').click()

# time.sleep(1)

# #「入力終了」ボタンをクリック
# try:
#  driver.find_element_by_xpath('//*[@ng-click="vm.onShowBetList()"]').click()
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@ng-click="vm.onShowBetList()"]').click()

# time.sleep(1)

# #購入金額を入力（単位：円）
# try:
#  driver.find_element_by_xpath('//*[@ng-model="vm.cAmountTotal"]').send_keys(str(bet *100))
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@ng-model="vm.cAmountTotal"]').send_keys(str(bet *100))

# time.sleep(1)

# #「購入する」ボタンをクリック
# try:
#  driver.find_element_by_xpath('//*[@ng-click="vm.clickPurchase()"]').click()
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@ng-click="vm.clickPurchase()"]').click()

# time.sleep(1)

# #マウスオーバーで「OK」ボタンをクリックする
# try:
#  actions = ActionChains(driver)
#  actions.move_to_element(driver.find_element_by_xpath("//*[text()='%s']" % "OK")).click().perform()
# except:
#  time.sleep(5)
#  actions = ActionChains(driver)
#  actions.move_to_element(driver.find_element_by_xpath("//*[text()='%s']" % "OK")).click().perform()


# #トップページへ移動
# try:
#  driver.find_element_by_xpath('//*[@ng-click="vm.clickLogo()"]').click()
# except:
#  time.sleep(5)
#  driver.find_element_by_xpath('//*[@ng-click="vm.clickLogo()"]').click()

# time.sleep(1)
