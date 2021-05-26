from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from facebook_auth_data import fb_password

opt = webdriver.ChromeOptions()

opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

wdriver = webdriver.Chrome(
    executable_path=r"C:\webriver\chromedriver.exe", options=opt)

try:
    wdriver.get("https://www.facebook.com/")
    time.sleep(3)

    # добавляем поле почты по id
    email_input = wdriver.find_element_by_id("email")

    # очищаем поле
    email_input.clear()

    # для ввода значения в поле используем метод send_keys, вводим номер телефона
    email_input.send_keys("some@mail.com")
    time.sleep(3)

    # заполняем поле пароля
    pass_input = wdriver.find_element_by_id("pass")
    pass_input.clear()
    pass_input.send_keys(fb_password)
    time.sleep(3)

    # эмулируем нажатие клавиши enter и для этого импортируем ключи
    pass_input.send_keys(Keys.ENTER)

    # # эмулируем нажатие на кнопку Войти
    # login_button = wdriver.find_element_by_id("u_0_d_9T").click()
    # time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()