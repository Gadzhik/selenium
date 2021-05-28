from selenium import webdriver
import time
from vk_auth_data import vk_password, vk_phone

opt = webdriver.ChromeOptions()

# оключаем обнаружение ua
opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# отключаем обнаружение режима веб драйвера
opt.add_argument("--disable-blink-features=AutomationControlled")

# запускаем веб драйвер в фоновом режиме(headless mode)
# 1-способ
#opt.add_argument("--headless")
# 2-способ
opt.headless = True

wdriver = webdriver.Chrome(executable_path=r"C:\webriver\chromedriver.exe", options=opt)

try:
    wdriver.get("https://vk.com/")
    time.sleep(3)

    # Выводим текст, для понимания на каком этапе мы находимся
    print("Passing authentication")
    # добавляем поле почты по id
    email_input = wdriver.find_element_by_id("email")

    # очищаем поле
    email_input.clear()

    # для ввода значения в поле используем метод send_keys, вводим номер телефона
    email_input.send_keys(vk_phone)
    time.sleep(3)

    # заполняем поле пароля
    pass_input = wdriver.find_element_by_id("pass")
    pass_input.clear()
    pass_input.send_keys(vk_password)
    time.sleep(3)

    # эмулируем нажатие на кнопку Войти
    #login_button = wdriver.find_element_by_id("index_login_button").click()
    time.sleep(7)

    # перемещаемся на страницу профайла
    print("Going to the profile page")
    profile_page = wdriver.find_element_by_id("l_pr").click()
    time.sleep(5)

    # начинаем просмотр видео
    print("Start watching the video")
    # после перехода на страницу профайла, запускаем просмотр видео
    video_watch = wdriver.find_element_by_class_name("VideoPreview__thumbWrap").click()
    time.sleep(5)
    # заканчиваем просмотр видео
    print("Finish watching the video")

except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()





