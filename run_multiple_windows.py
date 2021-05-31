from selenium import webdriver
import time
from multiprocessing import Pool
import random

opt = webdriver.ChromeOptions()

opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# # создаем функцию, которая принимает один параметр
# def get_data(url):
#     try:
#         # создаем объект браузера
#         wdriver = webdriver.Chrome(
#             executable_path=r"C:\webriver\chromedriver.exe", options=opt)
#
#         # отправляем его по адресу
#         wdriver.get(url=url)
#         time.sleep(3)
#         # получим скрин страницы
#         wdriver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#
#     except Exception as ex:
#         print(ex)
#     finally:
#         wdriver.close()
#         wdriver.quit()
#
#
# if __name__ == '__main__':
#     # создаем переменную, котороя будет объектом класса Pool
#     # urls_list состоит из трех элементов, потому количество процессов будет 3
#     p = Pool(processes=3)
#     # вызываем метод map у объекта класса Pool
#     # передаем первым элементом функцию, а вторым итерируемый объект
#     p.map(get_data, urls_list)

# тестируем один сайт в многопроцессорном режиме
def get_data(url):
    try:
        # создаем объект браузера
        wdriver = webdriver.Chrome(
            executable_path=r"C:\webriver\chromedriver.exe", options=opt)

        # отправляем его по адресу
        wdriver.get(url=url)
        time.sleep(3)
        wdriver.find_element_by_class_name("lazyload-wrapper").find_element_by_class_name("item-video-container").click()
        time.sleep(random.randrange(3, 10))

    except Exception as ex:
        print(ex)
    finally:
        wdriver.close()
        wdriver.quit()


if __name__ == '__main__':
    # создаем переменную process_count и запросим ввод от пользователя
    process_count = int(input("Enter the number of process: "))
    # создадим переменную и запросим ввод сайта у пользователя
    url = input("Enter the site Url: ")
    # создаем переменную в которую мы положим список url-адресов, количество которых
    # будет равно количеству запускаемых процессов
    url_list = [url] * process_count
    print(url_list)
    p = Pool(processes=process_count)
    p.map(get_data, url_list)






