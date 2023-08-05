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

ChromeOptions = Options()
ChromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=ChromeOptions)

# options = Options()
# options.add_argument('--headless')
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome(options=ChromeOptions)

driver.get('https://zukan.pokemon.co.jp/detail/0293')
time.sleep(0.3)
li = []
for i in range(2000):
    tmp = []
    pk_name = driver.find_element(By.XPATH, '/html/body/main/header/div/div/h2/span').text 
    num = driver.find_element(By.XPATH, '/html/body/main/header/div/div/h2/small').text
    num = num[3:]
    print(num) 
    print(pk_name)
    type1 = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/ul/li[2]/dl/dd/a[1]').text
    print(type1)
    if xpath_exist_check(driver, '/html/body/main/div/div/div[1]/ul/li[2]/dl/dd/a[2]'):
        type2 = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/ul/li[2]/dl/dd/a[2]').text
    else:
        type2 = ''
    print(type2)
    if xpath_exist_check(driver, '/html/body/main/header/div/div/h2/span[2]'):
        form = driver.find_element(By.XPATH, '/html/body/main/header/div/div/h2/span[2]').text
    else:
        form = ''
    print(form)
    classify = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/ul/li[1]/dl/dd').text
    print(classify)
    skill1 = ''
    skill2 = ''
    skill3 = ''
    
    img = driver.find_element(By.XPATH, '/html/body/main/header/div/figure/img').get_attribute("src")
    url = driver.current_url 
    id = url[35:]
    print(id)
    tmp.append(id)
    tmp.append(num)
    tmp.append(pk_name)
    tmp.append(form)
    tmp.append(type1)
    tmp.append(type2)
    tmp.append(skill1)
    tmp.append(skill2)
    tmp.append(skill3)
    save(img, id) 
    # if i == 0:
    #     next = '/html/body/main/header/nav/ul/li/a'
    # else:
    #     next = '/html/body/main/header/nav/ul/li[2]/a'
    next = '/html/body/main/header/nav/ul/li[2]/a'
    li.append(tmp)
    tmp = [tmp]
    # ファイル出力
    with open('./list1.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows(tmp)
    driver.find_element(By.XPATH, next).click()
    # time.sleep(2)


driver.quit()
