from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

# создаем объект класса UserAgent
useragent = UserAgent()

# создаем объект опций для дальнейшей передачи в браузер
options = webdriver.ChromeOptions()

# мы можем добавить в опции useragent просто наименование браузера
#options.add_argument(f"user-agent={useragent.firefox}")
# можем использовать метод random
options.add_argument(f"user-agent={useragent.random}")

# r используется для того чтобы не приходилось экранировать слеши
wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe", options=options)

try:
    wdriver.get(url="https://ciox.ru/check-user-agent")
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()

# --------------------------------------
# Code for FireFox

# from fake_useragent import UserAgent
#
# useragent = UserAgent()
#
# options = webdriver.FirefoxOptions()
#
# # change ua and override UA
# options.set_preference("general.useragent.override", "Is Not Firefox")
# using random module
# options.set_preference("general.useragent.override", useragent.random)

# wdriver = webdriver.Firefox(executable_path="SomePath/path", options=options)
#
# try:
#     wdriver.get(url="https://ciox.ru/check-user-agent")
#     time.sleep(3)
# except Exception as ex:
#     print(ex)
# finally:
#     wdriver.close()
#     wdriver.quit()


