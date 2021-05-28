from selenium import webdriver
import time

# в данном скрипте мы отключаем режим веб драйвера

opt = webdriver.ChromeOptions()

opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# отключаем режим веб драйвера

# # для версий браузера Chrome старше 79.0.3945.16
# opt.add_experimental_option("excludeSwitches", ["enable-automation"])
# opt.add_experimental_option("useAutomationExtension", False)

# для более новых версий Chrome, отключение контроля автоматизации
# остальные опции можно посмотреть на сайте https://peter.sh/experiments/chromium-command-line-switches
opt.add_argument("--disable-blink-features=AutomationControlled")

wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe", options=opt)

try:
    # заходим на страницу обнаружения веб драйвера
    wdriver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(7)
except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()






