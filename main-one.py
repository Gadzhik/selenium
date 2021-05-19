from selenium import webdriver
import time

# добавляем сайт который будет открывать selenium
url = "https://mvideo.ru"
wdriver = webdriver.Chrome(executable_path="C:\\webriver\\chromedriver.exe")


# в try мы пишем запросы
try:
    # вызываем метод get, куда основным параметром передаем ссылку
    wdriver.get(url=url)
    time.sleep(4)
    # если нужно перейти на еще одну/несколько страниц(у), то снова вызываем метод get
    #wdriver.get(url="https://somesite.com")
    #time.sleep(4)

    # метод для обновления окна браузера
    #wdriver.refresh()

    # делаем скриншоты сайта и сохраняем их
    #wdriver.get_screenshot_as_file("img1.png")
    #wdriver.get(url="https://yandex.ru")
    #time.sleep(4)
    #wdriver.save_screenshot("img_save.png")
    #time.sleep(2)

# в except выводим ошибки
except Exception as ex:
    print(ex)
# finally выполняется всегда, размещаем тут код закрытия драйвера
finally:
    wdriver.close()
    wdriver.quit()

# ------------------------------------------------
# Код для работы с FireFox

# from selenium import webdriver
# import time

# добавляем сайт который будет открывать selenium
# url = "https://yandex.ru"
# wdriver = webdriver.Firefox(executable_path="C:\\webriver\\geckodriver.exe")
#
#
# # в try мы пишем запросы
# try:
#     # вызываем метод get, куда основным параметром передаем ссылку
#     wdriver.get(url=url)
#     # делаем скриншоты сайта и сохраняем их
#     wdriver.save_screenshot("ya.ru")
#     time.sleep(4)
# # в except выводим ошибки
# except Exception as ex:
#     print(ex)
# # finally выполняется всегда, размещаем тут код закрытия драйвера
# finally:
#     wdriver.close()
#     wdriver.quit()








