from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from facebook_auth_data import fb_password, fb_phone
import pickle

# импортируем модуль pickle для сохранения cookies

# задаем опции
opt = webdriver.ChromeOptions()

opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe", options=opt)

try:
    # wdriver.get("https://www.facebook.com/")
    # time.sleep(3)
    #
    # # добавляем поле почты по id
    # email_input = wdriver.find_element_by_id("email")
    #
    # # очищаем поле
    # email_input.clear()
    #
    # # для ввода значения в поле используем метод send_keys, вводим номер телефона
    # email_input.send_keys(fb_phone)
    # time.sleep(3)
    #
    # # заполняем поле пароля
    # pass_input = wdriver.find_element_by_id("pass")
    # pass_input.clear()
    # pass_input.send_keys(fb_password)
    # time.sleep(3)
    #
    # # эмулируем нажатие на кнопку Войти
    # login_button = wdriver.find_element_by_id("u_0_d_9T").click()
    # time.sleep(3)
    #
    # # save cookies
    # # после того как мы залогинились на сайте, вызываем метод dump у модуля pickle
    # # в который в качестве параметров передаем 1-м аргументом cookies нашего драйвера
    # # который мы получаем вызвав метод get_cookies, а 2-м аргументом открываем файл на
    # # запись в двоичном формате используя флаг wb
    # pickle.dump(wdriver.get_cookie(), open(f"{fb_phone}_cookies", "wb"))

    # пишем код аутентификации
    wdriver.get("https://some-site.com")
    time.sleep(3)

    # открываем файл cookie на чтение в двоичном формате
    for cookie in pickle.load(open(f"{fb_phone}_cookies", "rb")):
        wdriver.add_cookie(cookie)

    time.sleep(3)
    # после загрузки cookie, обновляем страницу
    wdriver.refresh()
    time.sleep(7)

except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()





