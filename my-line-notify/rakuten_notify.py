import datetime
from datetime import datetime as dt
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

# driver_path = 'chromedriver.exe'
url = 'https://www.rakuten-card.co.jp/e-navi/'

def initialize():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--headless')
    
    global driver
    
    ## selenium3
    # driver = webdriver.Chrome(executable_path=driver_path, options=options)
    # driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    
    ## selenium4
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    sleep(5)
    
        
def user_login():
    driver.get(url)
    sleep(2)
    with open('user_info.json') as f:
        info = json.load(f)
        
    USER_ID = info["USER_ID"]
    PASSWORD = info["PASSWORD"]
    
    elem_user_id = driver.find_element(By.ID, 'u')
    elem_user_id.send_keys(USER_ID)
    sleep(1)
    
    elem_password = driver.find_element(By.ID, 'p')
    elem_password.send_keys(PASSWORD)
    sleep(1)
    
    elem_login_btn = driver.find_element(By.ID, 'loginButton').click()
    sleep(3)
    
def get_date():
    elem_date = driver.find_element(By.CLASS_NAME, 'rd-billInfo-table_month')
    date = elem_date.text
    _date = date.split('\n')
    date = f'''{_date[0]}

[{_date[1]}]:{_date[2]}'''
    return date

def get_amount():
    elem_amount = driver.find_element(By.ID, 'js-rd-billInfo-amount_show')
    amount = elem_amount.text
    return amount
    
def notify(date, amount):
    TOKEN = '747LK4bHrexn6izCY04Y8aUwJi79HTJgVtcs5mbmdtz'
    api_url = 'https://notify-api.line.me/api/notify'
    
    send_contents = f"""{date}
[金額]:{amount}"""
    
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}
    requests.post(api_url,
                  headers = TOKEN_dic,
                  data = send_dic)
    sleep(3)
    
def driver_quit():
    driver.quit()
    
    
def main():
    initialize()
    user_login()
    date = get_date()
    amount = get_amount()
    notify(date, amount)
    driver_quit()
        
if __name__ == '__main__':
    main()

