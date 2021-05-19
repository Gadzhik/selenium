from selenium import webdriver
import time
import random

#url = "https://mvideo.ru"

# создаем список user-agent
user_agents_list = [
    "Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.1.0; LM-X410(FG)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10"
]

# создаем объект опций для дальнейшей передачи в браузер
options = webdriver.ChromeOptions()
# add_arguments дает возможность добавлять все, что нужно для работы
#options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36")

options.add_argument(f"user-agent={random.choice(user_agents_list)}")


# r используется для того чтобы не приходилось экранировать слеши
wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe", options=options)


try:
    # узнаем наш user-agent
    wdriver.get(url="https://ciox.ru/check-user-agent")
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()
















