import time
import csv
import requests
import unicodedata
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import urllib
import os
import pprint
import urllib.error
import urllib.request
from googletrans import Translator

def save(url, name):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(str(name)+".png", mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def xpath_exist_check(driver, xpath):
    time.sleep(0.1)  
    if len(driver.find_elements(By.XPATH, xpath))!=0:
        return True
    return False

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://ja.wikipedia.org/wiki/%E5%9B%BD%E6%97%97%E3%81%AE%E4%B8%80%E8%A6%A7')
time.sleep(0.3)
translator = Translator()
count = 0
li = []
for i in range(3,20):
    for j in range(1,100): 
        xpf = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[' + str(i) + ']/tbody/tr[' + str(j) + ']/td[3]/span/a/img'
        if not xpath_exist_check(driver, xpf):
            break
        count += 1
        # if count<142:
        #     continue
        url = driver.find_element(By.XPATH, xpf).get_attribute("src")
        xpn = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[' + str(i) + ']/tbody/tr[' + str(j) + ']/td[1]/b/a'
        if not xpath_exist_check(driver, xpn):
            xpn = '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[' + str(i) + ']/tbody/tr[' + str(j) + ']/td[1]/a[1]'
        name = driver.find_element(By.XPATH, xpn).text
        tmp = []
        tmp.append(str(count).zfill(3))
        tmp.append(name)
        name_e = translator.translate(name).text
        # name_e.replace(' ', '_')
        tmp.append(name_e)
        print(tmp)
        li.append(tmp)
        save(url, str(count).zfill(3))
        time.sleep(1)
        # print(count)
# ファイル出力
with open('./list.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(li)
driver.quit()
