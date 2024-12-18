from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time

login_id = 'login_id'
login_pwd = 'login_pwd'
match_date = 12.25

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(options=chrome_options)
# 사이즈조절
driver.set_window_size(1400, 1000)  # (가로, 세로)
# driver.get('https://kovo.co.kr/KOVO/login')
driver.get('https://kovo.co.kr/skywalkers/login')
driver.implicitly_wait(100)
user_id = driver.find_element(By.XPATH, '/html/body/div/article/div/div/div[1]/form/div[1]/input[1]')
user_id.send_keys(login_id)
user_pwd = driver.find_element(By.XPATH, '/html/body/div/article/div/div/div[1]/form/div[1]/input[2]')
user_pwd.send_keys(login_pwd)
user_pwd.send_keys(Keys.ENTER)

time.sleep(3)

driver.get('https://kovo.co.kr/KOVO/ticket/ticket-buy')

driver.implicitly_wait(5)

driver.find_element(By.XPATH, '/html/body/div[1]/article/div/article/section/article/section[3]/div/div[2]/div/div[10]/button').click()
time.sleep(3)
# driver.get('https://facility.ticketlink.co.kr/reserve/product/51358/schedule/sports?teamId=133&menuIndex=reserve')

while len(driver.window_handles) == 1:
        pass

driver.switch_to.window(driver.window_handles[1])

driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div/table/tbody/tr[1]/td[4]/a').click()

print(driver.window_handles)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/button').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[6]/a/div/span[1]').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[6]/div/div/span/a').click()



