from selenium import webdriver


try:
    driver = webdriver.Chrome()
    # 사이즈조절
    driver.set_window_size(1400, 1000)  # (가로, 세로)
    driver.get('https://ticket.interpark.com/Gate/TPLogin.asp')
except:
    pass