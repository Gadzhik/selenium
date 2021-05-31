from selenium import webdriver
import time
import datetime

opt = webdriver.ChromeOptions()

opt.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

wdriver = webdriver.Chrome(
    executable_path=r"C:\webriver\chromedriver.exe", options=opt)

try:
    # создаем переменную и помещаем в нее текущее время, для замера скорости работы скрипта
    start_point = datetime.datetime.now()

    wdriver.get("https://www.avito.ru/rossiya/avtomobili/hyundai/sonata?cd=1")
    # печатаем полученный доступ к вкладкам
    #print(wdriver.window_handles)
    # печатаем текущий url адрес
    print(f"Current url is: {wdriver.current_url}")
    # альтернатива time.sleep() -> приостанавливает исполнение кода на указанное время
    # а метод wdriver.implicitly_wait(10) -> будет ожидать элемент не более указанного времени,
    # т.е, если исполнение действия займет 1 сек, то выполнение кода продолжится без ожидания еще 9 сек
    #wdriver.implicitly_wait(3)

    time.sleep(3)
    # ищем все блоки по xpath с атрибутом data-marker
    # в результате получим список из объявлений
    items = wdriver.find_elements_by_xpath("//div[@data-marker='item-photo']")

    # собираем нулевой элемент в списке - c указанием индекса [0] появляется ошибка(items[0].click()) -> не работает
    # кликнуть по нему
    # т.о мы откроем еще одну вкладку с конкретным предложением
    items[1].click()
    #print(wdriver.window_handles)
    time.sleep(5)
    #wdriver.implicitly_wait(5)

    # перемещаемся по вкладкам браузера
    wdriver.switch_to.window(wdriver.window_handles[1])
    time.sleep(5)
    #wdriver.implicitly_wait(5)
    # печатаем текущий url адрес
    print(f"Current url is: {wdriver.current_url}")

    # парсим информацию о продавце
    username = wdriver.find_element_by_class_name("seller-info-name")
    # выводим имя продавца
    print(f"Seller user name is: {username.text}")
    print("-" * 20)
    time.sleep(5)
    #wdriver.implicitly_wait(5)

    wdriver.close()

    # отправляем драйвер на изначальную вкладку
    wdriver.switch_to.window(wdriver.window_handles[0])
    time.sleep(5)
    #wdriver.implicitly_wait(5)
    print(f"Current url is: {wdriver.current_url}")

    items[1].click()
    time.sleep(5)
    #wdriver.implicitly_wait(5)

    # переключаемся на новую вкладку
    wdriver.switch_to.window(wdriver.window_handles[1])
    time.sleep(5)
    #wdriver.implicitly_wait(5)
    print(f"Current url is: {wdriver.current_url}")
    # выводим имя пользователя
    username = wdriver.find_element_by_xpath("//div[@data-marker='seller-info/name']")
    print(f"User name is: {username.text}")
    print("+" * 20)

    ad_publ_date = wdriver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"Ad date is: {ad_publ_date.text}")
    print("-" * 20)

    # информация о дате присоединения пользователя
    seller_joined_date = wdriver.find_elements_by_class_name("seller-info-value")[1]
    print(f"User since: {seller_joined_date.text}")
    print("*" * 20)

    # время окончания работы скрипта
    end_point = datetime.datetime.now()
    # разница между ними и будет скоростью работы скрипта
    time_for_the_script_run = end_point - start_point
    print(time_for_the_script_run)

except Exception as ex:
    print(ex)
finally:
    wdriver.close()
    wdriver.quit()