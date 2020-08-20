import cv2
import pyautogui as PG
import numpy as np
import imutils
import time
from bs4 import BeautifulSoup

####### IMAGES TEMPLATE ######
img_btn_show = cv2.imread('btn_show.png') #поиск кнопки поиска
img_search_cadastr = cv2.imread('search_cadastr.png') #поиск кнопки поиска
img_wait_request = cv2.imread('wait_request.png') #поиск кнопки поиска
img_detail_title = cv2.imread('detail_title.png') #поиск кнопки поиска

url_cadaster_search = "https://e.land.gov.ua/back/cadaster/"


def get_screenshot():
    img = PG.screenshot()                           #делаем скриншот
    frame = np.array(img)                           #подгоняем в формат с которым работает opencv
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #делаем коррекцию цвета. ибо к перегнанного изображения не верные цвета
    return frame


def find_element_position(serch_element, original_img = get_screenshot()):
    res = cv2.matchTemplate(original_img, serch_element, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(res)

    return maxloc

def compare_img(template_img, original_img = get_screenshot()):
    res = cv2.matchTemplate(original_img, template_img, cv2.TM_CCOEFF_NORMED)
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(res)
    threshold = 0.9

    loc = np.where(res >= threshold)
    first = loc[0]

    if(len(first) != 0):
        return True
    else:
        return False


def main_process(cadastr):

    open_page_in_new_tab(url_cadaster_search)                          #открываем новую вкладку и вводим урл кадастра

    status = compare_img(img_btn_show)                                 # проверяем открыта ли страница Поиска кадастров. В принципе не обязательно. но пусть пока побудет
    if(status == False):
        print("НЕ открыта страница КАДАСТРА")
        #TODO функция перехода на страницу поиска кадастров


    position = find_element_position(img_search_cadastr)               #осуществялем поиск элемента для ввода. да каждый раз. да я знаю что можно только один раз. но на усякий случай
    field_center = (position[0] + 200, position[1] + 30)
    search_cadastr(cadastr, field_center)                                #выполняем ввод и поиск по нужному кадастру

    #Делаем проверку на наличии окна ожидания. Если окна нет - то выходим из цикла
    while True:
        time.sleep(1)
        status = compare_img(img_wait_request)
        if status == False:
            break


    # TODO check not data by cadastr - Делаем проверку на наличи окна - Нед данных по кадастру.
    # Есди данных сохраняем кадастр и переходим к следующему номеру
        # if true
        # send data - no data
        #return

    # TODO check page with data -
    time.sleep(1)
    status = compare_img(img_detail_title)
    if (status == False):
        print("НЕ открыта деталка")

    time.sleep(1)
    download_data(cadastr)

    PG.hotkey('ctrl', 'F4')
    time.sleep(2)

    # TODO download all data
    # TODO check download

def open_page_in_new_tab(url):
    PG.hotkey('ctrl', 't')
    time.sleep(0.4)
    PG.write(url)
    time.sleep(0.1)
    PG.press('enter')
    time.sleep(2)

def search_cadastr(cadastr_num, search_position):
    PG.moveTo(search_position)  # фокус на поле ввода кадастрового номера
    PG.click()
    PG.hotkey('ctrl', 'a')

    PG.write(cadastr_num)
    time.sleep(0.4)

    PG.press('tab')
    PG.press('enter')

def download_data(cadastr):
    PG.hotkey('ctrl', 's')

    cadastr_name = cadastr.replace(':', '_')

    time.sleep(1)
    PG.write(cadastr_name)
    time.sleep(0.1)

    PG.press('tab')
    time.sleep(0.1)

    PG.press('tab')
    time.sleep(0.2)

    PG.press('enter')
    time.sleep(0.6)

    # Save pdf

    PG.press('tab')
    time.sleep(0.1)

    PG.press('enter')
    time.sleep(0.6)


def parser_html():
    with open("1.html", "r") as f:
        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')

        data = soup.find("table", class_="table-bordered")

        for td_header in data.findAll(class_="td-header"):
            td_header.decompose()  #удаляем лишние теги

        for tr in data.findAll("tr"):
            print(tr.select("td:nth-of-type(1)"))
            print(tr.select("td:nth-of-type(2)"))
            print("---------")