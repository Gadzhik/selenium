from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_log_pass import login, password

# создаем объект опций для дальнейшей передачи в браузер
options = webdriver.ChromeOptions()

# создаем объект класса UserAgent
useragent = UserAgent()

# мы можем добавить в опции useragent просто наименование браузера
#options.add_argument(f"user-agent={useragent.firefox}")
# можем использовать метод random
options.add_argument(f"user-agent={useragent.random}")

# устанавливаем через pip selenium-wire, импортируем и закоментируем импорт драйвера из selenium
# с его помощью мы получим дополнительные возможности для конфигурации веб-драйверов и работы с API
# создадим словарь, где login и password - это наши учетные данные, которые мы импортируем из файла proxy_log_pass
proxy_dict = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

# добавляем параметр seleniumwire_options
wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe",
                           seleniumwire_options=proxy_dict)

try:
    wdriver.get("https://2ip.ru")
    time.sleep(3)
    # wdriver.get(url="https://ciox.ru/check-user-agent")
    # time.sleep(3)
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

# задаем прокси
#proxy = "138.128.98.67:8000"
# получаем доступ к возможностям браузера
#firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# устанавливаем флаг марионетки в true
#firefox_capabilities["marionette"] = True

# передаем словарь для прокси
#firefox_capabilities["proxy"] = {
    #"proxyType": "MANUAL",
    #"httpProxy": proxy,
    #"ftpProxy": proxy,
    #"sslProxy": proxy
#}

# добавляем новый параметр в браузер
# wdriver = webdriver.Firefox(executable_path="SomePath/path", options=options, proxy=proxy)
#
# try:
    # для проверки прокси
    #wdriver.get("https://2ip.ru")
    #time.sleep(3)

#     wdriver.get(url="https://ciox.ru/check-user-agent")
#     time.sleep(3)
# except Exception as ex:
#     print(ex)
# finally:
#     wdriver.close()
#     wdriver.quit()


