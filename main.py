import time
from pyautogui import press, typewrite, hotkey
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://app2.pontomais.com.br/login")

browser.maximize_window()

last = browser.find_element("xpath", '//html/body/app-root/dx-drawer/div/div[2]/div[2]/div/app-container/login/div/div[1]/div/div[4]/div[1]/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text')
last.click()
typewrite('seuid/enderecodemail')
hotkey('tab')
time.sleep(2)
typewrite('suasenha')
time.sleep(3)
hotkey('enter')

time.sleep(8)

ultimalocalizacao = browser.find_element("xpath", '//html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/address-time-card-register/div[2]/p[3]/small')

ultimalocalizacao.click()

time.sleep(2)
baterponto = browser.find_element("xpath", '//html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button')

baterponto.click()
time.sleep(7)
browser.quit()




